# If you had played with photoshop or related graphical editing software before, you should've noticed about
# BLENDING MODES. If you don't know about it, it is essentially determining how the layer on top of another layer,
# should 'blend' with the colors of layer below it, instead of 100% covering up the layer below it.
#
# For example, the ADD blending mode will, as the name implies, add to the rgb value of the layer below it.
# Let's say the base layer is color rgb(10,10,10), and the blending layer is covered with rgb(20,20,20). In the
# end when they are blended, the final color is rgb(30,30,30) - Brighter!
# BTW, the opposite is true for the SUBTRACT blending mode.
#
# Using these blending modes, we can apply awesome visual effects like lighting, shadow, glow, or even introduce
# a whole new gameplay mechanics into our game (Like dark room with a torchlight to see, or field of visions / line
# of sight).


import pygame
import os.path as path

SCREEN_SIZE = (960, 486)
DESIRED_FPS = 60

pygame.init()
screen = pygame.display.set_mode( SCREEN_SIZE )
clock = pygame.time.Clock()


# Background image:
background = pygame.image.load( path.join('../Assets', 'living_room.jpg') )
background = pygame.transform.scale(background, SCREEN_SIZE)
background = background.convert_alpha()

# Darkening Layer:
darken_base_layer = pygame.Surface( SCREEN_SIZE )
darken_base_layer.fill( (240,240,240) )

# Torchlight:
torchlight = pygame.Surface( (400, 400) )
# Here I will draw circles of different radius, up to maximum size of torchlight surface to produce an light diffusion
# effect
for radius in range(200, 9, -5):
    brightness = 210 - radius
    pygame.draw.circle(torchlight, (brightness,brightness,brightness), (200, 200), radius)
torchlight.set_colorkey( (0,0,0) )


arial = pygame.font.SysFont('Arial', 30)
prompt = arial.render('Press ENTER to switch day/night', True, (255,0,0))
prompt_rect = prompt.get_rect( bottom=SCREEN_SIZE[1], centerx=screen.get_rect().centerx )


should_exit = False
is_torchlight_on = False

while not should_exit:
    dt = clock.tick(DESIRED_FPS) * 0.001 * DESIRED_FPS

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            should_exit = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            is_torchlight_on = not is_torchlight_on

    # Rendering
    # Instead of blitting darken layer with blend mode on background then the torchlight, I will blend the darken
    # layer with the torchlight layer first.
    # This is because blending background with darken will lose some information, which in the end doesn't look good
    # when lightened back up with torchlight layer.
    # Instead, copy the darken layer, apply torchlight layer to it, then only apply the modified layer to background
    screen.blit( background, (0,0) )
    if is_torchlight_on:
        darken = darken_base_layer.copy()
        darken.blit( torchlight, torchlight.get_rect(
            center=pygame.mouse.get_pos()
        ), special_flags=pygame.BLEND_SUB )
        screen.blit( darken, (0,0), special_flags=pygame.BLEND_SUB )
    screen.blit(prompt, prompt_rect)

    pygame.display.flip()
