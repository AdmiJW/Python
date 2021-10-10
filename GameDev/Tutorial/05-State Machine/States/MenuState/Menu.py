import pygame
from ..AbstractState import AbstractState
from ..QuitState import Quit as QuitState
from ..SplashScreenState import SplashScreen as SplashScreenState


class Menu(AbstractState):
    MENU_TITLE_FONT = pygame.font.SysFont('Arial', 60, bold=True)
    MENU_SUB_FONT = pygame.font.SysFont('Arial', 20)

    def __init__(self, screen: pygame.Surface, v_screen: pygame.Surface, clock: pygame.time.Clock):
        super().__init__(screen, v_screen, clock)
        self._selection = 0

        # Texts
        self.title = Menu.MENU_TITLE_FONT.render('TITLE', False, (255, 255, 255))
        self.title_rect = self.title.get_rect(center=self._center).move(0, -50)
        self.start_option = Menu.MENU_SUB_FONT.render('Start Game', True, (255, 255, 255))
        self.start_option_selected = Menu.MENU_SUB_FONT.render('Start Game', True, (231, 76, 60))
        self.start_option_rect = self.start_option.get_rect(center=self._center).move(0, 30)
        self.quit_option = Menu.MENU_SUB_FONT.render('Quit', True, (255, 255, 255))
        self.quit_option_selected = Menu.MENU_SUB_FONT.render('Quit', True, (231, 76, 60))
        self.quit_option_rect = self.quit_option.get_rect(center=self._center).move(0, 60)

    # @Override
    def handle_event(self):
        for event in pygame.event.get():
            # Exit game
            if event.type == pygame.QUIT:
                return QuitState.Quit(self._screen, self._v_screen, self._clock)
            elif event.type == pygame.KEYDOWN:
                # Change menu selection
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self._selection = (self._selection + 1) % 2
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self._selection = 1 if self._selection == 0 else self._selection - 1
                # ENTER key
                elif event.key == pygame.K_RETURN:
                    # Start Game
                    if self._selection == 0:
                        return SplashScreenState.SplashScreen(self._screen, self._v_screen, self._clock)
                    # Quit Game
                    else:
                        return QuitState.Quit(self._screen, self._v_screen, self._clock)

    # @Override
    def draw(self):
        self._v_screen.fill((0, 0, 0))

        self._v_screen.blit(self.title, self.title_rect)
        self._v_screen.blit(self.start_option_selected if self._selection == 0 else self.start_option,
                            self.start_option_rect)
        self._v_screen.blit(self.quit_option_selected if self._selection == 1 else self.quit_option,
                            self.quit_option_rect)

    # @Override
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
