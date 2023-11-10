import pygame
import sys
from pygame.locals import *
from Modules.Gui.GUI_form_main import FormMain
from Modules.Values.EColors import *

pygame.init()
WIDTH = 800
HEIGHT = 500
FPS = 30

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

form_prueba = FormMain(screen, FPS, 200, 100, 900, 350, EColors.DARK_GOLDENROD.value, EColors.DARK_GREEN.value, 3, True)

while True:
    clock.tick(FPS)
    eventos = pygame.event.get()
    for event in eventos:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()



    if form_prueba.end:
        break



    screen.fill("Black")
    form_prueba.update(eventos)
    
    pygame.display.flip()