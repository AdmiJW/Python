import pygame
pygame.init()

from StateMachine import StateMachine

screen = pygame.display.set_mode( (800,450) )
pygame.display.set_caption('State Machine')

v_screen = pygame.Surface( (400, 225) )

clock = pygame.time.Clock()

state_machine = StateMachine(screen, v_screen, clock)
state_machine.start()

pygame.quit()
quit()