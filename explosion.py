# explosion.py
import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, position, radius):
        super().__init__()
        self.position = position
        self.radius = radius
        self.lifetime = 0.3  # Duration of the explosion
        self.elapsed = 0

    def update(self, dt):
        self.elapsed += dt
        if self.elapsed > self.lifetime:
            self.kill()  # Remove the explosion after it finishes

    def draw(self, screen):
        alpha = 255 * (1 - self.elapsed / self.lifetime)  # Fading effect
        color = (255, 100, 100, alpha)  # Adjust color as needed
        pygame.draw.circle(screen, color, self.position, int(self.radius))
