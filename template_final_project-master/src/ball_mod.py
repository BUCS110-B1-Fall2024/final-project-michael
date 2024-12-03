import pygame
import random
class Ball(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        super().__init__()
        self.surf = pygame.Surface((12, 12)) # create abackground for ball
        self.image = self.surf 
        self.ball = pygame.draw.circle(self.image, 'white', (6, 6), 6)
        self.rect = self.surf.get_rect(center = (400, 400))  
        self.posx = posx
        self.posy = posy     
        self.velx = 0.1
        self.vely = 0.15 
    def movement(self):
        self.posx += self.velx
        self.posy += self.vely
        if self.posx >= 800:
            self.velx = -self.velx + random.randrange(0, 0.05)
            self.vely = -self.vely + random.randrange(0, 0.05)
        if self.posx <= 0:
            self.velx = -self.velx + random.randrange(0, 0.05)
            self.vely = -self.vely + random.randrange(0, 0.05)
        if self.posy >= 800:
            self.posx = 400
            self.posy = 400
        if self.posy <= 0:
            self.posx = 400
            self.posy = 400
        self.rect.center = (self.posx, self.posy) # new posistion
    def coll(self, obj1, obj2):
        if self.rect.colliderect(obj1):
            self.velx = -self.velx
            self.vely = -self.vely
        if self.rect.colliderect(obj2):
            self.velx = -self.velx
            self.vely = -self.vely


