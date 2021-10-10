
# If you had followed the tutorial until so far, you might already noticed when you change the FPS on purpose (or
# when your computer FPS drops), that the lower the FPS, the slower your character update and move!
# This is the problem if we don't apply framerate independency. Because FPS represents how many iterations of game
# loop we are going though per second, the lower the FPS, the lower the iterations done, and thus the character
# moves much, much slower.
#
# Once the framerate independence is implemented, no matter how high or low the FPS is, given the same amount of time,
# the speed of the game covered should always be the same.
#
# To implement framerate independence, the idea is as follows:
#   Say we set a desired FPS, like 60. Our character's gravity and speed is set to be suitable to the FPS of 60.
#   Now, every iteration of the game loop, we would obtain the number of seconds (or milliseconds) that had elapsed
#   since the last frame.
#
#   If the number of seconds is approximately (1/60 == 60 FPS), then its alright to move the character and update all
#   the stuff with the normal configuration - The speed we think is suitable for 60 FPS
#
#   What if the number of seconds elapsed is around (1/30 == 30FPS)? First, we could be able to calculate how many
#   times it is slower than our desired FPS of 60, by the formula:
#
#           ratio = (time elapsed in seconds) / (desired FPS in seconds) <-- If desired is 60FPS, then it is (1/60)
#
#   By performing the calculation using the above formula, we get
#           ratio = (1/30) / (1/60) == 2

#   Now, we know that by passing (1/30) seconds, around 2 of desired frame had passed. In other words, the time passed
#   is double of that we expected (1/30 seconds is double of 1/60)
#   That means, we really should move the character by two times of the set speed! Because the set speed is for (1/60)
#   seconds, yet the time passed is double.
#
# And that, is the idea of framerate independence.
#
# --------------------------------------------
# Often times, you will see methods like update(), move() will take in a parameter of dt, which exactly is what it
# means: Time elapsed since last frame.
#
# In pygame, you may easily get the time elapsed since last frame through the return value of clock.tick() method!
# Very convenient!


import pygame
import os.path as path

pygame.init()
screen = pygame.display.set_mode( (600,400) )
clock = pygame.time.Clock()

# Here, our desired framerate is 60
DESIRED_FPS = 60
# By setting DESIRED_FPS to 60, we calculate how much interval should each frame take
DESIRED_TIME_INTERVAL = 1/60


######################
# Player Class
######################
class Player(pygame.sprite.Sprite):
    GRAVITY = 0.4
    PLAYER_SIZE = (24,32)
    IMG_PATH = path.join('../Assets', 'platformer', 'Player', 'p3_stand.png')

    def __init__(self, screen: pygame.Surface):
        super().__init__()
        self.image = pygame.transform.smoothscale( pygame.image.load( Player.IMG_PATH ), Player.PLAYER_SIZE ).convert()
        self.rect = self.image.get_rect()
        self.screen = screen
        self.rect.topleft = ( 0, self.screen.get_height() // 2 )
        self.dx = 0
        self.dy = 0

    def move(self, key_event):
        if key_event.type == pygame.KEYDOWN:
            if key_event.key == pygame.K_w:
                self.dy -= 3
            elif key_event.key == pygame.K_s:
                self.dy += 3
            elif key_event.key == pygame.K_d:
                self.dx += 3
            elif key_event.key == pygame.K_a:
                self.dx -= 3
        elif key_event.type == pygame.KEYUP:
            if key_event.key == pygame.K_w:
                self.dy += 3
            elif key_event.key == pygame.K_s:
                self.dy -= 3
            elif key_event.key == pygame.K_d:
                self.dx -= 3
            elif key_event.key == pygame.K_a:
                self.dx += 3

    # Moves the character. Framerate Independence needs to be implemented
    # dt here DOES NOT mean the actual time elapsed in seconds, BUT INSTEAD is how many times the time elapsed is
    # compared to desired time. Eg: If FPS=30 and DESIRED_FPS=60, then dt=2
    def update(self, dt ):
        # Horizontal movement
        self.rect.left += self.dx * dt                  # Multiply by the ratio to always cover the correct distance
        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(self.screen.get_width(), self.rect.right)

        # Vertical movement
        self.rect.top += self.dy * dt  # Multiply by the ratio to always cover the correct distance
        self.rect.top = max(0, self.rect.top)
        self.rect.bottom = min(self.screen.get_height(), self.rect.bottom)

    def draw(self):
        self.screen.blit( self.image, self.rect )



def display_fps(screen):
    FONT = pygame.font.SysFont("Arial", 30)
    screen.blit( FONT.render(f"FPS: {clock.get_fps()}", True, (255,255,255)), (0,0))
    screen.blit( FONT.render("Press arrow up or down to adjust FPS", True, (255,255,255)), (0,40))


player = Player(screen)

# We will allow player to change their desired FPS
set_fps = DESIRED_FPS

should_exit = False
while not should_exit:
    # Calculate how many times is the elapsed time compared to our desired FPS's second
    # Note that clock.tick() return milliseconds. Remember to convert to seconds
    dt = clock.tick(set_fps) * 0.001 / DESIRED_TIME_INTERVAL

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            should_exit = True
        # Here we allow for changing FPS!
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    set_fps = min(120, set_fps + 5)
                elif event.key == pygame.K_DOWN:
                    set_fps = max(5, set_fps - 5)
            player.move(event)

    screen.fill( (0,0,0) )
    display_fps(screen)
    player.update(dt)
    player.draw()

    pygame.display.flip()


pygame.quit()
quit()
