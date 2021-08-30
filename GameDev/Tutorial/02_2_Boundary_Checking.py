# Boundary checking is to check if an image had moved beyond the visible area of the screen, and what
# should be done in case that happens. Does it result in game over? or simply act like a wall that object can't pass?
#
# To implement such behavior in our game, we would check the boundaries of the rectangle of our character with the
# boundaries of the screen. Once we detect that the character is going out of the boundary of the screen, we would
# adjust the character's position to be just right at the edge of the screen, not going out.
#

import pygame
import os.path as path

####################################
# Cat Class
class Cat:
    IMG_PATH = path.join('Assets', 'cat_avatar', 'cat_a1.gif')

    def __init__(self, screen):
        self._screen = screen

        # Now we have left facing and right facing Cat!
        self._sprite_face_right = pygame.image.load(Cat.IMG_PATH)
        self._sprite_face_right.set_colorkey( (0, 114, 188) )
        self._sprite_face_right = self._sprite_face_right.convert_alpha()
        self._sprite_face_right = pygame.transform.scale( self._sprite_face_right, (150, 150) )
        self._sprite_face_left = pygame.transform.flip( self._sprite_face_right, True, False)

        self._sprite = self._sprite_face_right

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

        # Sprite Change direction
        if self.dx > 0:
            self._sprite = self._sprite_face_right
        elif self.dx < 0:
            self._sprite = self._sprite_face_left


    def key_released(self, key_event):
        if key_event.key == pygame.K_a:
            self.dx += 5
        elif key_event.key == pygame.K_d:
            self.dx -= 5
        elif key_event.key == pygame.K_w:
            self.dy += 5
        elif key_event.key == pygame.K_s:
            self.dy -= 5

        # Sprite Change direction
        if self.dx > 0:
            self._sprite = self._sprite_face_right
        elif self.dx < 0:
            self._sprite = self._sprite_face_left


    def update(self):
        self.x += self.dx
        self.y += self.dy
        # Boundary checking done here. If exceeds screen width, fix it back
        self.x = max(0, min( self._screen.get_width() - self._sprite.get_width(), self.x) )
        self.y = max(0, min(self._screen.get_height() - self._sprite.get_height(), self.y) )

        # Some experience improvement: Now cat seem obvious to facing left or right
        self._screen.blit(self._sprite, (self.x, self.y))

##########################################
# End of Class Cat



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
