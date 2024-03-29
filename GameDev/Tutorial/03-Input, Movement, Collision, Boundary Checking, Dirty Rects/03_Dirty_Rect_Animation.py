import pygame
import os.path as path

##############################################################################################################
# If we use update() or flip(), every frame the whole window is refreshed. This may be inefficient especially
# if the screen size is large. Instead, we use the concept of "Dirty Rect", which we will only update specific
# areas that need to be updated.
#
# This technique is useful when not much on the screen has changed. For example, when the game is paused, or when
# the game is in Main Menu.
#
# However, on games where there is a "camera" that follows the character, the whole map essentially needs to be
# updated frequently, and given such, this technique is not really applicable. To speed things up in this case,
# remember to convert each of the images into pixel format using .convert()!
#
####################################
# Cat Class
class Cat:
    IMG_PATH = path.join('../Assets', 'cat_avatar', 'cat_a1.gif')

    def __init__(self, screen):
        self._screen = screen

        # Now we have left facing and right facing Cat!
        self._sprite_face_right = pygame.image.load(Cat.IMG_PATH)
        self._sprite_face_right.set_colorkey( (0, 114, 188) )
        self._sprite_face_right = self._sprite_face_right.convert_alpha()
        self._sprite_face_right = pygame.transform.scale( self._sprite_face_right, (150, 150) )
        self._sprite_face_left = pygame.transform.flip( self._sprite_face_right, True, False)

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


    def update(self, dirty_rects):
        # Obtain the rectangle BEFORE new location
        dirty_rect = pygame.Rect( (self.x, self.y), (self.width, self.height) )

        self.x += self.dx
        self.y += self.dy
        self.x = max(0, min( self._screen.get_width() - self._sprite.get_width(), self.x) )
        self.y = max(0, min(self._screen.get_height() - self._sprite.get_height(), self.y) )


        # Remove old sprite and blit the sprite on new location
        self._screen.fill((0,0,0), dirty_rect)
        self._screen.blit(self._sprite, (self.x, self.y))

        # Union the dirty rect with new location
        dirty_rect = dirty_rect.union( pygame.Rect( (self.x, self.y), (self.width, self.height) ) )
        # Append the dirty rectangle onto the dirty_rects list
        dirty_rects.append(dirty_rect)

##########################################
# End of Class Cat



pygame.init()

screen = pygame.display.set_mode( (800, 450) )
pygame.display.set_caption('Meow')

clock = pygame.time.Clock()
should_exit = False


cat = Cat(screen)
screen.fill( (0,0,0) )
pygame.display.update()

while not should_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            should_exit = True
        elif event.type == pygame.KEYDOWN:
            cat.key_pressed(event)
        elif event.type == pygame.KEYUP:
            cat.key_released(event)

    # Dirty Rect animation. We'll make a list of dirty_rect
    dirty_rects = []
    cat.update( dirty_rects )
    pygame.display.update( dirty_rects )

    clock.tick(30)


pygame.quit()
quit()