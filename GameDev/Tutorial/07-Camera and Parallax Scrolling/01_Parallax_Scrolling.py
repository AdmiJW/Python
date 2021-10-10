# Parallax scrolling is simply a visual effect where one image move at a different speed than other images.
#
# You should've experienced parallax scrolling yourself before. When driving a car down the highway, you
# should see the mountain in distance moves much more slower compared to the closer barrier of the road.
# That is exactly the effect we are aiming for.
#
# To achieve this effect, what we do is just move the images at different speed.
#   >   The one that is supposed to be distant, should move slowly
#   >   The one that is close, should move faster

import pygame
import os.path as path

pygame.init()
screen = pygame.display.set_mode( (400, 711) )

######################
# Background Class
######################
class Background(pygame.sprite.Sprite):
    PATH = path.join("../Assets", "FlappyBirb", "background.png")

    def __init__(self, screen: pygame.Surface):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load( Background.PATH ).convert()
        self.rect = self.image.get_rect()
        self.speed = 1

    def update(self, *args, **kwargs) -> None:
        self.rect.left = 0 if self.rect.left < -(self.rect.width // 2) else self.rect.left - self.speed

    def draw(self):
        self.screen.blit( self.image, self.rect )


######################
# Foreground Class
######################
class Foreground(pygame.sprite.Sprite):
    PATH = path.join("../Assets", "FlappyBirb", "ground.png")

    def __init__(self, screen: pygame.Surface):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load( Foreground.PATH ).convert()
        self.rect = self.image.get_rect()
        self.rect.bottom = self.screen.get_rect().bottom
        self.speed = 3

    def update(self, *args, **kwargs) -> None:
        self.rect.left = 0 if self.rect.left < -(self.rect.width // 2) else self.rect.left - self.speed

    def draw(self):
        self.screen.blit( self.image, self.rect )


clock = pygame.time.Clock()
should_exit = False

background = Background(screen)
foreground = Foreground(screen)

while not should_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            should_exit = True

    background.update()
    foreground.update()

    background.draw()
    foreground.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
quit()