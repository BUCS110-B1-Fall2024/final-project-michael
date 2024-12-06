import pygame, sys
from ball_mod import Ball, pong
from rect_mod import Rectangle, rectangle_1, rectangle_2
from div_model import Dividor, half
from colors import Buttons, red, green
pygame.init()
clock = pygame.time.Clock()
clock.tick(60)  # sets it to 60 fps


screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_height, screen_width))
all_sprites = pygame.sprite.Group()
def start(text, color, x, y, size):
    font = pygame.font.SysFont('Comic Sans MS', size)
    start_screen = font.render(text, False, (color))
    screen.blit(start_screen, (x, y))


def main():
    game_started = False
    second_test = False
    respawns = True
    while True:
        screen.fill('white')
        if game_started == True:
            screen.fill('black')
            all_sprites.add(red, green)
            pass
        else:
            start("Press space to start", 'black', 300, 300, 30)
        if second_test == True:
            all_sprites.remove(red, green)
            screen.fill('black')
            all_sprites.add(rectangle_1, rectangle_2, half, pong)
            start(f"Your score is: {pong.scores()}", 'white', 200, 200, 10)
            pass
        else:
            start("Click red for unlimited respawns, green for two", 'white', 100, 200, 30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_SPACE:  
                    print("Game Started!")
                    game_started = True  
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if (85 <= x <= 315) and (285 <= y <= 515):
                    print("Unlimited Respawns")
                    second_test = True
                if (485 <= x <= 715) and (285 <= y <= 515):
                    respawns = False
                    second_test = True
            

        rectangle_1.movement(pygame.K_LEFT, pygame.K_RIGHT)
        rectangle_2.movement(pygame.K_a, pygame.K_d)
        pong.movement()
        pong.coll(rectangle_1, rectangle_2)
        all_sprites.draw(screen)
        if respawns == False:
            if pong.respawns >= 2:
                screen.fill('white')
                start("You Lose!", 'black', 350, 350, 40)
        pygame.display.flip()


if __name__ == '__main__':
    main()
