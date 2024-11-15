import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidField import AsteroidField
from shot import Shot
from explosion import Explosion

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        for obj in asteroids:
            if obj.collision_check(player):
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision_check(shot):
                    asteroid.split()
                    explosion = Explosion(asteroid.position, asteroid.radius)
                    score += 5
                    updatable.add(explosion)
                    drawable.add(explosion)
                    



        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, "white")
        screen.blit(score_text, (10, 10))


        pygame.display.flip()  

        dt = clock.tick(60) / 1000 # Limit framerate to 60 FPS


        

if __name__ == "__main__":
    main()
