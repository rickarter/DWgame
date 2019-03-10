import pygame
from pygame.locals import *

class Control:
    def __init__(self):
        self.flag_game = True
        self.clock = pygame.time.Clock()

    def control(self, GUI):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.flag_game = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.flag_game = False
                elif event.key == K_DOWN and GUI.cursor != 2:
                    GUI.cursor += 1
                elif event.key == K_UP and GUI.cursor != 0:
                    GUI.cursor -= 1

        pygame.display.update()
        self.clock.tick(60)
