import pygame


class Pad(pygame.sprite.Sprite):
    WIDTH = 10
    HEIGHT = 50

    def __init__(self, state):
        super().__init__()

        self.WINDOW_WIDTH = state.WINDOW_WIDTH
        self.WINDOW_HEIGHT = state.WINDOW_HEIGHT

        self.surface = pygame.Surface( (self.WIDTH, self.HEIGHT) )
        self.surface.fill( (255,255,255) )


    def reset(self):
        self.__init__(self.state)

    def render(self, surface):
        surface.blit( self.surface, self.rect )



