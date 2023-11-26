from Modules.Levels.LevelConfig import LevelConfig
from Modules.Gui.GUI_form_main import FormMain
from Modules.Values.EColors import *
from pygame.locals import *
import pygame as py
import sys

class Game(LevelConfig):
    def __init__(self, size):
        super().__init__(size)
        self.screen
        self.form_main = FormMain(self.screen, 200, 50, 400, 400, EColors.BLACK.value, EColors.WHITE.value, 5, True)

    def init(self):
        
        py.init()

        while self.running:
            self.clock.tick(self.FPS)
            events = py.event.get()
            for event in events:
                if event.type == QUIT:
                    py.quit()
                    sys.exit()

            if self.form_main.exit:
                self.running = False

            self.screen.fill(EColors.GOLDEN.value)

            self.form_main.update(events)
            
            py.display.flip()
        py.quit()