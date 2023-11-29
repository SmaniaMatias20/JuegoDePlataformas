import re
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
from Modules.Values.Assets import BACKGROUND_SOUND


    
class FormMenuPlay(Form):
    def __init__(self, screen, x,y,w,h,color_background, color_border, active, path_image=""):
        super().__init__(screen, x,y,w,h,color_background, color_border, active)
        self.manejador_niveles = DriverLevels()  
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image, (w,h))
        self._slave = aux_image





        self._box_name = TextBox(screen=self._slave,
                          master_x=x,
                          master_y=y,
                          x=90,
                          y=50,
                          w= 230,
                          h= 50,
                          color_background = EColors.WHITE.value,
                          color_background_seleccionado= EColors.DARK_GOLDENROD.value,
                          color_border= EColors.DARK_GOLDENROD.value,
                          color_border_seleccionado= EColors.WHITE.value,
                          border_size= 4, 
                          font= "Arial Black",
                          font_color= EColors.BLACK.value,
                          font_size= 20,

                        )

        # Button Level One
        self._btn_level_1 = Button_Image(screen=self._slave,
                            master_x=x,
                            master_y=y,
                            x=100,
                            y=110,
                            w= 200,
                            h= 80,
                            onclick= self.create_level,
                            onclick_param= "level_one",
                            path_image= "Modules\Assets\Images\Menu\\table.png",
                            text = "Level One",
                            font = "Arial Black",
                            font_size = 25,
                            font_color = EColors.BLACK.value)
        
        # Button Level Two
        self._btn_level_2 = Button_Image(screen=self._slave,
                            master_x= x,
                            master_y=y,
                            x=100,
                            y=200,
                            w=200,
                            h=80,
                            onclick= self.create_level,
                            onclick_param= "level_two",
                            path_image= "Modules\Assets\Images\Menu\\table.png",
                            text = "Level Two",
                            font = "Arial Black",
                            font_size = 25,
                            font_color = EColors.BLACK.value)
        
        # Button Level Three
        self._btn_level_3 = Button_Image(screen=self._slave,
                            master_x= x,
                            master_y=y,
                            x=100,
                            y=290,
                            w= 200,
                            h= 80,
                            onclick= self.create_level,
                            onclick_param= "level_three",
                            path_image= "Modules\Assets\Images\Menu\\table.png",
                            text = "Level Three",
                            font = "Arial Black",
                            font_size = 25,
                            font_color = EColors.BLACK.value)
        
        # Button Home
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
        
        self.lista_widgets.append(self._box_name)
        self.lista_widgets.append(self._btn_level_1)
        self.lista_widgets.append(self._btn_level_2)
        self.lista_widgets.append(self._btn_level_3)
        self.lista_widgets.append(self._btn_home)
    
    def render(self):
        self._slave.fill(self._color_background)

    def sanitize_name(self):
        name_entered = self._box_name.get_text()
        cadena = re.sub("[0-9]+", "", name_entered)
        cadena = cadena.title()
        name = cadena.strip()

        if len(name) != 0:
            return name
        else:
            return "N/A"
 



    def update(self, events):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(events)
            self.draw()  
        else:
            self.hijo.update(events)

    def create_level(self, level_name):
        pygame.mixer.music.pause()
        name = self.sanitize_name()
        nivel = self.manejador_niveles.get_level(level_name)
        frm_contenedor_nivel = FormContainerLevel(self._master, nivel, name)
        self.show_dialog(frm_contenedor_nivel)

    def btn_home_click(self, param):
        self.end_dialog()