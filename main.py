import pygame
from pygame.locals import *
from control import Control
from gui import GUI

pygame.init()

GUI = GUI()
control = Control()

pygame.display.Info().current_w
pygame.display.Info().current_h


win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('DOCTOR WHO')

run = True
timer = pygame.time.Clock()

while control.flag_game:
    control.control(GUI)
    GUI.start(win)