import pygame

pygame.mixer.music.set_endevent( 666 )
pygame.mixer.music.set_volume(.3)

class Sounds:
    BALLHIT = pygame.mixer.Sound('Sounds/BallHit.wav')
    BALLSCORE = pygame.mixer.Sound('Sounds/BallScore.wav')

    @staticmethod
    def playMenu():
        pygame.mixer.music.stop()
        pygame.mixer.music.load('Sounds/menu.wav')
        pygame.mixer.music.play(-1)

    @staticmethod
    def playPlaying():
        pygame.mixer.music.stop()
        pygame.mixer.music.load('Sounds/playing.wav')
        pygame.mixer.music.set_endevent(666)
        pygame.mixer.music.play(-1)

    @staticmethod
    def playVictory():
        pygame.mixer.music.stop()
        pygame.mixer.music.load('Sounds/victory.wav')
        pygame.mixer.music.play(0)

