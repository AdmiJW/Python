import pygame
from ..AbstractState import AbstractState
from ..QuitState import Quit as QuitState
from ..GameOverState import GameOver as GameOverState

class InGame(AbstractState):
    GAME_FONT = pygame.font.SysFont('Arial', 40, bold=True)
    GAME_SUBFONT = pygame.font.SysFont('Arial', 14)

    def __init__(self, screen: pygame.Surface, v_screen: pygame.Surface, clock=pygame.time.Clock):
        super().__init__(screen, v_screen, clock)
        self._is_paused = False

        # Game Text
        self.title = InGame.GAME_FONT.render('In Game', True, (255,255,255) )
        self.title_rect = self.title.get_rect(center=self._center).move(0, -70)

        self.pause_text = InGame.GAME_FONT.render('PAUSED', True, (230, 126, 34))
        self.pause_text_rect = self.pause_text.get_rect(center=self._center)

        self.guide_1 = InGame.GAME_SUBFONT.render('Press ENTER to pause/unpause', True, (255,255,255))
        self.guide_2 = InGame.GAME_SUBFONT.render('Press SPACE to finish game', True, (255,255,255))
        self.guide_1_rect = self.guide_1.get_rect(center=self._center).move(0, 50)
        self.guide_2_rect = self.guide_2.get_rect(center=self._center).move(0, 70)


    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return QuitState.Quit(self._screen, self._v_screen, self._clock)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self._is_paused = not self._is_paused
                if event.key == pygame.K_SPACE and not self._is_paused:
                    # Return game over instead
                    return GameOverState.GameOver(self._screen, self._v_screen, self._clock)

    def draw(self):
        self._v_screen.fill( (0,0,0) )
        self._v_screen.blit( self.title, self.title_rect )

        self._v_screen.blit(self.guide_1, self.guide_1_rect)
        self._v_screen.blit(self.guide_2, self.guide_2_rect)

        if self._is_paused:
            self._v_screen.blit( self.pause_text, self.pause_text_rect )


    def run(self):
        while True:
            # Event Handling. May cause state transition to occur
            next_state = self.handle_event()
            if next_state is not None:
                return next_state

            # Rendering
            self.draw()

            self.blit_to_actual_screen()
            self._clock.tick(60)
