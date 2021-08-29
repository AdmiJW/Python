
# Drawing shapes in pygame is done via pygame.draw module. We can use it to draw simple shapes like rectangle, squares,
# circles, polygons or lines
#
# Unlike loading from images, it does not return a Surface which we need to manually blit onto the screen. Instead,
# it will blit it readily for us onto the screen.

import random

import pygame

pygame.init()


#################
# BouncableShape
#################
class BouncableShape:
    def __init__(self, screen, color):
        self._screen = screen
        self._screen_width = screen.get_width()
        self._screen_height = screen.get_height()
        self._color = color
        self.dx = random.randrange(-5, 5)
        self.dy = random.randrange(-5, 5)

    def update_and_draw(self, dirty_rects): pass


#################
# Bouncing Square
#################
class BouncingSquare(BouncableShape):
    def __init__(self, screen, side_length, color):
        super().__init__(screen, color)

        self._side_length = side_length
        self.x = random.randrange(0, self._screen_width - self._side_length)
        self.y = random.randrange(0, self._screen_height - self._side_length)

        self.prev_rect = pygame.draw.rect(self._screen, self._color,
                                          (self.x, self.y, self._side_length, self._side_length))

    def update_and_draw(self, dirty_rects):
        self._screen.fill((0, 0, 0), self.prev_rect)
        dirty_rects.append(self.prev_rect)
        self.x += self.dx
        self.y += self.dy

        # Boundary checking
        if self.x <= 0 or self.x > self._screen_width - self._side_length:
            self.x = min(self._screen_width - self._side_length, max(0, self.x))
            self.dx = -self.dx
        if self.y <= 0 or self.y > self._screen_height - self._side_length:
            self.y = min(self._screen_height - self._side_length, max(0, self.y))
            self.dy = -self.dy

        self.prev_rect = pygame.draw.rect(self._screen, self._color,
                                          (self.x, self.y, self._side_length, self._side_length))
        dirty_rects.append(self.prev_rect)


####################
# Bouncing Circle
####################
class BouncingCircle(BouncableShape):
    def __init__(self, screen, radius, color):
        super().__init__(screen, color)

        self._radius = radius
        self.x = random.randrange(0, self._screen_width - self._radius)
        self.y = random.randrange(0, self._screen_height - self._radius)

        self.prev_rect = pygame.draw.circle(self._screen, self._color,
                                            (self.x, self.y), self._radius)

    def update_and_draw(self, dirty_rects):
        self._screen.fill((0, 0, 0), self.prev_rect)
        dirty_rects.append(self.prev_rect)
        self.x += self.dx
        self.y += self.dy

        # Boundary checking
        if self.x <= self._radius or self.x > self._screen_width - self._radius:
            self.x = min(self._screen_width - self._radius, max(self._radius, self.x))
            self.dx = -self.dx
        if self.y <= self._radius or self.y > self._screen_height - self._radius:
            self.y = min(self._screen_height - self._radius, max(self._radius, self.y))
            self.dy = -self.dy

        self.prev_rect = pygame.draw.circle(self._screen, self._color,
                                            (self.x, self.y), self._radius)
        dirty_rects.append(self.prev_rect)
#############################################




screen = pygame.display.set_mode((800, 450))
pygame.display.set_caption('Shapes')

clock = pygame.time.Clock()
should_exit = False

square = BouncingSquare(screen, 60, (255, 255, 255))
circle = BouncingCircle(screen, 30, (255, 255, 255))

while not should_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            should_exit = True

    dirty_rects = []
    square.update_and_draw(dirty_rects)
    circle.update_and_draw(dirty_rects)

    pygame.display.update(dirty_rects)

    clock.tick(60)

pygame.quit()
quit()
