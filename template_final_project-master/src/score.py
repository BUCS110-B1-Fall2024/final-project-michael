import pygame
from controller import pong


class Score:
    def __init__(self, locx, locy):
        self.score = 0
        self.locx = locx
        self.locy = locy
    def increase(self):
        self.score += 1
    def display(self):
        font = pygame.font.SysFont('Comic Sans MS', 30)
        display =  font.render(self.score, False, ('white'))
        return display
score_top = Score(0, 350)
score_bot = Score(0, 450)

