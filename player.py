import pygame
from circleshape import *
from constants import *

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.radius = PLAYER_RADIUS
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self,screen):
        pygame.draw.polygon(screen,(255,255,255),self.triangle(),2)

    def rotate(self,dt,right):
        
        self.rotation += PLAYER_TURN_SPEED * dt if right else -PLAYER_TURN_SPEED * dt 
        if self.rotation >= 360:
            self.rotation -=360
        if self.rotation <= -360:
            self.rotation += 360
        

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt,True)
        if keys[pygame.K_d]:
            self.rotate(dt,False)
        if keys[pygame.K_w]:
            x =  int(self.position.x)
            print(x)

    def forward(self,dt):
        x =  int(self.position.x)
