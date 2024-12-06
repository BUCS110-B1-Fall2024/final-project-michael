import pygame

class Buttons(pygame.sprite.Sprite): # everything is in sprites
    def __init__(self, image, x, y): # loads the colors
        super().__init__()
        self.image = pygame.image.load(image) # loads the image
        self.rect = self.image.get_rect() # loads the rectangle on it
        self.rect = self.image.get_rect(center = (x, y)) # location    
red = Buttons('red.png', 200, 400) # the clickable blue and greens
green = Buttons('green.png', 600, 400)
