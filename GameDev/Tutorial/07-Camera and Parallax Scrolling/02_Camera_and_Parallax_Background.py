
# Reference
# https://www.youtube.com/watch?v=5q7tmIlXROg

# In side-scrolling games like Sonic the Hedgehog or simply Zelda games, the map has to be scrolled to
# follow the player.
# This terminology is also referred as "Camera", because in idea it is like a camera was following the
# main character in the game.
#
# Do we actually have an camera in the game? Turns out, it is not actually camera, but simply all the objects
# are moved to produce the effect of camera is following the player.
# Like in Super Mario, the player starts out at leftmost part of the map. All the tiles are blitted exactly as
# where they are.
# When the player begins to move to the right, the scroll position increases, where all the tile and object will be
# offseted by certain value to the left as Mario moves to the right, thus creating the effect of scrolling.
#
# Of course, we would not want our game to scroll off our map, revealing parts that aren't mapped (probably void),
# so scrolling would use some boundary checking as well!
#
# Here's how you would (preferably) implement scrolling:
#   >   Originally, when we press WASD, the player's rect will be moved to the new position. All the tiles remain at
#       their own place. We will perform boundary checking and collision detection using tile's rect and player's rect
#   >   With scroll value (x,y) which x indicates how far player moved to the right, and y as how high player moved,
#       as x increases in value, all the objects has to be shifted by x units (INCLUDING THE PLAYER) to the left to
#       seem as camera is following the player.
#   >   HOWEVER, DO NOT UPDATE THE RECT'S POSITION TO SUIT THE SCROLL_VALUE. The rects should remain in place just like
#       when the game just started:
#           - The player's rect x and y still moves according to keyboard input
#           - The tiles's rect remain in place
#       We only shift everything by scroll value when blitting! This is because changing the rect's position will mess
#       up the collision detection BADLY.
#   >   The camera will be following the player. Therefore, every frame we compute the new scroll_value by the formula:
#
#             [ Difference in player's pos and camera pos ]    [ To make the player on center of screen. Otherwise
#                                                              [  player will be fixed on left edge of screen ]
#                                V                                  V
#           scroll_x = ( player.x - scroll_x     - screen.width // 2 )
#
#   >   When shifting by scroll_value, we would introduce some "lag" into the camera which creates a much smoother
#       animation instead of the camera fixed tightly onto the player. This is done by dividing the increment value by
#       some constant, like:
#
#                                               [ The camera will not move immediately to player ]
#                                                                   V
#           scroll_x = ( player.x - scroll_x - screen.width // 2 ) // 20
#


import pygame
import os.path as path
import csv

pygame.init()
screen = pygame.display.set_mode( (600, 400) )
pygame.display.set_caption('Camera')
v_screen = pygame.Surface( (300, 200) )
clock = pygame.time.Clock()

######################
# Tile class
######################
class Tile(pygame.sprite.Sprite):
    TILE_SIZE = (10,10)
    BASE_PATH = path.join('../Assets', 'platformer', 'Tiles')

    # Tile ID Mapping
    # 0 - Nothing (Background)
    # 1 - Grass middle
    # 2 - Dirt
    # 3 - Grass rounded left
    # 4 - Grass rounded right
    # 5 - Grass cliff left
    # 6 - Grass cliff right
    TILE_IMG = [
        None,
        pygame.transform.scale( pygame.image.load( path.join( BASE_PATH, 'grassMid.png') ).convert_alpha(), TILE_SIZE ),
        pygame.transform.scale( pygame.image.load( path.join( BASE_PATH, 'grassCenter.png') ).convert_alpha(), TILE_SIZE ),
        pygame.transform.scale( pygame.image.load( path.join( BASE_PATH, 'grassLeft.png') ).convert_alpha(), TILE_SIZE ),
        pygame.transform.scale( pygame.image.load( path.join( BASE_PATH, 'grassRight.png') ).convert_alpha(), TILE_SIZE ),
        pygame.transform.scale( pygame.image.load( path.join( BASE_PATH, 'grassCliffLeft.png') ).convert_alpha(), TILE_SIZE ),
        pygame.transform.scale( pygame.image.load( path.join( BASE_PATH, 'grassCliffRight.png') ).convert_alpha(), TILE_SIZE ),
    ]

    def __init__(self, tile_id, location ):
        super().__init__()
        self.image = Tile.TILE_IMG[ int(tile_id) ]
        self.rect = self.image.get_rect()
        self.rect.top = location[0] * Tile.TILE_SIZE[1]
        self.rect.left = location[1] * Tile.TILE_SIZE[0]




######################
# TileMap class
######################
class TileMap(pygame.sprite.Group):
    def __init__(self, tile_map_path, screen: pygame.Surface):
        super().__init__()
        self.screen = screen

        with open(tile_map_path) as tile_map_file:
            tile_map_reader = csv.reader(tile_map_file)
            for i, row in enumerate(tile_map_reader):
                for j, tile_id in enumerate(row):
                    if tile_id != '0':
                        self.add( Tile( tile_id, (i,j) ) )
        print("Tilemap loaded successfully")

    def draw(self, scroll_value):
        # Fill background sky color
        self.screen.fill( (163, 214, 255) )
        # Hills background
        # Let's apply the technique of parallax scrolling we learned earlier to the hills!
        # it shall be moving slower than the player, so we multiply the scroll value by some constant smaller than 1
        background_scroll_value = ( -scroll_value[0] * 0.2, -scroll_value[1] * 0.2 )

        pygame.draw.rect(self.screen, (1, 97, 46), pygame.Rect(0, 150 ,300, 150).move(0, background_scroll_value[1]))
        pygame.draw.rect(self.screen, (32, 191, 107), pygame.Rect(20, 60, 50, 140).move( background_scroll_value ) )
        pygame.draw.rect(self.screen, (38, 222, 129), pygame.Rect(60, 40, 100, 160).move( background_scroll_value ) )
        pygame.draw.rect(self.screen, (33, 173, 102), pygame.Rect(220, 100, 70, 130).move( background_scroll_value ) )
        pygame.draw.rect(self.screen, (14, 153, 79), pygame.Rect(200, 80, 30, 120).move( background_scroll_value ))
        # For all the tiles, apply the scroll value and draw them
        for sprite in self.sprites():
            self.screen.blit( sprite.image, sprite.rect.move(-scroll_value[0], -scroll_value[1]))


############################
# Player class
############################
class Player(pygame.sprite.Sprite):
    GRAVITY = 0.4
    PLAYER_SIZE = (12,16)
    IMG_PATH = path.join('../Assets', 'platformer', 'Player', 'p3_stand.png')

    def __init__(self, screen: pygame.Surface):
        super().__init__()
        self.image_right = pygame.transform.smoothscale( pygame.image.load( Player.IMG_PATH ), Player.PLAYER_SIZE ).convert_alpha()
        self.image_left = pygame.transform.flip(self.image_right, True, False)
        self.image = self.image_right
        self.rect = self.image.get_rect()
        self.screen = screen
        self.rect.topleft = ( 0, self.screen.get_height() // 2 )
        self.dx = 0
        self.dy = 0
        self.is_in_air = True

    def move(self, key_event):
        if key_event.type == pygame.KEYDOWN:
            if key_event.key == pygame.K_w and not self.is_in_air:
                self.dy = -6
                self.is_in_air = True
            elif key_event.key == pygame.K_d:
                self.dx += 2
            elif key_event.key == pygame.K_a:
                self.dx -= 2
        elif key_event.type == pygame.KEYUP:
            if key_event.key == pygame.K_a:
                self.dx += 2
            elif key_event.key == pygame.K_d:
                self.dx -= 2

    # Update the camera position based on player's position
    def update_scroll_position(self, scroll_position):
        # (self.rect.x - scroll_position[0]) is the difference between camera position and player's position.
        # However we want the player to be centered, that's why we subtract by half width of screen.
        # Same logic applies to the y component
        # Then, we can divide the increment value by a constant to apply some camera "lag" which looks smooth
        scroll_position[0] += (self.rect.x - scroll_position[0] - self.screen.get_width() // 2) // 20
        scroll_position[1] += (self.rect.y - scroll_position[1] - self.screen.get_height() // 2) // 20

        # We don't want player to look through the map boundary.
        scroll_position[0] = max(0, min(scroll_position[0], 900 - self.screen.get_width() ) )
        scroll_position[1] = min(0, scroll_position[1] )  # Note that positive y is downwards

    # Moves the character. Check collision
    def update(self, tile_map ):
        if self.dx != 0:
            # Move while checking screen boundary. NOTE THE NEW SCREEN BOUNDARY IS 0 TO 900 BECAUSE OF EXTENDED MAP
            self.rect.left += self.dx
            self.rect.left = max(0, self.rect.left)
            self.rect.right = min(self.rect.right, 900 )

            # Check for tile collision
            for tile in map( lambda t: t.rect, tile_map.sprites() ):
                if self.rect.colliderect( tile ):
                    if self.dx > 0:
                        self.rect.right = tile.left
                    else:
                        self.rect.left = tile.right

        # Move Vertically. Note that we do not care if character goes over the top or bottom of screen boundary
        self.rect.top += self.dy
        # Check for tile collision
        for tile in map( lambda t: t.rect, tile_map.sprites() ):
            if self.rect.colliderect( tile ):
                if self.dy > 0:
                    self.rect.bottom = tile.top
                    self.is_in_air = False
                else:
                    self.rect.top = tile.bottom
                self.dy = 0
        self.dy = min(10, self.dy + Player.GRAVITY)

    def draw(self, scroll_value):
        if self.dx > 0:
            self.image = self.image_right
        elif self.dx < 0:
            self.image = self.image_left
        self.screen.blit( self.image, self.rect.move(-scroll_value[0], -scroll_value[1]) )


tile_map = TileMap( path.join('../Assets', 'tilemap2.csv'), v_screen )
player = Player( v_screen )

scroll_value = [0,0]

should_exit = False
while not should_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            should_exit = True
        else:
            player.move(event)

    # Updating Logics - Scrolling and Collision
    player.update( tile_map )
    player.update_scroll_position(scroll_value)

    tile_map.draw( scroll_value )
    player.draw( scroll_value )


    screen.blit( pygame.transform.scale(v_screen, screen.get_size(), screen), (0,0) )
    pygame.display.flip()

    dt = clock.tick(60)


pygame.quit()
quit()
