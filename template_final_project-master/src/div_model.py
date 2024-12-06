import pygame
class Divider(pygame.sprite.Sprite): 
    ''' using sprites '''
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((800, 2)) 
        ''' length of the divider '''
        self.image = self.surf 
        self.surf.fill('white') 
        ''' makes the line white '''
        self.line = pygame.draw.line(self.image, 'white', (0, 400), (800, 400)) 
        ''' line is drawn '''
        self.rect = self.surf.get_rect(center = (400, 400)) 
        ''' rectangle it is onn is drawn '''
half = Divider() 
''' makes the divider '''
