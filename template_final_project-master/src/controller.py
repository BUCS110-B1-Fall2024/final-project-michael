import pygame, sys
pygame.init()
from ball_mod import Ball
from rect_mod import Rectangle
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_height, screen_width))
rectangle_1 = Rectangle(385, 10)
rectangle_2 = Rectangle(386, 790)

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


if __name__ == '__main__':
    main()
