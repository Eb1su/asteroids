import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    frame_rate = pygame.time.Clock()
    dt = 0
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        for ast in asteroids:
            if ast.collision_check(player) == True:
                print("Game over!")
                sys.exit()
        

        pygame.Surface.fill(screen, "black")
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = frame_rate.tick(60) / 1000



if __name__ == "__main__":
    main()
