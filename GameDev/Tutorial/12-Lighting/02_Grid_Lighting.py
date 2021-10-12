
# Say we are developing a dungeon game, where the character is holding a torch and is only able to view until a
# certain radius. How do we do that?
#
# Using previous knowledge in Basic_Lighting.py, we can make the map dark by blending it with a darken layer! However,
# this time, the light diffusion has to depend on these:
#   > We are using Grid system. The lighting should be grid based
#   > The lighting should not pass through the walls.
#
# Therefore, we would use some knowledge of algorithms - Breadth First Search. Starting from the player as emitting
# light source, we would go out layer by layer, until we've reached certain radius where the light shouldn't be able
# to shine

import sys
import pygame

import CONSTANTS as C


pygame.init()
screen = pygame.display.set_mode(C.SCREEN_SIZE)
clock = pygame.time.Clock()

from Tile import TileGroup
from Player import Player
from LightingLayer import LightingLayer


map = TileGroup()
player = Player( 60, 720 )
lighting = LightingLayer()


should_exit = False
while not should_exit:
    dt = round( clock.tick(C.DESIRED_FPS) * 0.001 * C.DESIRED_FPS )

    # Event Handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            should_exit = True
        else:
            player.handle_event(event)

    # Update
    player.update_vertical(dt)
    map.update_vertical(player)
    player.update_horizontal(dt)
    map.update_horizontal(player)

    lighting.update_lighting(player, map)

    # Render
    map.render(screen)
    player.render(screen)
    lighting.render(screen)

    pygame.display.flip()


pygame.quit()
sys.exit()


