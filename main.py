import sys

import pygame

from asteroid import Asteroid
from asteroid_field import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    AsteroidField()

    Shot.containers = (bullets, updatable, drawable)

    dt = 0
    tick = clock.tick(60) / 1000
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable:
            obj.update(tick)
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game over!")
                sys.exit(0)
            for bullet in bullets:
                if bullet.is_colliding(asteroid):
                    bullet.kill()
                    asteroid.split()
        pygame.display.flip()
        dt += tick


if __name__ == "__main__":
    main()
