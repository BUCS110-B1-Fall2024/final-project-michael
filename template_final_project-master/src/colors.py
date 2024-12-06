import pygame

class Buttons(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(center = (x, y))        
red = Buttons('red.png', 200, 400)
green = Buttons('green.png', 600, 400)
