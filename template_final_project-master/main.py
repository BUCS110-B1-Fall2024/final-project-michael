import pygame, sys
#import your controller
pygame.init()
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_height, screen_width))
screen.fill('black')

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
    #Create an instance on your controller object
    #Call your mainloop

# make rectangle
class Rectangle(pygame.sprite.Sprite):
    def __init__(self, width, length):
        self.w = width
        self.l = length
rectangle_1 = Rectangle(200,200)
rectangle_2 = Rectangle(200,200)
"""
# make ball
class PBall(pygame.sprite.Sprite):
    def __init__(self,):
 
# make keyboard inputs
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("a")
            if event.key == pygame.K_d:
                print('rigt')

"""
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######
# https://www.geeksforgeeks.org/how-to-get-keyboard-input-in-pygame/
# https://coderslegacy.com/python/python-pygame-tutorial/
# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
