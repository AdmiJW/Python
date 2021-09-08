# What are particles? Particles:
#   >   Exist at a certain location at a certain time
#   >   Moves
#   >   Changes its size / speed over dt
#   >   Dissapear after some time (Probably also become smaller and smaller)
#
# Example of particles would be raindrops, grenade fragments, bullets, etc. Adding particles to your game would
# potentially create wholesome visual effects!
#
# This introduces the idea of particle generator. A particle generator is simply an object that generate particles.
# It controls the properties of the particle generated, like:
#   >   dx, dy of the particle
#   >   size of the particle
#   >   gravity affecting the particle
#   >   decay of the particle
# etc etc...
#
# Let's see how we create a grenade generator (which is a particle generator) that creates fragments (particles) on
# explosion!
import math
import random

import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

# A list of particles that we keep track of. It's more efficient to use a Set to able to remove in O(1)
particles = set()


###################
# Abstract Particle
###################
class Particle:
    # All particles should implement the following interfaces
    def update(self, dt): pass

    def render(self): pass

    # Return True if the particle no longer exists and should be removed from the game
    def is_dead(self): pass


##################
# Grenade
##################
class Grenade:
    # Grenade will detonate after self.life frames
    GRENADE_LIFE = 200
    GRAVITY = 1

    def __init__(self, _screen: pygame.Surface):
        self._screen = _screen
        self.centerx = self._screen.get_width() // 2
        self.centery = self._screen.get_height() // 2
        self.dx = random.randrange(-10, 10)
        self.dy = random.randrange(-40, -20)

        self.radius = self._screen.get_width() // 3

        self.life = Grenade.GRENADE_LIFE

    def update(self, dt):
        # Move in z direction, and get new radius
        self.radius = max(self.radius * 0.98, 3)

        # Move in x direction. Check screen boundary and adjust
        self.centerx += self.dx * dt
        if self.centerx - self.radius < 0:
            self.centerx = self.radius
            self.dx *= -0.8
        elif self.centerx + self.radius > self._screen.get_width():
            self.centerx = self._screen.get_width() - self.radius
            self.dx *= -0.8

        # Move in y direction. Check screen boundary and adjust
        self.centery += self.dy * dt
        if self.centery + self.radius > self._screen.get_height():
            self.centery = self._screen.get_height() - self.radius
            self.dy *= -0.7

        # Apply gravity
        self.dy += Grenade.GRAVITY * dt

        # Deduct the life of grenade
        self.life -= dt

    def is_dead(self):
        return self.life <= 0

    def generate_fragments(self):
        return (Fragment(self._screen,
                         self.centerx,
                         self.centery,
                         min(7, random.randrange(int(self.radius) - 2, int(self.radius) + 2)) )
                for i in range(random.randrange(150, 200)))

    def render(self):
        pygame.draw.circle(self._screen, (150, 0, 0), (self.centerx, self.centery), self.radius)


###################
# Fragments
###################
class Fragment(Particle):
    GRAVITY = 0.5
    LIFE = 120

    def __init__(self, screen, centerx, centery, radius):
        self._screen = screen
        self.centerx = centerx
        self.centery = centery
        self.radius = radius
        self.dx = random.randrange(-5, 5)
        self.dy = random.randrange(-25, 5)

        self.life = Fragment.LIFE

    def update(self, dt):
        # Move in x direction. Check screen boundary and adjust
        self.centerx += self.dx * dt

        # Move in y direction. Check screen boundary and adjust
        self.centery += self.dy * dt

        # Apply gravity
        self.dy += Fragment.GRAVITY * dt

        # Deduct the life of grenade
        self.life -= dt

    def is_dead(self):
        return self.life <= 0

    def render(self):
        pygame.draw.circle(self._screen, (0, 0, 0), (self.centerx, self.centery), self.radius)


font = pygame.font.SysFont('Arial', 30).render('Press Space to throw grenade', True, (0,0,0) )
font_rect = font.get_rect()
font_rect.bottom = screen.get_height() - 10
font_rect.centerx = screen.get_width() // 2

dt = 1
should_exit = False
while not should_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            should_exit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                particles.add(Grenade(screen))

    screen.fill((255, 255, 255))
    screen.blit( font, font_rect )

    # Updating the particles
    dead_particles = []

    for particle in particles:
        particle.update(dt)
        particle.render()

        if particle.is_dead():
            dead_particles.append(particle)

    for particle in dead_particles:
        if isinstance(particle, Grenade):
            for frag in particle.generate_fragments():
                particles.add(frag)
        particles.remove(particle)

    pygame.display.flip()
    dt = clock.tick(60) * 0.001 * 60

pygame.quit()
sys.exit()
