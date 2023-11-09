import pygame
from pygame.locals import *

from Modules.Gui.GUI_button import *
from Modules.Gui.GUI_form_container_level import FormContainerLevel
from Modules.Gui.GUI_slider import *
from Modules.Gui.GUI_textbox import *
from Modules.Gui.GUI_label import *
from Modules.Gui.GUI_form import *
from Modules.Gui.GUI_button_image import *
from Modules.Gui.GUI_form_menu_score import *
from Modules.Levels.DriverLevels import *


    
class FormMenuPlay(Form):
    def __init__(self, screen, x,y,w,h,color_background, color_border, active, path_image=""):
        super().__init__(screen, x,y,w,h,color_background, color_border, active)
        self.manejador_niveles = DriverLevels(self._master)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image, (w,h))
        self._slave = aux_image

        self._btn_level_1 = Button_Image(screen=self._slave,
                            master_x=x,
                            master_y=y,
                            x=100,
                            y=100,
                            w=100,
                            h=150,
                            onclick= self.entrar_nivel,
                            onclick_param= "level_one",
                            path_image= "Modules\Assets\Images\Menu\home.png")
        self._btn_level_2 = Button_Image(screen=self._slave,
                            master_x= x,
                            master_y=y,
                            x=250,
                            y=100,
                            w=100,
                            h=150,
                            onclick= self.entrar_nivel,
                            onclick_param= "level_two",
                            path_image= "Modules\Assets\Images\Menu\home.png")
        self._btn_level_3 = Button_Image(screen=self._slave,
                            master_x = self._x,
                            master_y= self._y,
                            x = self._w - 100,
                            y = self._h - 100,
                            w= 100,
                            h= 150,
                            color_background= (255, 0, 0),
                            color_border= (255, 0, 255),
                            onclick= self.entrar_nivel,
                            onclick_param= "level_three",
                            path_image= "Modules\Assets\Images\Menu\home.png")
        self._btn_home = Button_Image(screen=self._slave,
                            master_x = self._x,
                            master_y= self._y,
                            x = self._w - 100,
                            y = self._h - 100,
                            w= 50,
                            h= 50,
                            onclick= self.btn_home_click,
                            onclick_param= "",
                            path_image= "Modules\Assets\Images\Menu\home.png")
        
        self.lista_widgets.append(self._btn_level_1)
        self.lista_widgets.append(self._btn_level_2)
        self.lista_widgets.append(self._btn_level_3)
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

    def entrar_nivel(self, nombre_nivel):
        nivel = self.manejador_niveles.get_nivel(nombre_nivel)
        frm_contenedor_nivel = FormContainerLevel(self._master, nivel)
        self.show_dialog(frm_contenedor_nivel)

    def btn_home_click(self, param):
        self.end_dialog()