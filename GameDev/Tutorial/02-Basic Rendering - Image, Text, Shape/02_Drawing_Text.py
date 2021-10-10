
# All of the Font functionality is in pygame.font module
# We could use our own custom font by specifying where the .ttf file is located, or use
# System Available fonts using pygame.font.SysFont class.
#
# To display a text on our game, we simply create a Font first, then use render() method of it.

import pygame
pygame.init()


##############################
# Counter class
##############################
class Counter:
    # The Font instances that we will be using
    LG_FONT = pygame.font.SysFont('arial', 65, bold=True)
    SM_FONT = pygame.font.SysFont('arial', 40)

    def __init__(self, screen):
        self._screen = screen
        self._score = 0

        self.prompt = Counter.LG_FONT.render('Press Space to Increment:', True, (255,255,255))
        self.scoretext = Counter.SM_FONT.render( str(self._score) , True, (255,255,255))

        screen_center = self._screen.get_rect().center
        self._screen.blit( self.prompt, self.prompt.get_rect(center=(screen_center[0], screen_center[1] - 30) ) )
        self._screen.blit( self.scoretext, self.scoretext.get_rect(center=(screen_center[0], screen_center[1] + 30) ) )

    # This method handles both the logic of incrementing counter as well as updating the screen.
    # Be sure to pass the dirty_rects array into this method
    def increment(self, dirty_rects):
        self._score += 1
        self.scoretext = Counter.SM_FONT.render( str(self._score), True, (255,255,255))

        screen_center = self._screen.get_rect().center
        score_text_rect_center = self.scoretext.get_rect(center=(screen_center[0], screen_center[1] + 30))
        self._screen.fill((0,0,0), score_text_rect_center)
        self._screen.blit(self.scoretext, score_text_rect_center)

        dirty_rects.append( score_text_rect_center )


###############################
# End of Counter class
################################

screen = pygame.display.set_mode( (800, 450) )
pygame.display.set_caption("Counter")

clock = pygame.time.Clock()
should_exit = False

counter = Counter(screen)
pygame.display.flip()

while not should_exit:
    dirty_rects = []

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            should_exit = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            counter.increment(dirty_rects)

    pygame.display.update(dirty_rects)

    clock.tick(30)

pygame.quit()
quit()