
# As previously mentioned, tiles can be of many types. Tiles may be collidable or non-collidable, and interactable
# or non-interactable (Like the '?' block in Mario games).
# This time we'll look at Ramps - One of the special tile type that needs special handling.
#
# The main use of ramps is to allow us to move horizontally while changing our vertical position. Therefore,
# the collision detection of ramps would differ from the ones used in normal rectangular tiles. Furthermore,
# left ramp and right ramp would have different collision detection algorithm!
#
# The most basic way to handle ramp collision, is to:
#
#                ---
#             ---   |
#          ---      |
#       ------------|
#
# > First, get the x position of the player relative to the ramp. Say, our player is at 1/2 to the left of the ramp.
# > From the x position, we need to somehow deduce the y position that the player is supposed to be, depending
#   on the shape of the ramp. Usually, the ramp is triangular in shape, and thus we would use basic mathematics
#   to deduce the y position of the player.
#
#   Some ramps, like the one above (Where gradient is exactly 1 -> y=x), then the MIN y position is same as x position!
#   For other side, like:
#
#    ---
#   |   ---
#   |      ---
#   |------------
#
#   If the gradient is -1, (y=-x), then the MIN y position would simply be ( HEIGHT OF RAMP - x ).
#
# It may seem quite simple, but it is actually almost twice as complex as normal rectangular tiles. Problems:
#   >   You need to deduce the supposed y offset of the player depending on the player's relative x offset from the
#       ramp, and the ramp's shape
#
#   >   If we deduce the y offset depending on player's bottomleft / bottomright position, the player would look
#       'floating' on the ramp, like in this example game.
#
#   >   'Teleportation' issue when the player collides with the ramp from the flat side
#            /|
#           / |   <--- Player comes from here
#       If you do not implement the feature, the player would immediately teleport to the top of the ramp
#
#   >   Actual collision. Since the ramp is still a tile that is rectangular in shape, some part of the tile is actually
#       space! We need to know if the player is actually colliding with the ramp and not simply the space part of the
#       tile, to update some properties (Like jump reset, or set dy to 0)

import sys
import pygame
import csv
import os.path as path

pygame.init()
screen = pygame.display.set_mode( (600,400) )
v_screen = pygame.Surface( (300, 200) )
clock = pygame.time.Clock()

BASE_PATH = path.join('Assets', 'platformer', 'Tiles')
#################################
# Tile Class - For normal tiles
#################################
class Tile(pygame.sprite.Sprite):
    TILE_SIZE = (10,10)
    GRASS_MID = pygame.transform.scale( pygame.image.load( path.join(BASE_PATH, 'grassMid.png') ).convert(),
                                        TILE_SIZE )
    DIRT = pygame.transform.scale(pygame.image.load(path.join(BASE_PATH, 'grassCenter.png')).convert(),
                                  TILE_SIZE )
    GRASS_HILL_LEFT2 = pygame.transform.scale( pygame.image.load( path.join(BASE_PATH, 'grassHillLeft2.png') ).convert(),
                                               TILE_SIZE )
    GRASS_HILL_RIHGT2 = pygame.transform.scale( pygame.image.load( path.join(BASE_PATH, 'grassHillRight2.png') ).convert(),
                                                TILE_SIZE )

    def __init__(self, tile_id, location):
        super().__init__()
        self.image = None
        if tile_id == 1:
            self.image = Tile.GRASS_MID
        elif tile_id == 2:
            self.image = Tile.DIRT
        elif tile_id == 11:
            self.image = Tile.GRASS_HILL_LEFT2
        else:
            self.image = Tile.GRASS_HILL_RIHGT2
        self.rect = self.image.get_rect().move( location[1] * Tile.TILE_SIZE[0], location[0] * Tile.TILE_SIZE[1] )

    def handle_vertical_collision(self, player):
        if self.rect.colliderect(player.rect ):
            if player.dy > 0:
                player.rect.bottom = self.rect.top
                player.dy = 0
                player.is_in_air = False
            else:
                player.rect.top = self.rect.bottom
            player.dy = 0

    def handle_horizontal_collision(self, player):
        if self.rect.colliderect(player.rect ):
            if player.dx > 0:
                player.rect.right = self.rect.left
            else:
                player.rect.left = self.rect.right


###################################################################################
# Ramp class - Inherits Tile (Better design would be Tile -> (Square Tile / Ramp )
###################################################################################
class Ramp(pygame.sprite.Sprite):

    GRASS_HILL_LEFT = pygame.transform.scale( pygame.image.load( path.join(BASE_PATH, 'grassHillLeft.png') ).convert_alpha(),
                                              Tile.TILE_SIZE )
    GRASS_HILL_RIGHT = pygame.transform.scale(pygame.image.load(path.join(BASE_PATH, 'grassHillRight.png')).convert_alpha(),
                                              Tile.TILE_SIZE)

    def __init__(self, tile_id, location ):
        super().__init__()
        self.image = None
        # Ramp's collision detection differs by their direction too - Left Ramp / Right Ramp
        self.type = None
        if tile_id == 9:
            self.image = Ramp.GRASS_HILL_LEFT
            self.type = 'LEFT'
        else:
            self.image = Ramp.GRASS_HILL_RIGHT
            self.type = 'RIGHT'
        self.rect = self.image.get_rect().move( location[1] * Tile.TILE_SIZE[0], location[0] * Tile.TILE_SIZE[1] )

    # Obtains the supposed y position offset of the player if standing on the ramp, determined by player's x position.
    # However, it is bounded to TILE_SIZE so it never returns value higher than tile size
    def get_relative_y_pos(self, player):
        if self.type == 'LEFT':
            rel_y = min( Tile.TILE_SIZE[0], player.rect.right - self.rect.left )
        else:
            rel_y = min( Tile.TILE_SIZE[0], self.rect.right - player.rect.left )
        return rel_y

    def handle_vertical_collision(self, player):
        if self.rect.colliderect(player.rect ):
            # The supposed y position offset of player if it truely is standing on ramp
            y_rel_pos = self.get_relative_y_pos(player)

            # Collision from above the ramp (Which the player might not even be touching the ramp at all, but simply
            # the rect's empty space. We need to check that
            if player.dy > 0 and player.rect.bottom >= self.rect.bottom - y_rel_pos:
                player.rect.bottom = self.rect.bottom - y_rel_pos
                player.dy = 0
                player.is_in_air = False

    def handle_horizontal_collision(self, player):
        if self.rect.colliderect(player.rect):
            player.rect.bottom = min( player.rect.bottom, self.rect.bottom - self.get_relative_y_pos(player) )


#########################
# Tile Map Class
#########################
class TileMap(pygame.sprite.Group):
    def __init__(self, tile_map_location):
        super().__init__()

        with open(tile_map_location) as tile_map_file:
            tile_map_reader = csv.reader(tile_map_file)
            for i, row in enumerate(tile_map_reader):
                for j, tile_id in enumerate(row):
                    if tile_id != '0':
                        if tile_id not in ('9', '10'):
                            self.add( Tile( int(tile_id), (i,j) ) )
                        else:
                            self.add( Ramp( int(tile_id), (i,j) ) )
        print("Tilemap loaded successfully")

    def draw(self, surface: pygame.Surface):
        surface.fill( (163, 214, 255) )
        pygame.draw.rect(surface, (38, 222, 129), (20, 60, 50 ,140) )
        pygame.draw.rect(surface, (32, 191, 107), (60, 40, 100, 160))
        pygame.draw.rect(surface, (14, 130, 69), (200, 80, 30, 120))
        super().draw(surface)


#############################
# Player Class
#############################
class Player(pygame.sprite.Sprite):
    GRAVITY = 0.4
    PLAYER_SIZE = (12,16)
    IMG_PATH = path.join('Assets', 'platformer', 'Player', 'p3_stand.png')

    def __init__(self, screen: pygame.Surface):
        super().__init__()
        self.image = pygame.transform.smoothscale( pygame.image.load( Player.IMG_PATH ), Player.PLAYER_SIZE )\
            .convert_alpha()
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

    def update(self, tile_map):
        if self.dx != 0:
            self.rect.left += self.dx
            self.rect.left = max(0, self.rect.left)
            self.rect.right = min(self.rect.right, self.screen.get_width() )

            for tile in tile_map.sprites():
                tile.handle_horizontal_collision(self)

        self.rect.top += self.dy
        # Check for tile and ramp collision
        for tile in tile_map.sprites():
            tile.handle_vertical_collision(self)

        self.dy = min(10, self.dy + Player.GRAVITY)

    def draw(self):
        self.screen.blit( self.image, self.rect )



tile_map = TileMap( path.join('Assets', 'tilemap4.csv') )
player = Player( v_screen )

should_exit = False
while not should_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            should_exit = True
        else:
            player.move(event)

    player.update( tile_map )

    tile_map.draw( v_screen )
    player.draw()

    screen.blit( pygame.transform.scale(v_screen, screen.get_size(), screen), (0,0) )
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
