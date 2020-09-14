import pygame


class RenderableText:

    def getText(self, size, text):
        return self.bigFont.render(text, False, (255,255,255), (0,0,0) ) if size == 2 \
            else self.smallFont.render(text, False, (255,255,255), (0,0,0) ) if size == 0 \
            else self.midFont.render(text, False, (255,255,255), (0,0,0) )

    def __init__(self, state):

        self.WINDOW_WIDTH = state.WINDOW_WIDTH
        self.WINDOW_HEIGHT = state.WINDOW_HEIGHT

        self.bigFont = pygame.font.Font('Text/ArcadeFont.ttf', 140)
        self.bigFont.set_bold(True)

        self.midFont = pygame.font.Font('Text/ArcadeFont.ttf', 60)

        self.smallFont = pygame.font.Font('Text/ArcadeFont.ttf', 30)

        self.transparency = 255
        self.isFading = True


    def render(self, surface):
        self.transparency += 5 if not self.isFading else -5
        if self.transparency > 255 or self.transparency < 0:
            self.isFading = not self.isFading

        for txtTuple in self.toBlit:
            if txtTuple[2]:
                txtTuple[0].set_alpha( self.transparency )
            surface.blit( txtTuple[0], txtTuple[1] )