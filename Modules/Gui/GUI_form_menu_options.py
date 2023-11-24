import pygame
from pygame.locals import *

from Modules.Gui.GUI_button import *
from Modules.Gui.GUI_form_container_level import *
from Modules.Gui.GUI_slider import *
from Modules.Gui.GUI_textbox import *
from Modules.Gui.GUI_label import *
from Modules.Gui.GUI_form import *
from Modules.Gui.GUI_button_image import *
from Modules.Gui.GUI_form_menu_score import *
from Modules.Levels.DriverLevels import *


    
class FormMenuOptions(Form):
    def __init__(self, screen, x,y,w,h,color_background, color_border, active, path_image=""):
        super().__init__(screen, x,y,w,h,color_background, color_border, active)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image, (w,h))
        self._slave = aux_image

        # self.btn_play_music = Button_Image(self._slave, 
        #                                 x, 
        #                                 y, 
        #                                 625, 
        #                                 75, 
        #                                 50, 
        #                                 50,
        #                                 "Modules\Assets\Images\Menu\sound_on.png",
        #                                 self.btn_play_click, 
        #                                 "")

        # self.slider_volumen = Slider(self._slave, 
        #                                     x, 
        #                                     y, 
        #                                     400, 
        #                                     30, 
        #                                     200, 
        #                                     15, 
        #                                     self.volumen, 
        #                                     EColors.BLACK.value, 
        #                                     EColors.WHITE.value)
        
        # porcentaje_volumen = f"{self.volumen * 100}%"
        # self.label_volumen = Label(self._slave, 
        #                                     625, 
        #                                     10, 
        #                                     50, 
        #                                     50, 
        #                                     porcentaje_volumen, 
        #                                     "Comic Sans MS", 
        #                                     20, 
        #                                     EColors.WHITE.value,
        #                                     "Modules\Assets\Images\Menu\porcentaje.png")
        
        self._btn_home = Button_Image(screen=self._slave,
                            master_x = self._x,
                            master_y= self._y,
                            x = self._w - 50,
                            y = self._h - 50,
                            w= 30,
                            h= 30,
                            onclick= self.btn_home_click,
                            onclick_param= "",
                            path_image= "Modules\Assets\Images\Menu\home.png")
        
        # self.lista_widgets.append(self._btn_level_1)
        # self.lista_widgets.append(self._btn_level_2)
        # self.lista_widgets.append(self._btn_level_3)
        self.lista_widgets.append(self._btn_home)
    
    def render(self):
        self._slave.fill(self._color_background)

    def update(self, events):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(events)
            self.draw()  
        else:
            self.hijo.update(events)

    def btn_home_click(self, param):
        self.end_dialog()