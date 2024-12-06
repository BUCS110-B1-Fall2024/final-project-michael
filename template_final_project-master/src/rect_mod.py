import pygame
speed = pygame.math.Vector2 
''' accerelation and speed '''
ACC = 0.55
class Rectangle(pygame.sprite.Sprite):
    def __init__(self, locx, locy): 
        ''' makes the paddles. The rectangles are on top of an image '''
        super().__init__()
        self.surf = pygame.Surface((135, 10)) 
        ''' size '''
        self.surf.fill('white') 
        ''' color '''
        self.image = self.surf 
        ''' shows the image '''
        self.rect = self.surf.get_rect(center = (locx, locy)) 
        ''' starting location '''
        self.acc = speed(0, 0) 
        ''' takes pygame math vectors though we will only be using the x direction, this is the accerelation. '''
        score = 0   
        self.score = score   
    def movement(self, l, r): 
        ''' if a key is pressed, then it moves left or right '''
        key = pygame.key.get_pressed()
        if key[l]:
            self.acc.x = -ACC 
            ''' goes opposite direction to right (left) if left key is pressed '''
            if self.rect.x < 0: 
                ''' if it goes out the border, it appears on the other side '''
                self.rect.x = 800
        elif key[r]:
            self.acc.x = ACC
            if self.rect.x > 800:
                self.rect.x = 0
        else:
            self.acc.x = 0 
            ''' accerelation is 0 if nothing is pressed '''
        self.rect.x += self.acc.x  

rectangle_1 = Rectangle(385, 10) 
''' makes the objects '''
rectangle_2 = Rectangle(386, 790)