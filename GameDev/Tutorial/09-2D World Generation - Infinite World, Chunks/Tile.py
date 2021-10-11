from __future__ import annotations
import CONSTANTS as C
import pygame
import os.path as path

from Player import Player


class Tile(pygame.sprite.Sprite):
    TILE_PATHS = [
        path.join('../Assets', 'platformer', 'Tiles', 'grassCenter.png'),
        path.join('../Assets', 'platformer', 'Tiles', 'grassMid.png'),
        path.join('../Assets', 'platformer', 'Tiles', 'fence.png'),
    ]
    TILE_SPRITES = [
        pygame.transform.scale( pygame.image.load(TILE_PATHS[0]), C.TILE_SIZE).convert_alpha(),
        pygame.transform.scale(pygame.image.load(TILE_PATHS[1]), C.TILE_SIZE).convert_alpha(),
        pygame.transform.scale(pygame.image.load(TILE_PATHS[2]), C.TILE_SIZE).convert_alpha(),
    ]


    def __init__(self, tileID:int, x:int, y:int, is_collidable:bool):
        super().__init__()
        self.image = Tile.TILE_SPRITES[tileID]
        self.rect = self.image.get_rect(top=y, left=x)
        self.is_collidable = is_collidable

    def handle_horizontal_collision(self, player:Player):
        if not self.is_collidable: return
        if player.dx > 0:
            player.rect.right = self.rect.left
        else:
            player.rect.left = self.rect.right

    def handle_vertical_collision(self, player:Player):
        if not self.is_collidable: return
        if player.dy > 0:
            player.rect.bottom = self.rect.top
        else:
            player.rect.top = self.rect.bottom

    def render(self, screen:pygame.Surface, camera:tuple = (0,0) ):
        screen.blit( self.image, self.rect.move(-camera[0], -camera[1]) )
