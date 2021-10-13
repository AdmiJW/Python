# Here, we will try to produce a cool particle effect - Sparks
# These kind of particles usually show as a kind of attack pattern - Eg: When you slash an enemy with a sword, or
# when you cast some sort of magic
#
# The shape of spark goes best with a diamond shape, where it can be defined with those parameters:
#
#          (A)
#          /|\
#        /  |  \
#      /    |    \
# (B)/      X------\ (C)
#    \      |      /
#     \     |     /
#      \    |    /
#       \   |   /
#        \  |  /
#         \ | /
#          \|/
#          (D)
#
# The X is the center point, and from the X, we have the head length (Upwards), head radius (Right), and tail
# length (Downwards).
# With those three parameters, we can easily draw the polygon already - Defined by the 4 points.
#
# However, they should be also able to rotate, and using a little bit of trigonometry, we can easily rotate the spark
# around. This should be easier if you know about vectors and trigonometry. The formula is:
#
#   X component: cos( deg ) * length
#   Y component: -sin( deg ) * length

import math
import random
import sys

import pygame

SCREEN_SIZE = (960, 720)
DESIRED_FPS = 60

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()


#########################################
# Spark Particle
#########################################
# A spark needs the following attributes:
class Spark:
    # Here is the ratio between head length: head radius: tail length
    # This way we can draw them based on only 1 variable: life (or some other better name i dunno)
    HEAD_LENGTH_RATIO = 4
    HEAD_RADIUS_RATIO = 1
    TAIL_LENGTH_RATIO = 8
    # The speed at which the Spark decays.
    DECAY_RATE = 0.25

    def __init__(self, center: pygame.Vector2, initial_life: float, initial_velocities: pygame.Vector2):
        self.life = initial_life
        self.center = center
        self.velocity = initial_velocities
        self.is_alive = True

    # Several things to update:
    # - Decrement life (Spark decaying)
    # - Apply gravity (if set)
    # - Apply velocity (Spark movement)
    def update(self, dt: float, gravity: float = None):
        # Decrement Life (Decay)
        self.life -= (Spark.DECAY_RATE * dt)
        if self.life <= 0:
            self.is_alive = False
            return

        # Apply gravity (If set)
        if gravity is not None:
            self.velocity.y += (gravity * dt)

        # Apply velocity
        self.center = self.center + (self.velocity * dt)

    # Optional. Will rotate the spark for even cooler effects
    def update_rotation(self, dt:float):
        angle = self.get_angle()
        resultant = self.velocity.length()
        angle = (angle + 0.1 * dt) % (math.pi * 2)
        # Apply rotation back to the velocity vector
        self.velocity = pygame.Vector2( math.cos(angle) * resultant, -math.sin(angle) * resultant )


    # Render: broken down into several steps:
    # - Determine the angle of the spark using velocity direction vector
    # - Find 4 points of the diamond shape, with angle applied
    # - Draw the polygon using these 4 points
    def render(self, screen: pygame.Surface):
        angle = self.get_angle()

        # Deduce the 4 points
        # Offsets is simply the offset vector that should be added to the center point c
        ptAOffset = pygame.Vector2(
            math.cos(angle) * self.life * Spark.HEAD_LENGTH_RATIO,
            -math.sin(angle) * self.life * Spark.HEAD_LENGTH_RATIO
        )
        ptBOffset = pygame.Vector2(
            math.cos(angle + math.pi / 2) * self.life * Spark.HEAD_RADIUS_RATIO,
            -math.sin(angle + math.pi / 2) * self.life * Spark.HEAD_RADIUS_RATIO
        )
        ptCOffset = pygame.Vector2(
            math.cos(angle + math.pi) * self.life * Spark.TAIL_LENGTH_RATIO,
            -math.sin(angle + math.pi) * self.life * Spark.TAIL_LENGTH_RATIO
        )
        ptDOffset = pygame.Vector2(
            math.cos(angle + 3 * math.pi / 2) * self.life * Spark.HEAD_RADIUS_RATIO,
            -math.sin(angle + 3 * math.pi / 2) * self.life * Spark.HEAD_RADIUS_RATIO
        )
        ptA = self.center + ptAOffset
        ptB = self.center + ptBOffset
        ptC = self.center + ptCOffset
        ptD = self.center + ptDOffset

        # - Draw the polygon using these 4 points
        pygame.draw.polygon(screen, (255, 255, 255), (ptA, ptB, ptC, ptD))

    # - Determine the angle of the spark using velocity direction vector
    def get_angle(self):
        if self.velocity.x == 0:
            return math.pi / 2 if self.velocity.y >= 0 else 3 * math.pi / 2

        tangent = math.atan(abs(self.velocity.y / self.velocity.x))
        # 4 quadrants for angle.
        # REMEMBER in computer graphics world, y axis is flipped!!!!
        if self.velocity.y < 0:
            return tangent if self.velocity.x >= 0 else math.pi - tangent
        return 2 * math.pi - tangent if self.velocity.x >= 0 else math.pi + tangent


#############################################
# Spark Emitter that follows the Mouse
# Emits Sparks at 15deg increment at intervals
#############################################
class IntervalSparkEmitter:
    def __init__(self, interval: int, initial_life: float = 5, resultant_velocity: float = 8,
                 gravity: float = None):
        self.interval = interval
        self.initial_life = initial_life
        self.resultant_velocity = resultant_velocity
        self.gravity = gravity

        self.sparks = set()
        self.timer = 0

    def update(self, dt: float, rotate:bool = False):
        self.timer -= dt

        # Add new sparks if the timer is up.
        if self.timer < 0:
            mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
            self.timer = self.interval
            for angle in range(0, 360, 15):
                radians = math.radians(angle)
                init_velocity = pygame.Vector2(
                    math.cos(radians) * self.resultant_velocity,
                    -math.sin(radians) * self.resultant_velocity
                )
                self.sparks.add(Spark(mouse_pos, self.initial_life, init_velocity))

        # Update existing sparks - Following mouse position, and apply gravity
        died_sparks = []
        for spark in self.sparks:
            if rotate:
                spark.update_rotation(dt)
            spark.update(dt, self.gravity)
            if not spark.is_alive:
                died_sparks.append(spark)

        # Remove died sparks
        for died_spark in died_sparks:
            self.sparks.remove(died_spark)

    def render(self, screen: pygame.Surface):
        for spark in self.sparks:
            spark.render(screen)


#############################################
# Spark Emitter that follows the Mouse
# Emits Sparks in random direction at intervals
#############################################
class RandomDirectionSparkEmitter:
    def __init__(self, interval: int, initial_life: float = 5, resultant_velocity: float = 8,
                 gravity: float = None):
        self.interval = interval
        self.initial_life = initial_life
        self.resultant_velocity = resultant_velocity
        self.gravity = gravity

        self.sparks = set()
        self.timer = 0

    def update(self, dt: float, rotate:bool = False):
        self.timer -= dt

        # Add new sparks if the timer is up.
        if self.timer < 0:
            mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
            self.timer = self.interval
            radians = random.random() * math.pi * 2
            init_velocity = pygame.Vector2(
                math.cos(radians) * self.resultant_velocity,
                -math.sin(radians) * self.resultant_velocity
            )
            self.sparks.add(Spark(mouse_pos, self.initial_life, init_velocity))

        # Update existing sparks - Following mouse position, and apply gravity
        died_sparks = []
        for spark in self.sparks:
            if rotate:
                spark.update_rotation(dt)
            spark.update(dt, self.gravity)
            if not spark.is_alive:
                died_sparks.append(spark)

        # Remove died sparks
        for died_spark in died_sparks:
            self.sparks.remove(died_spark)

    def render(self, screen: pygame.Surface):
        for spark in self.sparks:
            spark.render(screen)





#####################################
# Game Loop
#####################################
should_exit = False

enable_rotation = False
spark_gens = [
    RandomDirectionSparkEmitter(1, 4, 18, 2),   # Random direction sparks with gravity
    RandomDirectionSparkEmitter(1, 8, 14),      # Random direction sparks
    IntervalSparkEmitter(8, 3, 15, 1.5),        # Interval sparks with gravity
    IntervalSparkEmitter(5, 8, 12),             # Interval sparks. Best effect with rotation
]
selected_spark = 0


prompt1 = pygame.font.SysFont('Arial', 20).render('press ENTER to switch spark generator type', True, (255,255,255))
prompt2 = pygame.font.SysFont('Arial', 20).render('press SPACE to toggle SPARK ROTATION', True, (255,255,255))
prompt1rect = prompt1.get_rect(top=0, centerx=screen.get_rect().centerx)
prompt2rect = prompt1.get_rect(top=prompt1rect.bottom, centerx=screen.get_rect().centerx)

while not should_exit:
    dt = clock.tick(DESIRED_FPS) * 0.001 * DESIRED_FPS
    print(clock.get_fps())

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            should_exit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                enable_rotation = not enable_rotation
            elif event.key == pygame.K_RETURN:
                selected_spark = (selected_spark + 1) % len(spark_gens)

    # Update
    spark_gens[selected_spark].update(dt, enable_rotation)

    # Rendering
    screen.fill((0, 0, 0))
    screen.blit( prompt1, prompt1rect )
    screen.blit(prompt2, prompt2rect)
    spark_gens[selected_spark].render(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
