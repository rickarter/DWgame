import pygame


class Doctor:

    def __init__(self):
        self.x = 100
        self.y = 800
        self.speed = 10

        self.width = 80
        self.height = 101

    def draw(self, win):
        win.fill((0, 0, 0))
        pygame.draw.rect(win, (0, 0, 255), (self.x, self.y, self.width, self.height))

    def animation(self):
        pass

    def sonic_screwdriver(self):
        pass
