import pygame
from pygame.locals import *

class Control:
    def __init__(self):
        self.flag_game = False
        self.flag_start = True
        self.gravity = True

        self.clock = pygame.time.Clock()
        self.width = 1920#pygame.display.Info().current_w
        self.height = 1080 #pygame.display.Info().current_h
        self.flag_jump = True

        self.speed = 0

        # self.myfont = pygame.font.SysFont(None, 96)

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


        '''posX = self.myfont.render('X' + str(doctor.x), False, (255, 255, 255))
        posY = self.myfont.render('Y' + str(doctor.y), False, (255, 255, 255))

        win.blit(posX, (100, 100))
        win.blit(posY, (300, 100))'''

        keys = pygame.key.get_pressed()

        # Gravity
        if self.gravity:
            if doctor.y < 950:
                doctor.y += 20
            if doctor.y > 950:
                doctor.y -= 5

        #Control
        if keys[K_d]:
            doctor.x += doctor.speed
        if keys[K_a]:
            doctor.x -= doctor.speed
        '''if keys[K_d] and keys[K_LSHIFT]:
            doctor.x += doctor.speed * 2
        if keys[K_a] and keys[K_LSHIFT]:
            doctor.x -= doctor.speed * 2'''
        #Jump

        if doctor.y == 950:
            self.flag_jump = True
        else:
            self.flag_jump = False

        '''if keys[K_SPACE] and self.flag_jump:
            self.gravity = False
            doctor.y -= 150
        else:
            self.gravity = True'''

        self.speed += 10
        pygame.display.update()
        self.clock.tick(60)

