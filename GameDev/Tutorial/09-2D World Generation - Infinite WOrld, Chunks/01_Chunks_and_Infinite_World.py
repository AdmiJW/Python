
# In Minecraft, Terraria, GTA or other similar games, the world is either theoretically 'infinite' or very, very large.
# If we simply use only previous techniques to create such a game, the game would probably lag a lot because of
# large amount of tiles we have to iterate through.
#
# Instead, we should've noticed that those games usually have concept such as "Chunks". Instead of having all the tiles
# in a list or some data structure, the tiles are stored in groups inside Chunks. They are basically a 'part'
# of the world that contains a finite number of tiles. In Minecraft, the chunk size is 16x16x256. In Terraria however,
# chunk size is unknown, but you can google for missing chunks error in terraria to get an idea for it.
#
# Now, we can store the chunks inside a 2D matrix or dictionary equivalent data structure that provides approximately
# O(1) lookup time. Given the player's coordinate, we can deduce the visible area on the player's screen and thus
# decide which chunk shall be loaded. These chunks are then retrieved from the O(1) data structure and checked for
# collision, rendered on screen etc.
# Instead of having to process every tile on the map, now we only have to process those who logically are interactable
# by the player on the screen. This greatly improves the performance of the game, and now you can have large maps!
#
# Chunk system improves both the performance and memory issue. Because we don't have to process every tile in our map
# every game loop, the performance is improved. Also the map could be so large that it couldn't fit inside our memory,
# therefore for chunks that are far away from the player, it could be unloaded from the memory and saved inside disks.


# In this example, the chunks only spans in x direction - There are no vertical component involved.


# 1 - Get left boundary of screen
# 2 - Using chunk size and floor division, deduce visible areas on screen to get chunk ID.

import sys
import pygame
import os.path as path

SCREEN_SIZE = (640, 480)
TILE_SIZE = (35, 35)
CHUNK_WIDTH = 8
DESIRED_FPS = 60


####################
# Tile class
####################
class Tile(pygame.sprite.Sprite):
    def __init__(self):






#####################
# Character class
#####################
class Player(pygame.sprite.Sprite):
    SPRITE_PATH = path.join('Assets', 'platformer', 'Player', 'p3_front.png')
    SPEED = 5
    GRAVITY = 1

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load( Player.SPRITE_PATH )
        self.image = pygame.transform.scale( self.image, (self.image.get_width() // 2, self.image.get_height() // 2) )
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect(left=0, bottom=SCREEN_SIZE[1] // 2)
        self.dx = 0
        self.dy = 0

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.dx += Player.SPEED
            elif event.key == pygame.K_a:
                self.dx -= Player.SPEED
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.dx -= Player.SPEED
            elif event.key == pygame.K_a:
                self.dx += Player.SPEED

    def update_horizontal(self, dt):
        self.rect.left += self.dx * dt

    def update_vertical(self, dt):
        self.rect.top += self.dy * dt
        self.dy = min(1, self.dy + Player.GRAVITY * dt)

    def render(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)







##################
# Game Setup
##################

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

player = Player()

##################
# Game Loop
##################
should_exit = False

while not should_exit:
    dt = round( clock.tick(DESIRED_FPS) * 0.001 * DESIRED_FPS )

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            should_exit = True
        else:
            player.handle_input(event)

    # Update
    player.update_vertical(dt)
    player.update_horizontal(dt)

    # Rendering
    screen.fill( (52, 152, 219) )
    player.render( screen )

    pygame.display.flip()

pygame.quit()
sys.exit()
