
# if you don't know already, a game itself can already be considered an animation! An animation can be thought as simply
# a collection of similar images "flipped" quickly, to create an illusion of movement.
#
# In previous platforming examples, we see that the character is able to move, but yet no animation is applied to it.
# Therefore, we will implement animations to our character to make it look much more alive!
#
# Animation is a series of images. Therefore, we could put all of the data inside of our Player class, or even abstract
# it into composition where Player will contain a PlayerAnimation which provides methods like set_action() and
# get_image().
#
# There are some key points to animating a character or object:
#   >   Loading the series of images and storing them in order
#   >   Setting Actions, like "Run", "Idle", "Jump"
#   >   Current state/frame of the action, like "Run_0", "Run_1", "Run_2"... and looping back

import pygame
import os.path as path
import itertools       # Using itertools.cycle to get cyclic iterator

pygame.init()
screen = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()

##################################################################
# PlayerAnimator class responsible for Player's image animation
##################################################################
class PlayerAnimator:
    BASE_PATH = path.join("Assets", "Little_boy", "Transparent PNG")
    TRANSITION_EVERY_N_FRAME = 2

    @staticmethod
    def _load_imgset(action_name, count, player_size):
        # List of paths
        img_set = [ path.join(PlayerAnimator.BASE_PATH, action_name, f'skeleton-{action_name}_{i}.png') for i in range(count)]
        # Load images
        img_set = [ pygame.image.load(img_path) for img_path in img_set ]
        # Scale and convert
        img_set = [ pygame.transform.smoothscale( img.convert_alpha(), player_size ) for img in img_set ]
        return img_set

    def __init__(self, player_size):
        # Load in Idle images
        self._idle_imgset = PlayerAnimator._load_imgset('idle', 21, player_size)
        self._jump_imgset = PlayerAnimator._load_imgset('jump', 11, player_size)
        self._run_imgset = PlayerAnimator._load_imgset('run', 21, player_size)
        self._curr_action = 'idle'
        self._frame = 0
        self._iterator = itertools.cycle(self._idle_imgset)
        self._curr_image = next( self._iterator )
        self._is_flip = False

    def set_action(self, action, is_flip=None):
        if is_flip is not None:
            self._is_flip = is_flip

        if self._curr_action != action:
            self._curr_action = action
            self._frame = 0
            if action == 'idle':
                self._iterator = itertools.cycle(self._idle_imgset)
            elif action == 'jump':
                self._iterator = itertools.cycle(self._jump_imgset)
            else:
                self._iterator = itertools.cycle(self._run_imgset)

    def get_image(self):
        if self._frame >= PlayerAnimator.TRANSITION_EVERY_N_FRAME:
            self._curr_image = next( self._iterator )
            self._frame = 0
        self._frame += 1

        return pygame.transform.flip(self._curr_image, self._is_flip, False)


################################
# Player class
################################
class Player(pygame.sprite.Sprite):
    GRAVITY = 0.3
    PLAYER_SIZE = (50, 83)

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.player_animator = PlayerAnimator( Player.PLAYER_SIZE )
        self.image = self.player_animator.get_image()
        self.rect = self.image.get_rect()
        self.is_in_air = True
        self.dx = 0
        self.dy = 0

    def move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.dx -= 5
            elif event.key == pygame.K_d:
                self.dx += 5
            elif event.key == pygame.K_w and not self.is_in_air:
                self.dy = -10
                self.is_in_air = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.dx += 5
            elif event.key == pygame.K_d:
                self.dx -= 5

    # Moves character, update animation image, boundary check
    def update(self):
        # X Component
        self.rect.left += self.dx
        self.rect.left = max(0,self.rect.left)
        self.rect.right = min(self.screen.get_width(), self.rect.right)

        # Y Component
        self.rect.top += self.dy
        # Player is on ground.
        if self.rect.bottom >= self.screen.get_height():
            self.rect.bottom = self.screen.get_height()
            self.is_in_air = False

        # Update Action
        if self.is_in_air:
            self.player_animator.set_action('jump', None if self.dx == 0 else self.dx < 0)
        else:
            self.player_animator.set_action('idle' if self.dx == 0 else 'run', None if self.dx == 0 else self.dx < 0)

        # Update image
        self.image = self.player_animator.get_image()

        # Gravity
        self.dy += Player.GRAVITY

    def draw(self):
        self.screen.blit( self.image, self.rect )




player = Player( screen )

should_exit = False
while not should_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            should_exit = True
        else:
            player.move(event)

    player.update()

    screen.fill( (255,255,255) )
    player.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
quit()