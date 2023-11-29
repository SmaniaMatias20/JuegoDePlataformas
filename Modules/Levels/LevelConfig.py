from Modules.Values.Assets import *
from Modules.Values.EColors import *
from Modules.Characters.Hero import *

import pygame as py

class LevelConfig:
    
    def __init__(self, size):
        py.mixer.init()

        self.complete = False
        self.pause = False
        self.size = size
        self.screen = py.display.set_mode(self.size)
        self.running = True
        self.DEBUG = False
        self.set_fps(25)
        self.clock = py.time.Clock()
        self.set_caption("Juego Segundo Parcial")
        self.set_icon(GAME_ICON)
        self.max_time = 180000
        self.start_time = py.time.get_ticks()
        self.time_remaining = 180
        
        

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
            
            for trap in self.traps:
                for key in trap.rect:
                    py.draw.rect(self.screen, EColors.DARK_ORANGE.value, trap.rect[key], 3)
            
            for item in self.items:
                for key in item.rect:
                    py.draw.rect(self.screen, EColors.DARK_VIOLET.value, item.rect[key], 3)
            
            for enemy in self.enemys:
                for key in enemy.rect:
                    py.draw.rect(self.screen, EColors.LIGHT_CYAN.value, enemy.rect[key], 3)

            for fo in self.falling_objects:
                for key in fo.rect:
                    py.draw.rect(self.screen, EColors.PINK.value, fo.rect[key], 3)
            
            for projectile in self.hero.list_projectile:
                for key in projectile.rect:
                    py.draw.rect(self.screen, EColors.YELLOW.value, projectile.rect[key], 3)



        
    def get_pressed(self):
        self.pressed_keys = py.key.get_pressed()  
    
    def show_score(self, text):
        font = py.font.SysFont('Arial Black', 25)
        text = font.render(f"score: {text}", True, EColors.WHITE.value)
        self.screen.blit(text, (self.screen.get_width() - 200, self.screen.get_height() - 490))
  
    def set_caption(self, caption):
        py.display.set_caption(caption)

    def set_icon(self, icon):
        self.icon_image = py.image.load(icon)
        py.display.set_icon(self.icon_image)

    def set_fps(self, FPS):
        self.FPS = FPS

    def set_music(self, music):
        self.music = py.mixer.Sound(music)
        self.music.set_volume(0.1)
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

    def fill_screen(self, color=None):
        if color != None:
            self.screen.fill(color)
        else:
            self.screen.blit(self.background_image, (0, 0))
    
    def change_mode(self):
        self.DEBUG = not self.DEBUG

    def get_mode(self):
        return self.DEBUG
    
    def create_text(self, message: str, color: tuple, size: int, font: str):
        my_font = py.font.SysFont(font, size)
        created_message = my_font.render(message, 0, color)

        return created_message
    
    def apply_text(self, message: str, location_x: int, location_y: int, color: list, size: int, font: str = ""):
        created_message = self.create_text(message, color, size, font)
        self.screen.blit(created_message, (location_x, location_y))

    def pause_game(self):
        self.pause = True
        self.paused_time = py.time.get_ticks() - self.start_time

    def resume_game(self):
        self.pause = False
        self.start_time = py.time.get_ticks() - self.paused_time

    def show_time(self):

        if not self.pause:
            current_time = py.time.get_ticks() - self.start_time
            remaining_time = max(self.max_time - current_time, 0)
        else:
            remaining_time = max(self.max_time - self.paused_time, 0)

        remaining_seconds = remaining_time // 1000
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60

        self.time_remaining = minutes * 60 + seconds

        message = f"{minutes:02}:{seconds:02}"

        if self.time_remaining <= 20:
            self.apply_text(message, 350, 10, EColors.RED.value, 30, "Arial Black")
        else:
            self.apply_text(message, 350, 10, EColors.WHITE.value, 30, "Arial Black")


    


    
