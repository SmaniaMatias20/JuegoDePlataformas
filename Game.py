from Modules.Levels.LevelConfig import LevelConfig
from Modules.Gui.GUI_form_main import FormMain
from Modules.Values.EColors import *
from pygame.locals import *
import pygame
import sys

class Game(LevelConfig):
    def __init__(self, size):
        super().__init__(size)
        pygame.init()
        self.screen
        self.form_main = FormMain(self.screen, 200, 50, 400, 400, EColors.BLACK.value, EColors.WHITE.value, 5, True)

    def init(self):
        while True:
            self.clock.tick(self.FPS)
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if self.form_main.exit:
                break

            self.screen.fill("Black")

            self.form_main.update(events)
            
            pygame.display.flip()