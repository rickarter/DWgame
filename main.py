import pygame
from pygame.locals import *
from control import Control
from gui import GUI
from player import Doctor

pygame.init()

GUI = GUI()
control = Control()
doctor = Doctor()
#Саша лох

# pygame.display.Info().current_w
# pygame.display.Info().current_h

win = pygame.display.set_mode((control.width, control.height), FULLSCREEN)
pygame.display.set_caption('DOCTOR WHO')

run = True
timer = pygame.time.Clock()

while control.flag_start:
    control.start(GUI)
    GUI.start(win)

while control.flag_game:
    control.game(doctor)
    doctor.draw(win)
