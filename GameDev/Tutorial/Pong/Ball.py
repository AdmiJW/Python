import pygame
import random

from GameDev.Tutorial.Pong.Pads.PlayerPad import PlayerPad
from GameDev.Tutorial.Pong.Pads.EnemyPad import EnemyPad

from GameDev.Tutorial.Pong.Sounds.Sounds import Sounds

class Ball(pygame.sprite.Sprite):
    BALL_SIZE = 20

    def __init__(self, state):
        super().__init__()

        self.state = state

        self.WINDOW_WIDTH = state.WINDOW_WIDTH
        self.WINDOW_HEIGHT = state.WINDOW_HEIGHT

        self.surface = pygame.Surface( (self.BALL_SIZE, self.BALL_SIZE) )
        self.rect = self.surface.get_rect( center=( self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2) )

        pygame.draw.circle( self.surface, (255,255,255), (self.BALL_SIZE // 2, self.BALL_SIZE // 2), \
                            (self.BALL_SIZE // 2 ) )

        self.dx = 5
        self.dy = 0

    def move(self, padRects):
        collideIndex = self.rect.collidelist(padRects)

        if collideIndex != -1:
            Sounds.BALLHIT.play()
            collideItem = padRects[collideIndex]
            if isinstance(collideItem, PlayerPad):
                self.rect.left = collideItem.rect.right
            elif isinstance(collideItem, EnemyPad):
                self.rect.right = collideItem.rect.left
            self.dx *= -1.05
            self.dy = random.randint(-3, 3)

        if (self.rect.top < 0):
            self.rect.top = 0
            self.dy *= -1
            Sounds.BALLHIT.play()
        elif (self.rect.bottom > self.WINDOW_HEIGHT ):
            self.rect.bottom = self.WINDOW_HEIGHT
            self.dy *= -1
            Sounds.BALLHIT.play()

        if (self.rect.left <= 0):
            Sounds.BALLSCORE.play()
            self.dx = 5
            self.dy = 0
            self.rect.center = ( self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2)
            self.state.Score2 += 1
            self.state.PendingUpdateScore = True
        elif (self.rect.right >= self.WINDOW_WIDTH ):
            Sounds.BALLSCORE.play()
            self.dx = -5
            self.dy = 0
            self.rect.center = (self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2)
            self.state.Score1 += 1
            self.state.PendingUpdateScore = True



        self.rect.move_ip( (self.dx, self.dy) )

    def reset(self):
        self.rect.center = ( self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2)


    def render(self, surface):
        surface.blit( self.surface, self.rect )