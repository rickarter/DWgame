import pygame
from pygame.locals import *

pygame.font.init()


class GUI:
    def __init__(self):
        '''myfont = pygame.font.SysFont(None, 30)
        self.start_ = myfont.render('Start', False, (255, 255, 255))'''
        self.width = 300
        self.height = 100
        self.centerPosX = 500 / 2 - self.width / 2
        self.centerPosY = 500 / 2 - self.height / 2
        self.cursor = 0

        self.colorStart = (255, 255, 255)
        self.colorSettings = (255, 255, 255)
        self.colorExit = (255, 255, 255)

    def start(self, win):

        if self.cursor == 0:
            self.colorStart = (0, 0, 255)
        else:
            self.colorStart = (255, 255, 255)

        if self.cursor == 1:
            self.colorSettings = (0, 0, 255)
        else:
            self.colorSettings = (255, 255, 255)

        if self.cursor == 2:
            self.colorExit = (0, 0, 255)
        else:
            self.colorExit = (255, 255, 255)

        # Start
        pygame.draw.rect(win, self.colorStart,
                         (self.centerPosX, self.centerPosY - self.height - 7, self.width, self.height), 8)

        # Settings
        pygame.draw.rect(win, self.colorSettings,
                         (self.centerPosX, self.centerPosY, self.width, self.height), 8)

        # Exit
        pygame.draw.rect(win, self.colorExit,
                         (self.centerPosX, self.centerPosY + self.height + 7, self.width, self.height), 8)

    def pause(self):
        pass
