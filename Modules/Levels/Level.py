import pygame as py

from Modules.Values.EColors import EColors
from Modules.Values.Assets import *
from Modules.Values.EColors import *
from Modules.Characters.Hero import *

# FPS = 60

class Level:
    
    def __init__(self, size):


        self.size = size
        self.DEBUG = False
        self.screen = py.display.set_mode(self.size)
        self.running = True
        self.set_fps(20)
        self.clock = py.time.Clock()
        self.set_caption("Ragnarok")
        self.set_icon(GAME_ICON)
        # self.time = py.time.get_ticks()


    def update(self, list_events):
        for event in list_events:
            if event.type == py.KEYDOWN:
                if event.key == py.K_TAB:
                    self.change_mode()
        self.get_pressed()
        self.fill_screen()
        

    def draw_hitbox(self):
        if self.get_mode():
            for pl in self.platforms:
                for key in pl.rect:
                    py.draw.rect(self.screen, EColors.RED.value, pl.rect[key], 3)

            for key in self.hero.rect:
                    py.draw.rect(self.screen, EColors.GREEN.value, self.hero.rect[key], 3)
        
    def get_pressed(self):
        self.pressed_keys = py.key.get_pressed()  
    
    def show_score(self, text):
        font = py.font.SysFont('Arial Black', 20)
        text = font.render(f"score: {text}", True, EColors.WHITE.value)
        self.screen.blit(text, (5, 0))
  
    def set_caption(self, caption):
        py.display.set_caption(caption)

    def set_icon(self, icon):
        self.icon_image = py.image.load(icon)
        py.display.set_icon(self.icon_image)

    def set_fps(self, FPS):
        self.FPS = FPS

    def set_music(self, music):
        self.music = py.mixer.Sound(music)
        self.music.set_volume(0.2)
        self.play_music()
        
    def set_volume(self, volume):
        self.music.set_volume(volume)

    def play_music(self):
        self.music.play()

    def stop_music(self):
        self.music.stop()

    def set_background_image(self, background):
        self.background_image = py.image.load(background)
        self.background_image = py.transform.scale(self.background_image, self.size)

    def set_fuente(self):
        pass

    def fill_screen(self, color=None):
        if color != None:
            self.screen.fill(color)
        else:
            self.screen.blit(self.background_image, (0, 0))
    
    def change_mode(self):
        self.DEBUG = not self.DEBUG

    def get_mode(self):
        return self.DEBUG
    
    

    
