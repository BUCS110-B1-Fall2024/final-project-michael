import pygame
class Dividor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((800, 2))
        self.image = self.surf
        self.surf.fill('white')
        self.line = pygame.draw.line(self.image, 'white', (0, 400), (800, 400))
        self.rect = self.surf.get_rect(center = (400, 400))
half = Dividor()
