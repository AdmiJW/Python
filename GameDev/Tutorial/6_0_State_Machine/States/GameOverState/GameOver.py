import pygame
from ..AbstractState import AbstractState
from ..QuitState import Quit as QuitState
from ..MenuState import Menu as MenuState


class GameOver(AbstractState):
    LG_FONT = pygame.font.SysFont('Arial', 40, bold=True)
    SM_FONT = pygame.font.SysFont('Arial', 14)

    def __init__(self, screen: pygame.Surface, v_screen: pygame.Surface, clock: pygame.time.Clock):
        super().__init__(screen, v_screen, clock)

        self.title = GameOver.LG_FONT.render('GAME OVER', True, (255,255,255) )
        self.title_rect = self.title.get_rect(center=self._center).move(0, -40)

        self.guide = GameOver.SM_FONT.render('Press ENTER to return to main menu', True, (255, 255, 255))
        self.guide_rect = self.guide.get_rect(center=self._center).move(0, 40)


    def handle_event(self):
        for event in pygame.event.get():
            # Exit game
            if event.type == pygame.QUIT:
                return QuitState.Quit(self._screen, self._v_screen, self._clock)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return MenuState.Menu(self._screen, self._v_screen, self._clock)


    def draw(self):
        self._v_screen.fill( (0,0,0) )

        self._v_screen.blit( self.title, self.title_rect )
        self._v_screen.blit( self.guide, self.guide_rect )


    def run(self):
        while True:
            # Event Handling. May cause state transition to occur
            next_state = self.handle_event()
            if next_state is not None:
                return next_state

            # Rendering
            self.draw()

            self.blit_to_actual_screen()
            self._clock.tick(15)


