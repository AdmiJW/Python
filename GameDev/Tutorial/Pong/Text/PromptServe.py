import pygame

from Tutorial.Pong.Text.RenderableText import RenderableText


class PromptServe(RenderableText):
    def __init__(self, state):
        super().__init__(state)

        prompt = self.getText(0, 'PRESS SPACE BAR')
        prompt2 = self.getText(0, 'TO SERVE!')
        promptRect = prompt.get_rect(center=(self.WINDOW_WIDTH // 2, 480))
        prompt2Rect = prompt2.get_rect(center=(self.WINDOW_WIDTH // 2, 520))

        self.toBlit = [(prompt, promptRect, True), (prompt2, prompt2Rect, True)]