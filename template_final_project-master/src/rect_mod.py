import pygame
speed = pygame.math.Vector2
ACC = 0.7
class Rectangle(pygame.sprite.Sprite):
    def __init__(self, locx, locy):
        super().__init__()
        self.surf = pygame.Surface((135, 10))
        self.surf.fill('white')
        self.image = self.surf
        self.rect = self.surf.get_rect(center = (locx, locy))
        self.acc = speed(0, 0)        
    def movement(self, l, r):
        key = pygame.key.get_pressed()
        if key[l]:
            self.acc.x = -ACC
            if self.rect.x < 0:
                self.rect.x = 800
        elif key[r]:
            self.acc.x = ACC
            if self.rect.x > 800:
                self.rect.x = 0
        else:
            self.acc.x = 0

        self.rect.x += self.acc.x  
rectangle_1 = Rectangle(385, 10)
rectangle_2 = Rectangle(386, 790)
