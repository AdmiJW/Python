import pygame
from ..AbstractState import AbstractState
from ..QuitState import Quit as QuitState
from ..InGameState import InGame as InGameState


class SplashScreen(AbstractState):
    SCREEN_FONT = pygame.font.SysFont('Arial', 30, bold=True)

    def __init__(self, screen: pygame.Surface, v_screen: pygame.Surface, clock: pygame.time.Clock):
        super().__init__(screen, v_screen, clock)
        self._countdown = 4

        self.title = SplashScreen.SCREEN_FONT.render('Game Starting', True, (255,255,255) )
        self.title_rect = self.title.get_rect(center=self._center).move(0, -40)

        # Updated in update() method
        self.countdown_text = None
        self.countdown_text_rect = None

    def handle_event(self):
        for event in pygame.event.get():
            # Exit game
            if event.type == pygame.QUIT:
                return QuitState.Quit(self._screen, self._v_screen, self._clock)

    def update(self):
        self._countdown -= 1

        if self._countdown == 0:
            return InGameState.InGame( self._screen, self._v_screen, self._clock )

        self.countdown_text = SplashScreen.SCREEN_FONT.render( str(self._countdown), True, (255, 255, 255))
        self.countdown_text_rect = self.countdown_text.get_rect(center=self._center).move(0, 30)


    def draw(self):
        self._v_screen.fill( (0,0,0) )

        self._v_screen.blit( self.title, self.title_rect )
        self._v_screen.blit( self.countdown_text, self.countdown_text_rect )


    def run(self):
        while True:
            # Event Handling. May cause state transition to occur
            next_state = self.handle_event()
            if next_state is not None:
                return next_state

            # Update. May cause state transition to occur
            next_state = self.update()
            if next_state is not None:
                return next_state

            # Rendering
            self.draw()

            self.blit_to_actual_screen()
            self._clock.tick(1)


