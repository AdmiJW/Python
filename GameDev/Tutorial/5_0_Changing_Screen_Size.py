import pygame
import itertools
import os.path as path

pygame.init()


# # What we can do to change screen size without affecting the game coordinates, is to blit all our entities onto a
# # "Virtual" screen, then only upsize to fit the screen
# # However, this would mean we need to resize on each frame, and applying the concept of dirty rects suddenly become
# # harder to implement due to difference in Virtual screen and actual screen.
#
# # Another method is to dynamically determine the current screen size and blit accordingly on all entities, kind of
# like creating a CSS media query for all the entities.
# This would be tiresome to implement, but is much faster.

###########################
# Cat class
###########################
class Cat(pygame.sprite.Sprite):
    IMG_PATH = path.join('Assets', 'cat_avatar', 'cat_a1.gif')

    def __init__(self, screen):
        self._screen = screen

        self._sprite_face_right = pygame.image.load(Cat.IMG_PATH)
        self._sprite_face_right.set_colorkey((0, 114, 188))
        self._sprite_face_right = self._sprite_face_right.convert_alpha()
        self._sprite_face_right = pygame.transform.scale(self._sprite_face_right, (75, 75))
        self._sprite_face_left = pygame.transform.flip(self._sprite_face_right, True, False)

        self._sprite = self._sprite_face_right

        self.width = self._sprite.get_width()
        self.height = self._sprite.get_height()

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
        self.x = max(0, min(self._screen.get_width() - self._sprite.get_width(), self.x))
        self.y = max(0, min(self._screen.get_height() - self._sprite.get_height(), self.y))

        self._screen.blit(self._sprite, (self.x, self.y))


###########################
# Screen sizes
###########################
SCREEN_SIZES = ( (200, 400), (280, 560), (450, 800) )
VSCREEN_SIZE = (240, 480)
# Use a cycle iterator to loop through the screen sizes
screen_size_cycle_iterator = itertools.cycle(SCREEN_SIZES)


screen = pygame.display.set_mode( next(screen_size_cycle_iterator) )
pygame.display.set_caption('Resizing')

clock = pygame.time.Clock()
should_exit = False

##################################################
# Virtual Surface which size is always consistent
#################################################
v_screen = pygame.Surface( VSCREEN_SIZE )


cat = Cat(v_screen)


while not should_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            should_exit = True
        elif event.type == pygame.KEYDOWN:
            # When user press ENTER key, that's when we change the screen size
            if event.key == pygame.K_RETURN:
                screen = pygame.display.set_mode( next(screen_size_cycle_iterator) )
            else:
                cat.key_pressed(event)
        elif event.type == pygame.KEYUP:
            cat.key_released(event)

    v_screen.fill((0,0,0))
    cat.update()

    # Blitting the virtual screen onto the real screen
    screen.blit( pygame.transform.scale( v_screen, screen.get_size() ), (0,0) )

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
quit()