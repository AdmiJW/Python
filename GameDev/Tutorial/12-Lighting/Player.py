
import pygame
import os.path as path
import CONSTANTS as C


class Player(pygame.sprite.Sprite):
    SPRITE_PATH = path.join('../Assets', 'platformer', 'Player', 'p3_front.png')
    SPRITE = pygame.transform.smoothscale( pygame.image.load(SPRITE_PATH), C.PLAYER_SIZE )

    def __init__(self, x:int, y:int):
        self.image = Player.SPRITE
        self.rect = self.image.get_rect(left=x, top=y)
        self.velocity = pygame.Vector2(0, 0)


    def handle_event(self, event:pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.velocity.y -= 5
            elif event.key == pygame.K_s:
                self.velocity.y += 5
            elif event.key == pygame.K_a:
                self.velocity.x -= 5
            elif event.key == pygame.K_d:
                self.velocity.x += 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.velocity.y += 5
            elif event.key == pygame.K_s:
                self.velocity.y -= 5
            elif event.key == pygame.K_a:
                self.velocity.x += 5
            elif event.key == pygame.K_d:
                self.velocity.x -= 5

    def update_vertical(self, dt: int):
        self.rect.top += self.velocity.y * dt
        self.rect.top = max(0, self.rect.top)
        self.rect.bottom = min(C.SCREEN_SIZE[1], self.rect.bottom)

    def update_horizontal(self, dt: int):
        self.rect.left += self.velocity.x * dt
        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(C.SCREEN_SIZE[0], self.rect.right)

    def render(self, screen: pygame.Surface):
        screen.blit( self.image, self.rect )

