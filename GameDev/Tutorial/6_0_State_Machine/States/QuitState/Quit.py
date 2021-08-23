import pygame
from ..AbstractState import AbstractState

# Simple State which quits the game when run()
class Quit(AbstractState):
    def __init__(self, screen: pygame.Surface, v_screen: pygame.Surface, clock: pygame.time.Clock):
        pass

    def run(self):
        pygame.quit()
        quit()
