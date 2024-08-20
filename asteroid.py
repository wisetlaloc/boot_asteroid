import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        rotate_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        left = Asteroid(self.position.x, self.position.y, new_radius)
        left.velocity = self.velocity.rotate(rotate_angle) * 1.2
        right = Asteroid(self.position.x, self.position.y, new_radius)
        right.velocity = self.velocity.rotate(-rotate_angle) * 1.2

