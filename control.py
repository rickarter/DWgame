import pygame
from pygame.locals import *

class Control:
    def __init__(self):
        self.flag_game = True
        self.clock = pygame.time.Clock()
        self.width = pygame.display.Info().current_w
        self.height = pygame.display.Info().current_h

    def control(self, GUI):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.flag_game = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.flag_game = False
                elif event.key == K_DOWN:
                    GUI.cursor += 1
                    if GUI.cursor == 3:
                        GUI.cursor = 0
                elif event.key == K_UP:
                    GUI.cursor -= 1
                    if GUI.cursor == -1:
                        GUI.cursor = 2
                elif event.key == K_RETURN:
                    if GUI.cursor == 0:
                        print('Start')
                    elif GUI.cursor == 1:
                        print('Settings')
                    elif GUI.cursor == 2:
                        print('Exit')
                        self.flag_game = False

        pygame.display.update()
        self.clock.tick(60)
