import pygame, sys
from ball_mod import Ball
from rect_mod import Rectangle
from div_model import Dividor, half
pygame.init()

rectangle_1 = Rectangle(385, 10)
rectangle_2 = Rectangle(386, 790)
pong = Ball(400, 400, 0)

#### make these not global
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_height, screen_width))
all_sprites = pygame.sprite.Group()
all_sprites.add(rectangle_1, rectangle_2, half)
def start(text, color, x, y):
    font = pygame.font.SysFont('Comic Sans MS', 30)
    start_screen = font.render(text, False, (color))
    screen.blit(start_screen, (x, y))


def main():
    game_started = False
    second_test = False
    respawns = True
    
    while True:
        screen.fill('white')
        if game_started == True:
            screen.fill('blue')
            pass
        else:
            start("Press space to start", 'black', 300, 300)
        if second_test == True:
            screen.fill('black')
            all_sprites.add(pong)
            pass
        else:
            start("Press u for unlimitred respawns, i for one", 'white', 100, 600)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_SPACE:  
                    print("Game Started!")
                    game_started = True  
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:
                    print("Unlimited Respawns")
                    second_test = True
                if event.key == pygame.K_i:
                    respawns = False
                    second_test = True
            

        rectangle_1.movement(pygame.K_LEFT, pygame.K_RIGHT)
        rectangle_2.movement(pygame.K_a, pygame.K_d)
        pong.movement()
        pong.coll(rectangle_1, rectangle_2)
        all_sprites.draw(screen)
        if respawns == False:
            if pong.respawns >= 1:
                break
        pygame.display.flip()


if __name__ == '__main__':
    main()
