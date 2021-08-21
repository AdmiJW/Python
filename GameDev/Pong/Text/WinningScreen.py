import pygame

from Pong.Text.RenderableText import RenderableText

class WinningScreen(RenderableText):

    def __init__(self, state):
        super().__init__(state)

        #   Texts
        title = self.getText(1, 'PLAYER')
        title2 = self.getText(1, str(state.Winner) )
        title3 = self.getText(1, 'WINS!')

        prompt = self.getText(0, 'PRESS SPACE BAR')
        prompt2 = self.getText(0, 'TO CONTINUE!')

        titleRect = title.get_rect(center=(self.WINDOW_WIDTH // 2, 80))
        title2Rect = title2.get_rect(center=(self.WINDOW_WIDTH // 2, 160))
        title3Rect = title3.get_rect(center=(self.WINDOW_WIDTH // 2, 240))

        promptRect = prompt.get_rect(center=(self.WINDOW_WIDTH // 2, 420))
        prompt2Rect = prompt2.get_rect(center=(self.WINDOW_WIDTH // 2, 460))

        self.toBlit = [(title, titleRect, False), (title2, title2Rect, False), (title3, title3Rect, False), \
                       (prompt, promptRect, True), (prompt2, prompt2Rect, True)]

    def updateWinner(self, state):
        self.__init__(state)