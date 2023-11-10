import pygame
import sys
from pygame.locals import *
from Modules.Gui.GUI_form_main import FormMain
from Modules.Levels.Level import Level
from Modules.Values.EColors import *

pygame.init()

level = Level((800, 500), 30) # Al juego le llega otro size, corregir
form_main = FormMain(level.screen, 50, 50, 700, 400, EColors.LIME_GREEN.value, EColors.WHITE.value, 3, True)


while True:
    level.clock.tick(level.FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if form_main.exit:
        break

    level.screen.fill("Black")
    form_main.update(events)
    
    pygame.display.flip()