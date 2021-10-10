#####################################################################################################################
# In most of the platforming games, the map itself can be thought as tiles, or a plane of grids.
# Therefore, when loading the game, some tiles will be reused many times, with the same image (Eg: grass tile)
#
# So, we will be using TileMaps, which is essentially an array that shows which tile shall be placed on where.
# Usually, we will use external software to help us construct our map with tiles. Then, the tilemap would be
# exported in certain format, like a csv that shows the id of the tile in each grid.
#
# To ensure our character will be standing on the tiles and not fall through it, we will need to check for collision
# on each of the tiles. However for performance, only the tiles that is ever possible to be touched by the player shall
# be checked.
#
# While checking for collision, one way to make the logic easier, is to separate collision detection on x and y axis
# (In other words, two passes). This separates the concern on whether the player is colliding on a certain tile from
# left/right, or up/down.
#
# So when moving the character, we first move its x position, check collision, then only move its y position and
# check for collision once again
#
#
# ############################
# Food For Thought
# ############################
#   >   If we have a large, large map (or even infinite, like the case of Minecraft), do we have to do collision
#       checking on ALL of the tiles? (In case of infinite map, then infinite tiles to check!)
#       One solution is to separate the map into 'chunks', which are smaller rectangular area of the map, containing
#       a fixed number of tiles.
#       Only when the player is inside the chunk, then collision checking needs to be done to the tiles in that chunk
#       Also, the idea of 'chunk' allows rendering what's visible on the screen only, instead of rendering ALL of the
#       tiles in the world!
#
#       'Chunk' itself deserves a standalone tutorial on that, because the idea itself is not so simple, yet very
#       important in 2D games (or 3D games like Minecraft!)
#
#   >   When doing collision detection, you may have faced this dilemma:
#           |   Between Collidable and Collider, which one do I implement collision logic in it?
#
#       For example, Collidable is Tiles, and Collider is Player.
#       If I implement collision logic in Collidable, then it look look like:
#
#           class Tile:
#               def check_collision(player):...
#
#       Otherwise,
#
#           class Player:
#               def check_collision(tile):...
#
#       Here's some tips to help you make your decision:
#       - Think about relationship. Is Collider to Collidable 1-to-many relationship?
#         Aka there is only 1 player, and many tiles to check
#       - Think about complexity. When collider collides with collidable, which one involves more complex logic?
#         In case of player colliding the tile, the complex logic goes to Player.
#
#       Consider that player not only has normal tiles, maybe it can also collide with spikes, ramps, etc
#       If we choose to implement logic in Player, then:
#
#           class Player:
#               def check_collision_tile(tiles):...
#               def check_collision_spike(spikes):...
#               def check_collision_ramp(ramps):...
#
#       On the other hand:
#
#           class Tile:
#               def collide_player(player):...
#           class Spike:
#               def collide_player(player):...
#           class Ramp:
#               def collide_player(player):...
#
#       You'll decide

import pygame
import os.path as path
import csv


pygame.init()
screen = pygame.display.set_mode( (600, 400) )

#############################
# Tile class
#############################
# Food for Thought: Tiles can either be interactable (like collision), or non interactable.
# This is such that when player collides with the tile, the Tile's interact() method will be invoked.
# We can use polymorphism for Tile class, like CollidableTile and NonCollidableTile
#
# Eg:
#
#          Tile
#         /    \
# Interactable  Non-interactable
#   /        \
# Collidable  PortalTile etc...
#
# However we don't do that in this example. Simply take note of this good practice of polymorphism!
#
# ===============================================
# You should realize that not all of the tiles on the map needs to be checked for collision. Some tiles, like
# the ones in the underground, buried, shall not be check for collision because it should be impossible for player
# to end up colliding with it. This saves the computations needed especially on large maps.
#
class Tile(pygame.sprite.Sprite):
    TILE_SIZE = (10,10)
    BASE_PATH = path.join('Assets', 'platformer', 'Tiles')

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

    # Tile ID is the key in TILE_IMG, location is tuple of (x,y). x and y will be multiplied by TILE_SIZE in this
    # constructor, so x,y can be 0,1,2,3...
    def __init__(self, tile_id, location ):
        super().__init__()
        self.image = Tile.TILE_IMG[ int(tile_id) ]
        self.rect = self.image.get_rect()
        self.rect.top = location[0] * Tile.TILE_SIZE[1]
        self.rect.left = location[1] * Tile.TILE_SIZE[0]

#####################
# Tile Map Class
#####################
class TileMap(pygame.sprite.Group):
    def __init__(self, tile_map_location):
        super().__init__()

        with open(tile_map_location) as tile_map_file:
            tile_map_reader = csv.reader(tile_map_file)
            for i, row in enumerate(tile_map_reader):
                for j, tile_id in enumerate(row):
                    if tile_id != '0':
                        self.add( Tile( tile_id, (i,j) ) )
        print("Tilemap loaded successfully")

    def draw(self, surface: pygame.Surface):
        # Fill background sky color
        surface.fill( (163, 214, 255) )
        # Hills background
        pygame.draw.rect(surface, (38, 222, 129), (20, 60, 50 ,140) )
        pygame.draw.rect(surface, (32, 191, 107), (60, 40, 100, 160))
        pygame.draw.rect(surface, (14, 130, 69), (200, 80, 30, 120))
        # Call draw() method from super class to draw all Tile Spritess
        super().draw(surface)


############################
# Player class
############################
class Player(pygame.sprite.Sprite):
    GRAVITY = 0.4
    PLAYER_SIZE = (12,16)
    IMG_PATH = path.join('Assets', 'platformer', 'Player', 'p3_stand.png')

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

    # Moves the character. Check collision
    def update(self, tile_map ):
        if self.dx != 0:
            # Move while checking screen boundary
            self.rect.left += self.dx
            self.rect.left = max(0, self.rect.left)
            self.rect.right = min(self.rect.right, self.screen.get_width() )

            # Check for tile collision
            for tile in map( lambda t: t.rect, tile_map.sprites() ):
                if self.rect.colliderect( tile ):
                    # Moving right caused collision
                    if self.dx > 0:
                        self.rect.right = tile.left
                    # Moving left caused collision
                    else:
                        self.rect.left = tile.right

        # Move Vertically. Note that we do not care if character goes over the top or bottom of screen boundary
        self.rect.top += self.dy
        # Check for tile collision
        for tile in map( lambda t: t.rect, tile_map.sprites() ):
            if self.rect.colliderect( tile ):
                # Falling caused collision
                if self.dy > 0:
                    self.rect.bottom = tile.top
                    self.is_in_air = False
                # Jumping caused collision
                else:
                    self.rect.top = tile.bottom
                self.dy = 0
        # Player is affected by gravity, but terminal velocity is -10
        self.dy = min(10, self.dy + Player.GRAVITY)

    def draw(self):
        if self.dx > 0:
            self.image = self.image_right
        elif self.dx < 0:
            self.image = self.image_left
        self.screen.blit( self.image, self.rect )
###################
# End of Classes
###################
###########################################################


v_screen = pygame.Surface( (300, 200) )
pygame.display.set_caption('Tiles and Platforming Basic')


clock = pygame.time.Clock()
should_exit = False

player = Player(v_screen)
tile_map = TileMap( path.join('Assets', 'tilemap1.csv') )

while not should_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            should_exit = True
        else:
            player.move(event)

    player.update( tile_map )

    v_screen.fill( (0,0,0) )
    tile_map.draw( v_screen )
    player.draw()

    pygame.transform.scale(v_screen, screen.get_size(), screen)

    pygame.display.flip()
    clock.tick(60)



pygame.quit()
quit()