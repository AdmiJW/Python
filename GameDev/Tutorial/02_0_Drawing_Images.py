import pygame
import os.path as path

pygame.init()

screen = pygame.display.set_mode( (800, 450) )
pygame.display.set_caption("Meow")

clock = pygame.time.Clock()

should_exit = False


# Demonstration on how the image is loaded, here:
cat_sprite = pygame.image.load(path.join('../Assets', 'cat_avatar', 'cat_a1.gif'))
# Set the color key, which all pixels with this color is transparent
cat_sprite.set_colorkey( (0, 114, 188) )
# Convert it to pixel format for faster blitting
cat_sprite = cat_sprite.convert_alpha()
# Use pygame.transform to perform transformtions on Surfaces
cat_sprite = pygame.transform.scale( cat_sprite, (300,300) )

while not should_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            should_exit = True

        print(event)

    # Every FPS, we will paint the whole screen with color black. Using fill(), it takes color in RGB tuple
    screen.fill( (0,0,0) )
    # Now we draw the cat into the center of screen. First get the center coordinates.
    center_x = screen.get_rect().centerx - cat_sprite.get_rect().width // 2
    center_y = screen.get_rect().centery - cat_sprite.get_rect().height // 2

    screen.blit( cat_sprite, (center_x, center_y) )

    # Don't forget to update the screen. flip() is like update() but only option is to update whole screen
    pygame.display.flip()

    clock.tick(30)

pygame.quit()
quit()