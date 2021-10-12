import pygame
from collections import deque

import CONSTANTS as C
from Player import Player
from Tile import TileGroup


class LightingLayer:
    def __init__(self):
        self.base = pygame.Surface(C.SCREEN_SIZE)
        self.base.fill( (C.DIM_LEVEL,) * 3 )

        self.lighting_layer = self.base.copy()

    # The core algorithm for lighting mechanism - Breadth First Search (Graph / Grid)
    # 1. Get copy of darkening layer
    # 2. Get light emitting source - The player position (as grid)
    # 3. Perform BFS. Light should be dimmer the further away from the source. Use a visited set to record recorded
    #    grids. Lighten the darkening layer using SUB blend mode
    def update_lighting(self, player: Player, tilegroup: TileGroup):
        self.lighting_layer = self.base.copy()

        r,c = self.get_player_grid_pos(player)
        # Queue item (r, c, layer)
        queue = deque()
        queue.append( (r, c, 0) )
        # Visited grids containing (r,c). Ensure no Revisiting
        visited = set( (r,c) )

        while len(queue):
            r, c, layer = queue.popleft()

            brightness = (200 - (15 * layer), 200 - (15 * layer),  0 )

            # Add a block of 'lightening' to the lighting layer
            block = pygame.Surface(C.TILE_SIZE)
            block.fill(brightness)
            self.lighting_layer.blit( block, (c * C.TILE_SIZE[0],r * C.TILE_SIZE[1]), special_flags=pygame.BLEND_SUB )

            # This grid is a wall or it's already layer 8. Stop.
            if tilegroup.grid[r][c].tileID == 0 or layer == 12: continue
            # Above
            if r - 1 >= 0 and (r-1, c) not in visited:
                visited.add( (r-1, c) )
                queue.append( (r-1, c, layer+1) )
            # Below
            if r + 1 < C.MAP_SIZE[1] and (r+1, c) not in visited:
                visited.add( (r+1, c) )
                queue.append( (r+1, c, layer+1) )
            # Left
            if c - 1 >= 0 and (r, c-1) not in visited:
                visited.add( (r, c-1) )
                queue.append( (r, c-1, layer+1) )
            # Right
            if c + 1 < C.MAP_SIZE[0] and (r,c+1) not in visited:
                visited.add( (r, c+1) )
                queue.append( (r, c+1, layer+1) )


    def get_player_grid_pos(self, player: Player):
        return (
            player.rect.centery // C.TILE_SIZE[1],
            player.rect.centerx // C.TILE_SIZE[0]
        )


    def render(self, screen: pygame.Surface):
        screen.blit( self.lighting_layer, (0,0), special_flags=pygame.BLEND_SUB )