from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS

class Shot(CircleShape):
    containers = None

    def __init__(self, x, y):
        super().__init__(x, y,SHOT_RADIUS)
        pygame.sprite.Sprite.__init__(self)
        if self.containers:
            self.add(self.containers)

    def draw(self, screen):
        return pygame.draw.circle(screen, 'red',(self.position.x,self.position.y),self.radius,2)
    
    def update(self, dt):
        self.position += self.velocity * dt