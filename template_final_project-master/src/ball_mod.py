import pygame
import random
#from score import Score, score_top, score_bot
class Ball(pygame.sprite.Sprite):
    def __init__(self, posx, posy, respawns, score):
        super().__init__()
        self.surf = pygame.Surface((12, 12)) # create abackground for ball
        self.image = self.surf # creates an image for the ball
        self.ball = pygame.draw.circle(self.image, 'white', (6, 6), 6) # creates the ball itself
        self.rect = self.surf.get_rect(center = (400, 400)) # centers the ball when formed
        self.posx = posx # posistions
        self.posy = posy     
        self.velx = (random.uniform(-0.25, -0.15) or random.uniform(0.15, 0.25)) # velocity of x is random so the ball does not go the same direction 
        self.vely = 1.3 # velocity of y is 1.3
        self.respawns = respawns # respawns
        self.score = score # score tracking
    def ball_respawn(self): # if the ball is out of bounds, it respawns
        self.posx = 400
        self.posy = 400
        self.vely = 1.3
        self.velx = (random.uniform(-0.25, -0.15) or random.uniform(0.15, 0.25))
        self.respawns += 1 # adds 1 repsawn to the list
        
    def movement(self):
        self.posx += self.velx # moves the ball at the velocity 
        self.posy += self.vely 
        if self.posx >= 800: # if the ball its a wall, it reflects
            self.velx = -self.velx 
        if self.posx <= 0:
            self.velx = -self.velx 
        if self.posy >= 800: # if it goes out of bounds (ceiling or floor) it respawns)
            self.ball_respawn()
        if self.posy <= 0:
             self.ball_respawn()
        self.rect.center = (self.posx, self.posy) # new posistion
    def coll(self, obj1, obj2):
        if self.rect.colliderect(obj1): # if it collides with the rectangles (obj1, obj2), it reflects and gets a speed boost
            self.vely = -self.vely * 1.1
            self.score += 1 # if it collides, one is added to the score
        if self.rect.colliderect(obj2):
            self.vely = -self.vely * 1.1
            self.score += 1
    def scores(self): # score tracker for the controller
        score = self.score
        score = str(score)
        return score
    def respawns(self): # respawn tracker for the controller
        return int(self.respawns)
        

pong = Ball(400, 400, 0, 0) # makes the ball

