
# To have peaks and troughs in our map generation algorithm, we will be commonly use 'Perlin Noise'
# 'Perlin noise' is more commonly used in places you might not think of: World generation, Movies, Realistic textures,
# etc
#
# The idea behind Perlin noise is that it is smooth randomness. You give it a coordinate of x (for 1D perlin noise)
# or x,y (for 2D perlin noise), and it will return to you a number in range [-1,1].
# However, the difference between using pure psuedorandom algorithm with using Perlin noise is that Perlin noise is
# smooth. You won't suddenly get transitioned from low value to high value suddenly when using Perlin noise, which
# is what world generation is all about!



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
from PerlinChunk import PerlinChunk


###########################
# Chunk Management System
###########################
# The very same chunk system used in 01_Chunks_and_Infinite_World.py. However this time the chunk used is not
# FlatChunk but PerlinChunk - Random, but smooth heights
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
            # More information on perlin chunk generation in PerlinChunk.py
            if id not in self.chunks:
                self.chunks[id] = PerlinChunk(left)
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
