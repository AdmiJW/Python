# You have seen these games before: Enemies has a line of sight, and would detect the player if the player stands
# in its field of vision. How the heck it is achieved in games, even in 2D?
#
# The topic involved is raycasting, and it is also used in lighting - detecting objects that will
# block the light.
# Essentially, each light source would be emitting light in all directions, 360 degree. The most basic raycasting would
# be to have, perhaps 360 rays, each emitting at an angle of x degree from the light source. Then, we would have:
#
# > Ray object
#       - Represents a light ray emitted from a light emitting source centered at c (x,y)
#       - Contains center point c (x,y) and direction vector (x,y)
# > Boundary object
#       - Represents a opaque object that will block the light ray from passing through it
#       - Contains two points - Starting point a (x,y) and ending point b (x,y)
#
# Intuitively, every frame in our game, we would have a collection of Ray objects and Boundary objects on our map.
# For each of the rays, we would do some vector mathematics to see if the ray will intersect with the line segment
# formed by the Boundary or not.
# BTW, the mathematics involved with said algorithm would be "line-line intersection":
#       https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
#
# The time complexity of this algorithm would be O(R * B) where R = number of Rays and B = number of boundaries.
# Each Ray object would check against B boundaries to see whether the ray intersected with the boundary or not.
# If there are more than 1 boundary that the ray is intersecting, then we would take only the one closest to the ray
# source, since that's how light works!
#
#
# What's next?
#
# You might argue: We are doing nothing but simply drawing lines out from a light emitting object! What you want is
# actually a nice looking 'circle' representing the field of view.
# In reality, light is simply electromagnetic waves, lots of them, way more than just 360 rays (1 ray per degree).
# What we could do as a good starting point, is to basically draw a triangle between two adjacent rays
# (Say, draw a triangle between 3 points: Center, Ray of 45 deg, Ray of 46 deg)
# If the degree are not sparsely spaced out, you will get approximately a circle looking shape.
#
# However, of course this is not the only way you could implement Raycasting. There are more way, way better algorithms
# that runs in better efficiency than having to iterate through all rays and boundaries like this.
# See:
#       https://www.redblobgames.com/articles/visibility/#ray-casting
#
import math
import sys
import pygame

SCREEN_SIZE = (960,720)

pygame.init()
screen = pygame.display.set_mode( SCREEN_SIZE )
clock = pygame.time.Clock()



###########################
# Wall Object
###########################
# A wall is simply a straight line - Contains p1 (x,y) and p2 (x,y)
class Wall:
    WIDTH = 5

    def __init__( self, x1:int, y1:int, x2:int, y2:int ):
        self.p1 = pygame.Vector2(x1, y1)
        self.p2 = pygame.Vector2(x2, y2)

    def render(self, screen:pygame.Surface):
        pygame.draw.line(screen, (255,255,255), self.p1, self.p2, Wall.WIDTH)


###########################
# Ray object
###########################
# A ray originating from a center point c (x,y).
# It also contains a direction (Represented by direction vector) v
class Ray:
    VIEW_RADIUS = 300

    def __init__(self, x:int, y:int, degree:float):
        radians = math.radians( degree )
        # Center point
        self.c = pygame.Vector2(x, y)
        # Direction Vector - Remember that in this world, positive y is downwards
        self.direction_vector = pygame.Vector2( math.cos(radians), -math.sin(radians) )
        # Target - The point of intersection with the Wall that the ray ends.
        self.target = None


    def project_ray( self, walls:list[Wall] ):
        self.target = self.c + self.direction_vector * Ray.VIEW_RADIUS
        closest_distance = Ray.VIEW_RADIUS

        for wall in walls:
            intersection_point = self.check_intersection(wall.p1, wall.p2, self.c, self.direction_vector)
            if intersection_point is None: continue

            if self.c.distance_to(intersection_point) < closest_distance:
                closest_distance = self.c.distance_to(intersection_point)
                self.target = intersection_point

    def set_center( self, x:int, y:int ):
        self.c.xy = x, y

    # Note that 0deg is this direction: ---->
    def set_direction_vector( self, degree:float ):
        radians = math.radians(degree)
        self.direction_vector.x = math.cos(radians)
        self.direction_vector.y = -math.sin(radians)

    def render( self, screen:pygame.Surface ):
        if self.target is not None:
            pygame.draw.aaline(screen, (100,100,100), self.c, self.target )


    # Checks for intersection between a line segment and a direction vector from center point c
    # Returns None if no intersection, otherwise returns a vector2 which is point of intersection
    @staticmethod
    def check_intersection(line1A: pygame.Vector2, line1B: pygame.Vector2,
                           center: pygame.Vector2, direction_vector: pygame.Vector2):
        x1, y1 = line1A
        x2, y2 = line1B
        x3, y3 = center
        x4, y4 = center + direction_vector

        denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

        # Denominator == 0 means wall and ray are parallel. No blocking
        if denominator == 0: return None

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denominator
        u = ((x1 - x3) * (y1 - y2) - (y1 - y3) * (x1 - x2)) / denominator

        # No intersection. Return
        if not 0 <= t <= 1 or u <= 0: return None
        # Return intersecting point
        return pygame.Vector2(x1 + t * (x2 - x1), y1 + t * (y2 - y1))


#############################
# Game Loop
#############################
walls = [
    Wall( 100, 0, 100, 350),
    Wall( 0, 400, 500, 400 ),
    Wall( 300, 0, 300, 200 ),
    Wall( 500, 0, 500, 200 ),
    Wall( 300, 200, 460, 200 ),

    Wall( 700, 0, 700, 50),
    Wall( 700, 60, 700, 100),
    Wall( 700, 110, 700, 150),
    Wall( 700, 160, 700, 200),
    Wall( 700, 210, 700, 250),
    Wall( 700, 260, 700, 300),
    Wall( 700, 310, 700, 350),
    Wall( 700, 360, 700, 700),

    Wall( 200, 500, 500, 500 )
]
rays = [ Ray(0, 0, deg / 2) for deg in range(720) ]

should_exit = False
while not should_exit:
    dt = clock.tick(60) * 0.001 * 60
    print(clock.get_fps())
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            should_exit = True

    # Update
    for ray in rays:
        ray.set_center( *pygame.mouse.get_pos() )
        ray.project_ray( walls )

    # Render
    screen.fill( (0,0,0) )
    for wall in walls:
        wall.render(screen)
    for ray in rays:
        ray.render(screen)
    pygame.display.flip()


pygame.quit()
sys.exit()
