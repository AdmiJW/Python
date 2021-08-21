from enum import Enum


class STATUS(Enum):
    MENU = 1
    WIN = 2
    BALL_TRAVELLING = 3
    AWAIT_SERVE = 4


class STATE:
    FPS = 60
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

    WINNING_SCORE = 5

    Score1 = 0
    Score2 = 0
    Status = STATUS.MENU
    Server = 0
    Winner = 1

    PendingUpdateScore = False
    IsWinnerDecided = False