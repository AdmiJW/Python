import pygame, sys

#   INITIALIZATION ===================
pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=512)
pygame.init()


from Tutorial.Pong.State import STATE, STATUS

from Tutorial.Pong.Pads.PlayerPad import PlayerPad
from Tutorial.Pong.Pads.EnemyPad import EnemyPad

from Tutorial.Pong.Text.MainMenu import MainMenu
from Tutorial.Pong.Text.WinningScreen import WinningScreen
from Tutorial.Pong.Text.Scores import Scores
from Tutorial.Pong.Text.PromptServe import PromptServe

from Tutorial.Pong.Ball import Ball

from Tutorial.Pong.Sounds.Sounds import Sounds


#   STATE ===========================

state = STATE

#   WINDOW INITIALIZATION =============
DISPLAY = pygame.display.set_mode( ( state.WINDOW_WIDTH, state.WINDOW_HEIGHT ) )
pygame.display.set_caption("My Pong")

CLOCK = pygame.time.Clock()




#   PLAYER ===========================
PLAYER_PAD = PlayerPad(state)
ENEMY_PAD = EnemyPad(state)

BALL = Ball(state)

MAIN_MENU = MainMenu(state)
WINNING_SCREEN = WinningScreen(state)
SCORES = Scores(state)
PROMPTSERVE = PromptServe(state)

Sounds.playMenu()


#   GAME LOOP ===========================
while True:
    #   LOGIC =================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if state.Status == STATUS.MENU:
                state.Status = STATUS.AWAIT_SERVE
                Sounds.playPlaying()
            elif state.Status == STATUS.AWAIT_SERVE:
                state.Status = STATUS.BALL_TRAVELLING
            elif state.Status == STATUS.WIN:
                state.Status = STATUS.MENU
                Sounds.playMenu()
        if event.type == pygame.mixer.music.get_endevent():
            print('ENDD')

    if state.Score1 >= state.WINNING_SCORE:
        Sounds.playVictory()
        state.Score1 = 0
        state.Score2 = 0
        state.Winner = 1
        SCORES.updateScore( state )
        BALL.reset()
        WINNING_SCREEN.updateWinner(state)
        state.Status = STATUS.WIN
    if state.Score2 >= state.WINNING_SCORE:
        Sounds.playVictory()
        state.Score1 = 0
        state.Score2 = 0
        state.Winner = 2
        SCORES.updateScore( state )
        WINNING_SCREEN.updateWinner(state)
        BALL.reset()
        state.Status = STATUS.WIN

    PLAYER_PAD.move()
    ENEMY_PAD.move()

    if state.Status == STATUS.BALL_TRAVELLING:
        BALL.move( (PLAYER_PAD, ENEMY_PAD) )

    if state.PendingUpdateScore:
        SCORES.updateScore(state)


    #   DISPLAY ===============
    DISPLAY.fill( (0,0,0) )

    PLAYER_PAD.render( DISPLAY )
    ENEMY_PAD.render( DISPLAY )

    if state.Status == STATUS.MENU:
        MAIN_MENU.render( DISPLAY )
    elif state.Status == STATUS.WIN:
        WINNING_SCREEN.render( DISPLAY )
    else:
        if state.Status == STATUS.AWAIT_SERVE:
            PROMPTSERVE.render( DISPLAY )

        SCORES.render( DISPLAY )
        BALL.render( DISPLAY )

    pygame.display.update()
    CLOCK.tick( state.FPS )


