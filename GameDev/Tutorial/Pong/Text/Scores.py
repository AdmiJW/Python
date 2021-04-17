import pygame

from GameDev.Tutorial.Pong.State import STATUS

from GameDev.Tutorial.Pong.Text.RenderableText import RenderableText


class Scores(RenderableText):

    def __init__(self, state):
        super().__init__(state)

        #   Texts
        score1 = self.getText( 2, str( state.Score1 )  )
        score1Rect = score1.get_rect( center=( self.WINDOW_WIDTH // 2 - 100, 100) )

        score2 = self.getText( 2, str( state.Score2 ) )
        score2Rect = score2.get_rect( center=(self.WINDOW_WIDTH // 2 + 100, 100) )

        self.toBlit = [ (score1, score1Rect, False), (score2, score2Rect, False) ]


    def updateScore(self, state):
        state.Status = STATUS.AWAIT_SERVE
        state.PendingUpdateScore = False

        score1 = self.getText(2, str(state.Score1))
        score1Rect = score1.get_rect(center=(self.WINDOW_WIDTH // 2 - 100, 100))

        score2 = self.getText(2, str(state.Score2))
        score2Rect = score2.get_rect(center=(self.WINDOW_WIDTH // 2 + 100, 100))

        self.toBlit = [(score1, score1Rect, False), (score2, score2Rect, False)]