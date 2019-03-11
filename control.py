import pygame
from pygame.locals import *

class Control:
    def __init__(self):
        self.flag_game = False
        self.flag_start = True

        self.clock = pygame.time.Clock()
        self.width = 1920#pygame.display.Info().current_w
        self.height = 1080 #pygame.display.Info().current_h

    def start(self, GUI):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pass
                elif event.key == K_DOWN:
                    GUI.cursor += 1
                    if GUI.cursor == 3:
                        GUI.cursor = 0
                elif event.key == K_UP:
                    GUI.cursor -= 1
                    if GUI.cursor == -1:
                        GUI.cursor = 2
                elif event.key == K_RETURN:
                    if GUI.cursor == 0: #Start
                        self.flag_start = False
                        self.flag_game = True
                    elif GUI.cursor == 1: #Setting
                        pass
                    elif GUI.cursor == 2: #Exit
                        self.flag_start = False
                        self.flag_game = False

        pygame.display.update()
        self.clock.tick(60)

    def game(self, doctor):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.flag_game = False

        keys = pygame.key.get_pressed()
        if keys[K_d]:
            doctor.x += doctor.speed
        if keys[K_a]:
            doctor.x -= doctor.speed
        '''if keys[K_d] and keys[K_LSHIFT]:
            doctor.x += doctor.speed * 2
        if keys[K_a] and keys[K_LSHIFT]:
            doctor.x -= doctor.speed * 2'''

        pygame.display.update()
        self.clock.tick(60)

