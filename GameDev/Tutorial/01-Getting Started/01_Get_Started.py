import pygame

# Pygame module requires to be initialized. See https://www.pygame.org/docs/ref/pygame.html?highlight=init#pygame.init
pygame.init()


# The topmost Surface which is displayed on screen, is obtained using pygame.display.set_mode(size)
# https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode
screen = pygame.display.set_mode( (800, 450) )


# Setting the game's title. Optional
pygame.display.set_caption("1.0 - Introduction")


# Creating a pygame.time.Clock() object which will be our FPS limiter.
# https://www.pygame.org/docs/ref/time.html
clock = pygame.time.Clock()


shouldExit = False


# Game loop
while not shouldExit:
    # Basic event handling. Use pygame.event.get() to fetch all events from queue that occurred since last frame
    # https://www.pygame.org/docs/ref/event.html
    # If you didn't pygame.event.get() to clear the event queue, the event queue will eventually get filled up and
    # your OS will decide that your game is irresponsive, resulting in (Not responding) status.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            shouldExit = True
        print(event)


    # Refresh the screen. Note that using update() without arguments update the whole screen. This is inefficient.
    # https://www.pygame.org/docs/ref/display.html#pygame.display.update
    pygame.display.update()


    # Use the Clock to limit FPS to 60 FPS
    clock.tick(60)



# Exit the game and python
pygame.quit()            # Uninitialize all modules
quit()                   # Quit python