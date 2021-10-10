import pygame
import States.MenuState.Menu as MenuState

# Top level State Machine responsible for whole game
class StateMachine:
    def __init__(self, screen: pygame.Surface, v_screen: pygame.Surface, clock: pygame.time.Clock):
        self._screen = screen
        self._v_screen = v_screen
        self._clock = clock
        self._state = MenuState.Menu(screen, v_screen, clock)

    def start(self):
        while True:
            next_state = self._state.run()
            if next_state is not None:
                self._state = next_state
            else:
                return
