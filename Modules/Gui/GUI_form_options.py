import pygame as py
from pygame.locals import *

from Modules.Gui.GUI_form import *
from Modules.Gui.GUI_label import *
from Modules.Gui.GUI_button_image import *
from Modules.Gui.GUI_slider import Slider
from Modules.Gui.GUI_button import *

class FormMenuOptions(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active, path_image, volumen, flag_play):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)

        self.tipo = "Options"
        self.flag_play = flag_play
        # BOTON DE LA MUSICA

        color_background = "Cyan"
        font_color = "Red"
        text = "Play"
        if self.flag_play:
            color_background = "Red"
            font_color = "White"
            text = "Pause"
            
        self.btn_play = Button(self._slave, x, y, 100, 100, 100, 50, color_background, "Blue", self.btn_play_click, "Nombre", text, "Verdana", 15, font_color)
        
        # PORCENTAJE MUSICA
        self.label_volumen = Label(self._slave, 650, 190, 100, 50, "20%", "Comic Sans", 15, "White", "Modules\Assets\Images\Menu\Table.png")
        # control volumen
        self.slider_volumen = Slider(self._slave, x, y, 100, 200, 250, 15, volumen, "Blue", "White")

        # append
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)

        self._btn_home = Button_Image(
                                    screen=self._slave,
                                    x = w-70,
                                    y = h-70,
                                    master_x = x,
                                    master_y = y,
                                    w = 50,
                                    h = 50,
                                    color_background = (255,0,0),
                                    color_border = (255,0,255),
                                    onclick = self.btn_home_click,
                                    onclick_param = "",
                                    text = "",
                                    font = "Verdana",
                                    font_size = 15,
                                    font_color = (0,255,0),
                                    path_image = "Modules\Assets\Images\Menu\home.png")
        
        self.lista_widgets.append(self._btn_home)

        self.render()

    def btn_play_click(self, texto):
        if self.flag_play:
            self.btn_play._color_background = "Cyan"
            self.btn_play._font_color = "Red"
            self.btn_play.set_text("Play")
        else:
            self.btn_play._color_background = "Red"
            self.btn_play._font_color = "White"
            self.btn_play.set_text("Pause")
        self.flag_play = not self.flag_play

    def btn_home_click(self, param):
        self.end_dialog()
        
    def update(self, lista_eventos):
        if self.active:
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
    
