import pygame, sys, random
#import your controller
pygame.init()
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_height, screen_width))
tscore = 0
bscore = 0
#create sprites https://coderslegacy.com/python/pygame-platformer-game-development/


# make rectangle
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

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((12, 12)) # create abackground for ball
        self.image = self.surf 
        self.surf.fill('black') # fill the background for the ball
        self.ball = pygame.draw.circle(self.image, 'white', (6, 6), 6)
        self.rect = self.surf.get_rect(center = (400, 400))

pong = Ball()


class Dividor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((800, 2))
        self.image = self.surf
        self.surf.fill('white')
        self.line = pygame.draw.line(self.image, 'white', (0, 400), (800, 400))
        self.rect = self.surf.get_rect(center = (400, 400))

half = Dividor()
all_sprites = pygame.sprite.Group()
all_sprites.add(rectangle_1, rectangle_2, pong, half)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        rectangle_1.movement(pygame.K_LEFT, pygame.K_RIGHT)
        rectangle_2.movement(pygame.K_a, pygame.K_d)
        
        screen.fill('black')
        all_sprites.draw(screen)
        pygame.display.flip()
    #Create an instance on your controller object
    #Call your mainloop

    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######
# https://www.geeksforgeeks.org/how-to-get-keyboard-input-in-pygame/
# https://coderslegacy.com/python/python-pygame-tutorial/
# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
