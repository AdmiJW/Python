
# A perlin chunk. Random heights based on perlin noise.
#
# If you pass in integer arguments into the perlin noise function, you'll always get 0. Don't know why this happens,
# but it is a fact.
# Therefore (and you'll more likely do this), scale your x positions (Eg: multiply by 0.003). This way not only your
# x position is no longer an integer, the perlin noise will also get smoother (Due to scaling) and less arbitrary
from __future__ import annotations
import pygame
import random
from noise import pnoise1

import CONSTANTS as C
from Tile import Tile
from Player import Player


class PerlinChunk(pygame.sprite.Group):
    def __init__(self, xoffset:int):
        super().__init__()

        # For every x position, get perlin noise height
        for x in range(xoffset, xoffset + C.TILE_SIZE[0] * C.CHUNK_WIDTH + 1, C.TILE_SIZE[0]):
            # Remember that perlin noise returns [-1,1]. Clip to [1,9) instead
            height = int( pnoise1(x * 0.003, repeat=999999) * 4 + 5 )

            # Underground
            for y in range(C.SCREEN_SIZE[1] - C.TILE_SIZE[1] * (height-1), C.SCREEN_SIZE[1]+1, C.TILE_SIZE[1]):
                self.add( Tile(0, x, y, True) )
            # Surface grass & Collidable
            self.add( Tile(1, x, C.SCREEN_SIZE[1] - C.TILE_SIZE[1] * height, True) )
            # Random fence
            if random.random() < 0.2:
                self.add( Tile(2, x, C.SCREEN_SIZE[1] - C.TILE_SIZE[1] * (height+1), False ) )

    def update_after_player_horizontal(self, player:Player):
        for collided_tiles in pygame.sprite.spritecollide(player, self, False):
            collided_tiles.handle_horizontal_collision(player)

    def update_after_player_vertical(self, player:Player):
        for collided_tiles in pygame.sprite.spritecollide(player, self, False):
            collided_tiles.handle_vertical_collision(player)


    def render(self, screen: pygame.Surface, camera:tuple = (0,0)):
        for tile in self.sprites():
            tile.render( screen, camera )
