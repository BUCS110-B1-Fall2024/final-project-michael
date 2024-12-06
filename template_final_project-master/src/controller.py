'''
imports
'''
import pygame, sys
from ball_mod import Ball, pong
from rect_mod import Rectangle, rectangle_1, rectangle_2
from div_model import Divider, half
from colors import Buttons, red, green
pygame.init() 
''' initalizations '''
clock = pygame.time.Clock()
clock.tick(60)  
''' sets it to 60 fps '''


screen_width = 800 
''' sets screen size '''
screen_height = 800
screen = pygame.display.set_mode((screen_height, screen_width)) 
''' sets screen  '''
all_sprites = pygame.sprite.Group() 
''' sets the sprites to be used '''
def start(text, color, x, y, size): 
    ''' function for the text '''
    font = pygame.font.SysFont('Comic Sans MS', size) 
    ''' system font, size '''
    start_screen = font.render(text, False, (color)) 
    ''' variable to render with text and font '''
    screen.blit(start_screen, (x, y)) 
    ''' location '''


def main():
    game_started = False 
    ''' variables for different GUI screens '''
    second_test = False
    respawns = True
    while True: 
        ''' main loops '''
        screen.fill('white') 
        """ first loop """
        if game_started == True: 
            ''' Black screen with instructions, when space is pressed, next screen '''
            screen.fill('black')
            all_sprites.add(red, green)
            pass
        else:
            start("Press space to start", 'black', 300, 300, 30)
        if second_test == True: 
            ''' second screen '''
            all_sprites.remove(red, green) 
            ''' game loop starts when mouse is clicked on either blue or green '''
            screen.fill('black')
            all_sprites.add(rectangle_1, rectangle_2, half, pong)
            start(f"Your score is: {pong.scores()}", 'white', 25, 410, 10) 
            ''' shows score '''
            pass
        else:
            start("Click red for unlimited respawns, green for two", 'white', 100, 200, 30)
        for event in pygame.event.get(): 
            ''' main loop '''
            if event.type == pygame.QUIT: 
                ''' allows tab to be closed '''
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN: 
                ''' if space is clicked, the first screen is passed '''
                if event.key == pygame.K_SPACE:  
                    print("Game Started!")
                    game_started = True  
            
            if event.type == pygame.MOUSEBUTTONDOWN: 
                ''' if mouse button is clicked on one of the buttons, game is started '''
                x, y = pygame.mouse.get_pos()
                if (85 <= x <= 315) and (285 <= y <= 515):
                    print("Unlimited Respawns") 
                    second_test = True 
                    ''' variable for second screen '''
                if (485 <= x <= 715) and (285 <= y <= 515):
                    respawns = False 
                    ''' respawn variable is here, which means there will be respawns '''
                    second_test = True
            

        rectangle_1.movement(pygame.K_LEFT, pygame.K_RIGHT) 
        ''' movement keys '''
        rectangle_2.movement(pygame.K_a, pygame.K_d)
        pong.movement() 
        ''' pong movements '''
        pong.coll(rectangle_1, rectangle_2) 
        ''' collisions for the two paddles '''
        all_sprites.draw(screen) 
        ''' draws the screen '''
        if respawns == False: 
            ''' if all respawns are used and green is pressed, ends the game '''
            if pong.respawns >= 2:
                screen.fill('white')
                start("You Lose!", 'black', 350, 350, 40)
        pygame.display.flip()


if __name__ == '__main__':
    main()
