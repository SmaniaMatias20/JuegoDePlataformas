import pygame as py

# from modulos.values.assets import BACKGROUND_IMAGE
FPS = 60

class Config:

    def __init__(self, size, FPS, caption="Title", icon=""):
        py.mixer.init()
        
        self.size = size
        self.screen = py.display.set_mode(self.size)
        self.running = True
        self.FPS = FPS
        self.clock = py.time.Clock()
        self.set_caption(caption)
        self.DEBUG = False

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
    
    
