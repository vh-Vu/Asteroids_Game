import pygame
import random
from circleshape import CircleShape 
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,0),self.position,self.radius,2)
    
    def update(self,dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        blue_angle = random.uniform(20,50)
        random_angle = self.velocity.rotate(blue_angle)
        minus_random_angle = self.velocity.rotate(-blue_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        child1_asteroid = Asteroid(self.position.x,self.position.y,new_radius)
        child2_asteroid = Asteroid(self.position.x,self.position.y,new_radius)
        child1_asteroid.velocity = random_angle*1.2
        child2_asteroid.velocity = minus_random_angle*1.2
