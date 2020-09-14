import pygame
from Tutorial.Pong.Pads.Pad import Pad

class PlayerPad(Pad):
    def __init__(self, state):
        super().__init__(state)

        self.rect = self.surface.get_rect( center=( 50, self.WINDOW_HEIGHT // 2 ) )

    def move(self):
        buttonpress = pygame.key.get_pressed()

        if buttonpress[pygame.K_w]:
            self.rect.move_ip( (0, -5) )
        if buttonpress[pygame.K_s]:
            self.rect.move_ip( (0, 5) )

        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > self.WINDOW_HEIGHT:
            self.rect.bottom = self.WINDOW_HEIGHT