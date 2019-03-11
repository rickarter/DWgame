import pygame
from pygame.locals import *
from control import Control

pygame.font.init()

class GUI:

    def __init__(self):
        self.control = Control()
        self.width = pygame.display.Info().current_w * .5
        self.height = pygame.display.Info().current_h * .2
        self.centerPosX = self.control.width / 2
        self.centerPosY = self.control.height / 2
        self.cursor = 0

        self.colorStart = (255, 255, 255)
        self.colorSettings = (255, 255, 255)
        self.colorExit = (255, 255, 255)
        
        self.myfont = pygame.font.SysFont(None, 144)
        self.start_ = self.myfont.render('Start', False, self.colorStart)
        self.settings = self.myfont.render('Settings', False, self.colorSettings)
        self.exit = self.myfont.render('Exit', False, self.colorExit)

    def start(self, win):
        self.start_ = self.myfont.render('Start', False, self.colorStart)
        self.settings = self.myfont.render('Settings', False, self.colorSettings)
        self.exit = self.myfont.render('Exit', False, self.colorExit)

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
                         (self.centerPosX - self.width / 2, self.centerPosY - self.height / 2 - self.height - 7, self.width, self.height), 8)
        win.blit(self.start_, (self.centerPosX - 192, self.centerPosY - 192 / 4 - self.height))

        # Settings
        pygame.draw.rect(win, self.colorSettings,
                         (self.centerPosX - self.width / 2, self.centerPosY - self.height / 2, self.width, self.height), 8)
        win.blit(self.settings, (self.centerPosX - 192, self.centerPosY - 192 / 4))

        # Exit
        pygame.draw.rect(win, self.colorExit,
                         (self.centerPosX - self.width / 2, self.centerPosY - self.height / 2 + self.height + 7, self.width, self.height), 8)
        win.blit(self.exit, (self.centerPosX - 192, self.centerPosY - 192 / 4 + self.height))

    def pause(self):
        pass
