import pygame
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((12, 12)) # create abackground for ball
        self.image = self.surf 
        self.surf.fill('black') # fill the background for the ball
        self.ball = pygame.draw.circle(self.image, 'white', (6, 6), 6)
        self.rect = self.surf.get_rect(center = (400, 400))        
pong = Ball()