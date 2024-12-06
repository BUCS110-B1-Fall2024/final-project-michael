import pygame
import random
#from score import Score, score_top, score_bot
class Ball(pygame.sprite.Sprite):
    def __init__(self, posx, posy, respawns, score):
        super().__init__()
        self.surf = pygame.Surface((12, 12)) # create abackground for ball
        self.image = self.surf 
        self.ball = pygame.draw.circle(self.image, 'white', (6, 6), 6)
        self.rect = self.surf.get_rect(center = (400, 400))  
        self.posx = posx
        self.posy = posy     
        self.velx = (random.uniform(-0.25, -0.15) or random.uniform(0.15, 0.25))
        self.vely = 1.3
        self.respawns = respawns
        self.score = score
    def ball_respawn(self):
        self.posx = 400
        self.posy = 400
        self.vely = 1.3
        self.velx = (random.uniform(-0.25, -0.15) or random.uniform(0.15, 0.25))
        self.respawns += 1
        
    def movement(self):
        self.posx += self.velx
        self.posy += self.vely
        if self.posx >= 800:
            self.velx = -self.velx 
        if self.posx <= 0:
            self.velx = -self.velx 
        if self.posy >= 800:
            self.ball_respawn()
        if self.posy <= 0:
             self.ball_respawn()
        self.rect.center = (self.posx, self.posy) # new posistion
    def coll(self, obj1, obj2):
        if self.rect.colliderect(obj1):
            self.vely = -self.vely 
            self.score += 1
        if self.rect.colliderect(obj2):
            self.vely = -self.vely 
            self.score += 1
    def scores(self):
        score = self.score
        score = str(score)
        return score
    def respawns(self):
        return int(self.respawns)
        


