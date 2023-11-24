import pygame
import sys
from pygame.locals import *
from Modules.Gui.GUI_form_main import FormMain
from Modules.Levels.LevelOne import LevelOne
from Modules.Values.EColors import *

pygame.init()
WIDTH = 800
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
FPS = 20
form_main = FormMain(screen, 200, 50, 400, 400, EColors.BLACK.value, EColors.WHITE.value, 5, True)
# level = LevelOne((WIDTH,HEIGHT))

while True:
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # level.update(events)
    if form_main.exit:
        break

    screen.fill("Black")

    form_main.update(events)
    
    pygame.display.flip()