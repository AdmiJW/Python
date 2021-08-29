import pygame
import os.path as path


#################################################################################################
# IT IS ALWAYS a good idea to use OOP in game development, representing every entity as an object
# What you should really do is to use modularization, where Cat class is in different .py script
#################################################################################################
class Cat:
    IMG_PATH = path.join('Assets', 'cat_avatar', 'cat_a1.gif')

    def __init__(self, screen):
        self._screen = screen

        self._sprite = pygame.image.load(Cat.IMG_PATH)
        self._sprite.set_colorkey((0, 114, 188))
        self._sprite.convert_alpha()
        self._sprite = pygame.transform.scale(self._sprite, (150, 150))

        self.x = self._screen.get_rect().centerx - self._sprite.get_rect().width // 2
        self.y = self._screen.get_rect().centery - self._sprite.get_rect().height // 2
        self.dx = 0
        self.dy = 0

    def key_pressed(self, key_event):
        if key_event.key == pygame.K_a:
            self.dx -= 5
        elif key_event.key == pygame.K_d:
            self.dx += 5
        elif key_event.key == pygame.K_w:
            self.dy -= 5
        elif key_event.key == pygame.K_s:
            self.dy += 5


    def key_released(self, key_event):
        if key_event.key == pygame.K_a:
            self.dx += 5
        elif key_event.key == pygame.K_d:
            self.dx -= 5
        elif key_event.key == pygame.K_w:
            self.dy += 5
        elif key_event.key == pygame.K_s:
            self.dy -= 5

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self._screen.blit(self._sprite, (self.x, self.y))
#############################################################################
# END OF Cat Class


pygame.init()

screen = pygame.display.set_mode( (800, 450) )
pygame.display.set_caption("Meow")

clock = pygame.time.Clock()

should_exit = False

cat = Cat(screen)

while not should_exit:
    # Logic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            should_exit = True
        elif event.type == pygame.KEYDOWN:
            cat.key_pressed( event )
        elif event.type == pygame.KEYUP:
            cat.key_released( event )

    # Update
    screen.fill( (0,0,0) )
    cat.update()
    pygame.display.flip()

    # FPS
    clock.tick(30)

pygame.quit()
quit()