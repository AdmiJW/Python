# A flat chunk without any world generation like terraria or minecraft does.
# However, it does generate random fences tho!
from __future__ import annotations
import pygame
import random

import CONSTANTS as C
from Tile import Tile
from Player import Player


class FlatChunk(pygame.sprite.Group):
    def __init__(self, xoffset:int):
        super().__init__()

        # Underground height 4
        for y in range(C.SCREEN_SIZE[1] - C.TILE_SIZE[1] * 4, C.SCREEN_SIZE[1]+1, C.TILE_SIZE[1]):
            for x in range(xoffset, xoffset + C.TILE_SIZE[0] * C.CHUNK_WIDTH + 1, C.TILE_SIZE[0] ):
                self.add( Tile(0, x, y, False) )
        # Surface grass - Collidable
        for x in range(xoffset, xoffset + C.TILE_SIZE[0] * C.CHUNK_WIDTH + 1, C.TILE_SIZE[0]):
            self.add(Tile(1, x, C.SCREEN_SIZE[1] - C.TILE_SIZE[1] * 5, True))
        # Random fences
        for x in range(xoffset, xoffset + C.TILE_SIZE[0] * C.CHUNK_WIDTH + 1, C.TILE_SIZE[0]):
            if random.random() < 0.3:
                self.add(Tile(2, x, C.SCREEN_SIZE[1] - C.TILE_SIZE[1] * 6, False))

    def update_after_player_horizontal(self, player:Player):
        for collided_tiles in pygame.sprite.spritecollide(player, self, False):
            collided_tiles.handle_horizontal_collision(player)

    def update_after_player_vertical(self, player:Player):
        for collided_tiles in pygame.sprite.spritecollide(player, self, False):
            collided_tiles.handle_vertical_collision(player)


    def render(self, screen: pygame.Surface, camera:tuple = (0,0)):
        for tile in self.sprites():
            tile.render( screen, camera )
