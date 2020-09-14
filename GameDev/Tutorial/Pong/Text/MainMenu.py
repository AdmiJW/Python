import pygame

from Tutorial.Pong.Text.RenderableText import RenderableText

class MainMenu(RenderableText):

    def __init__(self, state):
        super().__init__(state)

        #   Texts
        title = self.getText(2, 'PONG')
        titleRect = title.get_rect(center=(self.WINDOW_WIDTH // 2, 120))

        prompt = self.getText(0, 'PRESS SPACE BAR')
        prompt2 = self.getText(0, 'TO PLAY!')
        promptRect = prompt.get_rect(center=(self.WINDOW_WIDTH // 2, 280))
        prompt2Rect = prompt2.get_rect(center=(self.WINDOW_WIDTH // 2, 330))

        self.toBlit = [(title, titleRect, False), (prompt, promptRect, True),
                       (prompt2, prompt2Rect, True)]



