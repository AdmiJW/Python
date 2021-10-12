
import pygame
import os.path as path
import csv

import CONSTANTS as C

from Player import Player


class Tile(pygame.sprite.Sprite):
    BASE_PATH = path.join('../Assets', 'platformer', 'tiles')
    TILE_PATH = [
        path.join( BASE_PATH, 'brickWall.png' ),
        path.join( BASE_PATH, 'castleCenter.png' )
    ]
    TILE_SPRITE = [
        pygame.transform.scale( pygame.image.load(TILE_PATH[0]), C.TILE_SIZE ).convert_alpha(),
        pygame.transform.scale(pygame.image.load(TILE_PATH[1]), C.TILE_SIZE).convert_alpha(),
    ]


    def __init__(self, tileID:int, x:int, y:int, is_collidable:bool):
        super().__init__()
        self.tileID = tileID
        self.image = Tile.TILE_SPRITE[tileID]
        self.rect = self.image.get_rect(left=x, top=y)
        self.is_collidable = is_collidable

    def handle_vertical_collision(self, player: Player):
        if not self.is_collidable: return
        if player.velocity.y > 0:
            player.rect.bottom = self.rect.top
        else:
            player.rect.top = self.rect.bottom

    def handle_horizontal_collision(self, player: Player):
        if not self.is_collidable: return
        if player.velocity.x > 0:
            player.rect.right = self.rect.left
        else:
            player.rect.left = self.rect.right


    def render(self, screen:pygame.Surface):
        screen.blit( self.image, self.rect )



class TileGroup( pygame.sprite.Group ):
    MAP_PATH = path.join('../Assets', 'dungeon.csv')

    def __init__(self):
        super().__init__()
        self.grid = [ [None] * C.MAP_SIZE[0] for r in range(C.MAP_SIZE[1]) ]

        with open(TileGroup.MAP_PATH) as tilemap:
            for r, row in enumerate( csv.reader(tilemap) ):
                for c, tileID in enumerate( row ):
                    tileID = int(tileID)
                    self.grid[r][c] = Tile(tileID, c * C.TILE_SIZE[0], r * C.TILE_SIZE[1], tileID == 0 )
                    self.add( self.grid[r][c] )


    def update_vertical(self, player: Player):
        for collided_sprite in pygame.sprite.spritecollide(player, self, False):
            collided_sprite.handle_vertical_collision(player)


    def update_horizontal(self, player: Player):
        for collided_sprite in pygame.sprite.spritecollide(player, self, False):
            collided_sprite.handle_horizontal_collision(player)


    def render(self, screen: pygame.Surface):
        for sprite in self.sprites():
            sprite.render( screen )
