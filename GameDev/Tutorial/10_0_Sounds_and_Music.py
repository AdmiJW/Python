
# Playing background music is fairly simple using pygame. Look into the pygame.mixer.music module for that purpose.
# https://www.pygame.org/docs/ref/music.html
#
# For sounds effects, things is a bit more complicated. You have to play the sound effects at the right time,
# and even the slightest lag will ruin the overall auditory experience.
#
# Sound effects in pygame is done via pygame.mixer module. Look https://www.pygame.org/docs/ref/mixer.html
#
# Tips for implementing sound effects:
#   >   Play it at the right time. Eg: The jump sound effect is played when we detected the player had jumped.
#   >   In pygame, the default number of channels is only 8. You may choose to raise it by pygame.mixer.set_num_channels
#   >   For a more complex sound effect implementation, like footsteps when the character moves, we would very well
#       use Composition (Once more) to have a PlayerAudio system to handle the complexity.
#       For example, footsteps shall be heard when the player is indeed walking on the path
#           - Non-zero horizontal velocity
#           - Not in air
#       Also, we do not want to play the sound every iteration of game loop! Surely that will annoy the hell out of the
#       player. What we need to do instead is to have a countdown timer to play the sound at interval.
#       Different tiles in which the player step on may produce different sound. This introduces the necessity to check
#       for the type of tile the player is on, and passing that information to the sound system.
#       Eg:
#           - The Player will have a property like self.ground_type, indicating the type of ground the player is
#             currently on
#           - This self.ground_type will be updated during the collision detection part of our game, and each tile
#             will probably have the information of ground type stored.


import pygame
import os.path as path
import csv

pygame.init()
screen = pygame.display.set_mode( (600, 400) )
clock = pygame.time.Clock()


#################
# Tile Class
#################
class Tile(pygame.sprite.Sprite):
    TILE_SIZE = (20, 20)
    BASE_PATH = path.join('Assets', 'platformer', 'Tiles')

    # Tile ID Mapping
    # 0 - Nothing (Background)
    # 1 - Grass middle
    # 2 - Dirt
    # 7 - Stone Top
    # 8 - Inner Stone
    TILE_IMG = {
        1: pygame.transform.scale( pygame.image.load( path.join( BASE_PATH, 'grassMid.png') ).convert_alpha(), TILE_SIZE ),
        2: pygame.transform.scale( pygame.image.load( path.join( BASE_PATH, 'grassCenter.png') ).convert_alpha(), TILE_SIZE ),
        7: pygame.transform.scale( pygame.image.load( path.join( BASE_PATH, 'castle.png') ).convert_alpha(), TILE_SIZE ),
        8: pygame.transform.scale( pygame.image.load( path.join( BASE_PATH, 'castleCenter.png') ).convert_alpha(), TILE_SIZE )
    }

    def __init__(self, tile_id, location ):
        super().__init__()
        # Tile ID is a way to store information about what type of tile it is. 1 - Grass, 7 - Stone etc
        self.tile_id = int(tile_id)
        self.image = Tile.TILE_IMG[ self.tile_id ]
        self.rect = self.image.get_rect()
        self.rect.top = location[0] * Tile.TILE_SIZE[1]
        self.rect.left = location[1] * Tile.TILE_SIZE[0]


###################
# TileMap class
##################
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
        surface.fill( (163, 214, 255) )
        pygame.draw.rect(surface, (38, 222, 129), (40, 120, 100,280) )
        pygame.draw.rect(surface, (32, 191, 107), (120, 80, 200, 320))
        pygame.draw.rect(surface, (14, 130, 69), (400, 160, 60, 240))
        super().draw(surface)


##########################
# Player Sounds class
##########################

class PlayerSound:
    JUMP_SFX = pygame.mixer.Sound( path.join("Assets", "sounds", "jump_sound.wav"))
    GRASS_SFX = pygame.mixer.Sound( path.join("Assets", "sounds", "grass_walk.wav"))
    ROCK_SFX = pygame.mixer.Sound( path.join("Assets", "sounds", "footstep.wav"))
    FOOTSTEP_INTERVAL = 5

    def __init__(self):
        self.footstep_cooldown = PlayerSound.FOOTSTEP_INTERVAL
        self.tile_id = -1

    @staticmethod
    def play_jump_sound():
        PlayerSound.JUMP_SFX.play()

    # Called whenever player is walking on ground. Pass in the type of ground into the parameter
    def update_footstep(self, tile_id):
        if self.tile_id != tile_id:
            self.tile_id = tile_id
            self.footstep_cooldown = PlayerSound.FOOTSTEP_INTERVAL
        elif self.footstep_cooldown == 0:
            self.footstep_cooldown = PlayerSound.FOOTSTEP_INTERVAL
            if self.tile_id == 1:
                PlayerSound.GRASS_SFX.play()
            elif self.tile_id == 7:
                PlayerSound.ROCK_SFX.play()
        else:
            self.footstep_cooldown -= 1

############################
# Player class
############################
class Player(pygame.sprite.Sprite):
    GRAVITY = 0.4
    PLAYER_SIZE = (24,32)
    IMG_PATH = path.join('Assets', 'platformer', 'Player', 'p3_stand.png')

    def __init__(self, screen: pygame.Surface):
        super().__init__()
        self.player_sound_player = PlayerSound()
        self.image = pygame.transform.smoothscale( pygame.image.load( Player.IMG_PATH ), Player.PLAYER_SIZE ).convert_alpha()
        self.rect = self.image.get_rect()
        self.screen = screen
        self.rect.topleft = ( 0, self.screen.get_height() // 2 )
        self.dx = 0
        self.dy = 0
        self.jumps_left = 0
        # Indicates what kind of tile the player is currently on
        self.ground_id = 0

    def move(self, key_event):
        if key_event.type == pygame.KEYDOWN:
            if key_event.key == pygame.K_w and self.jumps_left != 0:
                self.dy = -8
                self.jumps_left -= 1
                self.player_sound_player.play_jump_sound()
            elif key_event.key == pygame.K_d:
                self.dx += 3
            elif key_event.key == pygame.K_a:
                self.dx -= 3
        elif key_event.type == pygame.KEYUP:
            if key_event.key == pygame.K_a:
                self.dx += 3
            elif key_event.key == pygame.K_d:
                self.dx -= 3

    # Moves the character. Check collision
    def update(self, tile_map):
        if self.dx != 0:
            self.rect.left += self.dx
            self.rect.left = max(0, self.rect.left)
            self.rect.right = min(self.rect.right, self.screen.get_width() )

            # Check for tile collision
            for tile in tile_map.sprites():
                if self.rect.colliderect( tile.rect ):
                    if self.dx > 0:
                        self.rect.right = tile.rect.left
                    else:
                        self.rect.left = tile.rect.right

        # Move Vertically. Note that we do not care if character goes over the top or bottom of screen boundary
        self.rect.top += self.dy
        # Check for tile collision
        for tile in tile_map.sprites():
            if self.rect.colliderect( tile.rect ):
                if self.dy > 0:
                    self.rect.bottom = tile.rect.top
                    self.jumps_left = 2
                    # This is where we update the type of the tile that the player is currently on!
                    self.ground_id = tile.tile_id
                    # Now the type of tile standing is updated, let's check whether should we play footsteps?
                    if self.dx != 0:
                        self.player_sound_player.update_footstep( self.ground_id )
                else:
                    self.rect.top = tile.rect.bottom
                self.dy = 0

        self.dy = min(10, self.dy + Player.GRAVITY)

    def draw(self):
        self.screen.blit( self.image, self.rect )


###################
# Game Loop
###################
tile_map = TileMap( path.join("Assets", "tilemap3.csv") )
player = Player(screen)

# To play background music is very simple:
# Every control is inside pygame.mixer.music
# Configuration to make sound play faster (Especially by setting buffer size to 512)
pygame.mixer.pre_init(44100, -16, 2, 512)
# Set number of channels to 32 instead of default 8
pygame.mixer.set_num_channels(32)

pygame.mixer.music.load( path.join('Assets', 'musics', 'happy.wav'))
pygame.mixer.music.set_volume(0.5)
# Use loop=-1 to indicate infinite looping
pygame.mixer.music.play(-1)


should_exit = False
while not should_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            should_exit = True
        else:
            player.move(event)

    player.update(tile_map)

    tile_map.draw(screen)
    player.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
quit()