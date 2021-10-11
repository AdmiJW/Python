import pygame
import os.path as path

import CONSTANTS as C

#####################
# Character class
#####################
class Player(pygame.sprite.Sprite):
    SPRITE_PATH = path.join('../Assets', 'platformer', 'Player', 'p3_front.png')
    SPEED = 5
    GRAVITY = 1

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load( Player.SPRITE_PATH )
        self.image = pygame.transform.scale( self.image, (self.image.get_width() // 2, self.image.get_height() // 2) )
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect(left=0, top=0)
        self.dx = 0
        self.dy = 0

        # Since the camera is fixed onto the player, I just implement camera here
        self.camera = [0, 0]

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.dx += Player.SPEED
            elif event.key == pygame.K_a:
                self.dx -= Player.SPEED
            elif event.key == pygame.K_w:
                self.dy = -15
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.dx -= Player.SPEED
            elif event.key == pygame.K_a:
                self.dx += Player.SPEED

    def update_horizontal(self, dt):
        self.rect.left = max(0, self.rect.left + self.dx * dt)

    def update_vertical(self, dt):
        self.rect.top += self.dy * dt
        self.dy = min(10, self.dy + Player.GRAVITY * dt)

    def render(self, screen: pygame.Surface, camera:tuple = (0,0) ):
        screen.blit(self.image, self.rect.move(-camera[0], -camera[1]))

    def get_camera(self):
        targetx = max(0, self.rect.centerx - C.SCREEN_SIZE[0] // 2)
        targety = 0
        self.camera[0] += (targetx - self.camera[0]) // 15
        return *self.camera,
