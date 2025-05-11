import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    clock = pygame.time.Clock()
    dt = 0


    # grouping classes to execute on gameloop
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable,drawable)
    Shot.containers = (shots,updatable,drawable)
    asteroidFieldObject = AsteroidField()
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while running:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
          screen.fill('black')

          for item in drawable:
               item.draw(screen)

          updatable.update(dt)

          for asteroid in asteroids:
               for shot in shots:
                    if asteroid.collide(shot):
                         asteroid.split()
                         shot.kill()

          for asteroid in asteroids:
               if asteroid.collide(player):
                    print("Game over!")
                    sys.exit()



          pygame.display.flip()
          
          tick = clock.tick(60)
          dt = tick/1000
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
        main()
