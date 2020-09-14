import pygame, sys

#   Initialization ============================
pygame.init()

#   State =================================
state = {
    'FPS': 60,
    'WINDOW_WIDTH': 600,
    'WINDOW_HEIGHT': 600,
    'BACKGROUND': pygame.image.load('soccerfield.jpg'),
    'BOUNCE_SFX': pygame.mixer.Sound('ballSfx.wav')
}

#   Ball Class ==============================
class Ball(pygame.sprite.Sprite):
    def __init__(self, state):
        super().__init__()
        self.image = pygame.image.load('ball.png').convert_alpha()
        self.BALL_SIZE = 300
        self.surface = pygame.Surface( (self.BALL_SIZE, self.BALL_SIZE) )
        self.rect = self.surface.get_rect( center = (state['WINDOW_WIDTH'] // 2, \
                                                     0 + self.BALL_SIZE // 2) )
        self.gravity = 9.81 / 60

        self.vy = 0
        self.vx = 0

    #   Will displace the ball. First by increasing the y velocity by gravity value
    #   Then will check for key presses to add vx or vy
    #   Will also check if the ball has hit the wall (boundaries). If so, just negate the velocity value and reposition
    def move(self):
        self.vy += self.gravity

        buttonPress = pygame.key.get_pressed()
        if (buttonPress[ pygame.K_a] ):
            self.vx -= self.gravity
        if (buttonPress[ pygame.K_d] ):
            self.vx += self.gravity
        if (buttonPress[ pygame.K_w] ):
            self.vy -= self.gravity
        if (buttonPress[ pygame.K_s] ):
            self.vy += self.gravity

        self.rect.move_ip( (self.vx, self.vy) )

        if self.rect.bottom > state['WINDOW_HEIGHT']:
            state['BOUNCE_SFX'].play()
            self.rect.bottom = state['WINDOW_HEIGHT']
            self.vy = -self.vy
        if self.rect.top < 0:
            state['BOUNCE_SFX'].play()
            self.rect.top = 0
            self.vy = -self.vy
        if self.rect.left < 0:
            state['BOUNCE_SFX'].play()
            self.rect.left = 0
            self.vx = -self.vx
        if self.rect.right > state['WINDOW_WIDTH']:
            state['BOUNCE_SFX'].play()
            self.rect.right = state['WINDOW_WIDTH']
            self.vx = -self.vx

    #   Resets the ball
    def reset(self):
        self.__init__(state)

    def render(self, surface):
        surface.blit( self.image, self.rect)

#   A smaller ball. It extends the Ball class but has a smaller ball size (100px)
class BallSmall(Ball):
    def __init__(self, state):
        super().__init__(state)
        self.image = pygame.image.load('ballsmaller.png').convert_alpha()
        self.BALL_SIZE = 100
        self.surface = pygame.Surface((self.BALL_SIZE, self.BALL_SIZE) )
        self.rect = self.surface.get_rect(center=(state['WINDOW_WIDTH'] // 2, \
                                                  0 + self.BALL_SIZE // 2))
        self.gravity = 9.81 / 60

        self.vy = 0
        self.vx = 0




#   Window Initialization ================
DISPLAY = pygame.display.set_mode( (state['WINDOW_WIDTH'], state['WINDOW_HEIGHT'] ) )
pygame.display.set_caption("Foot ball")

#   Converts the background image
state.update({
    'BACKGROUND': state['BACKGROUND'].convert()
})

CLOCK = pygame.time.Clock()

#   Sprite Initalization ====================
ball1 = BallSmall(state)

ball_sprite = pygame.sprite.Group()
ball_sprite.add( ball1 )

#   Game Loop ==============================
while True:

    #   Logic =======================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for ball in ball_sprite:
                    ball.reset()

    for ball in ball_sprite:
        ball.move()

    #   Display ===============
    DISPLAY.fill( (255,255,255) )
    DISPLAY.blit( state['BACKGROUND'], (0,0) )

    for ball in ball_sprite:
        ball.render(DISPLAY)

    pygame.display.update()

    CLOCK.tick( state['FPS'] )