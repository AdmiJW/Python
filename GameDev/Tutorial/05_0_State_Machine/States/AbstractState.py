import pygame

# Abstract State to be inherited by all states
class AbstractState:
    def __init__(self, screen: pygame.Surface, v_screen: pygame.Surface, clock: pygame.time.Clock):
        self._screen = screen
        self._v_screen = v_screen
        self._clock = clock
        self._center = self._v_screen.get_rect().center

    def blit_to_actual_screen(self):
        self._screen.blit( pygame.transform.scale(self._v_screen, self._screen.get_size(), self._screen), (0,0) )
        pygame.display.flip()

    # Do override these methods in inherited classes!
    def handle_event(self): pass
    def update(self): pass
    def draw(self): pass
    def run(self): pass