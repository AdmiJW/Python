
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

import CONSTANTS as C

##################
# Game Setup
##################

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(C.SCREEN_SIZE)


from Player import Player
from FlatChunk import FlatChunk


###########################
# Chunk Management System
###########################
#
# In your implementation, as you walk you may see the chunks being generated from emptyness. If you don't want this
# type of effect, simply extend the boundary for chunk generation in update_chunk_in_range() method to generate
# 1 or 2 more chunks that are out of screen.
class ChunkSystem:
    CHUNK_WIDTH_PX = C.CHUNK_WIDTH * C.TILE_SIZE[0]

    def __init__(self):
        self.chunks = dict()
        self.chunk_in_range = []

    def update_chunk_in_range(self, camera:tuple):
        self.chunk_in_range.clear()

        left_edge = camera[0]
        right_edge = left_edge + C.SCREEN_SIZE[0]
        for left in range(left_edge - ChunkSystem.CHUNK_WIDTH_PX, right_edge + ChunkSystem.CHUNK_WIDTH_PX,
                          ChunkSystem.CHUNK_WIDTH_PX):
            id = left // (C.CHUNK_WIDTH * C.TILE_SIZE[0])

            # Chunk not seen before. Generate a new one
            if id not in self.chunks:
                self.chunks[id] = FlatChunk(left)
            self.chunk_in_range.append( self.chunks[id] )

    def update_after_player_horizontal(self, player:Player):
        for chunk in self.chunk_in_range:
            chunk.update_after_player_horizontal(player)

    def update_after_player_vertical(self, player:Player):
        for chunk in self.chunk_in_range:
            chunk.update_after_player_vertical(player)

    def render(self, screen:pygame.Surface, camera:tuple):
        for chunk in self.chunk_in_range:
            chunk.render(screen, camera)


player = Player()
chunk_sys = ChunkSystem()

##################
# Game Loop
##################
should_exit = False

while not should_exit:
    dt = round( clock.tick(C.DESIRED_FPS) * 0.001 * C.DESIRED_FPS )

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            should_exit = True
        else:
            player.handle_input(event)

    camera = player.get_camera()

    # Update
    chunk_sys.update_chunk_in_range(camera)
    player.update_vertical(dt)
    chunk_sys.update_after_player_vertical(player)
    player.update_horizontal(dt)
    chunk_sys.update_after_player_horizontal(player)

    # Rendering
    screen.fill( (138, 253, 255) )

    chunk_sys.render(screen, camera)
    player.render( screen, camera )

    pygame.display.flip()

pygame.quit()
sys.exit()
