from Modules.Values.Assets import BACKGROUND_SOUND
from Modules.Gui.GUI_form_container_level import *
from Modules.Gui.GUI_form_menu_options import *
from Modules.Gui.GUI_form_menu_score import *
from Modules.Gui.GUI_form_menu_play import *
from Modules.Gui.GUI_button_image import *
from Modules.Gui.GUI_textbox import *
from Modules.Gui.GUI_button import *
from Modules.Gui.GUI_slider import *
from Modules.Values.EColors import *
from Modules.Gui.GUI_label import *
from Modules.Gui.GUI_form import *
from pygame.locals import *
import pygame as py


    
class FormMain(Form):
    def __init__(self,screen,x,y,w,h,color_background, color_border = "Black", border_size = -1, active = True):
        super().__init__(screen, x,y,w,h,color_background, color_border, border_size, active)
        self.exit = False
        self.volume = 0.1
        pygame.mixer.init()
        pygame.mixer.music.load(r"Modules\Assets\Music\background.mp3")
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play(-1)
        
        self._label_main = Label(screen=self._slave,
                          x=100,
                          y=40,
                          w= 200,
                          h= 50,
                          text= "Main Menu",   
                          font= "Arial Black",
                          font_color= EColors.BLACK.value,
                          font_size= 25,
                          path_image= "Modules\Assets\Images\Menu\\table.png"  
                        )

        # Button Score
        self.btn_scores = Button_Image(self._slave, 
                                            x, 
                                            y, 
                                            100, 
                                            205, 
                                            200, 
                                            80, 
                                            "Modules\Assets\Images\Menu\\table.png", 
                                            self.btn_scores_click, 
                                            "",
                                            "Scores",
                                            "Arial Black",
                                            25)
        
        # Button Levels
        self.btn_levels = Button_Image(self._slave, 
                                            x, 
                                            y, 
                                            100, 
                                            110, 
                                            200, 
                                            80, 
                                            "Modules\Assets\Images\Menu\\table.png", 
                                            self.btn_levels_click, 
                                            "",
                                            "Levels",
                                            "Arial Black",
                                            25)
        


        # Button Quit
        self.btn_quit = Button_Image(self._slave, 
                                            x, 
                                            y, 
                                            100, 
                                            300, 
                                            200, 
                                            80, 
                                            "Modules\Assets\Images\Menu\\table.png", 
                                            self.btn_quit_click, 
                                            "hola",
                                            "Quit",
                                            "Arial Black",
                                            25)
        
        # Button Config
        self.btn_config = Button_Image(self._slave, 
                                            x, 
                                            y, 
                                            335, 
                                            20, 
                                            40, 
                                            40, 
                                            "Modules\Assets\Images\Menu\config.png", 
                                            self.btn_config_click, 
                                            "hola")

        self.lista_widgets.append(self._label_main)
        self.lista_widgets.append(self.btn_scores)
        self.lista_widgets.append(self.btn_levels)
        self.lista_widgets.append(self.btn_quit)
        self.lista_widgets.append(self.btn_config)
    
    def render(self):
        self._slave.fill(self._color_background)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
        else:
            self.hijo.update(lista_eventos)

    def btn_scores_click(self, param):
        diccionario = []
        
        result = get_top_scores("Modules\Data\scores.db")
        for row in result:
            diccionario.append({"Player": row[0], "Score": row[1]})
        
        nuevo_form = FormMenuScore(screen = self._master, 
        x = 200, 
        y = 40, 
        w = 425, 
        h = 450, 
        color_background = EColors.WHITE.value, 
        color_border = EColors.WHITE.value, 
        active = True, 
        path_image = "Modules\Assets\Images\Menu\window.png", 
        scoreboard = diccionario, 
        margen_x = 10, 
        margen_y = 100, 
        espacio = 10
        )

        self.show_dialog(nuevo_form)
    
    def btn_levels_click(self, param):
        menu_play = FormMenuPlay(self._master, 
        x= 200, 
        y= 25, 
        w= 400, 
        h= 400, 
        color_background = EColors.WHITE.value, 
        color_border = EColors.WHITE.value, 
        active = True, 
        path_image = "Modules\Assets\Images\Menu\window.png")

        self.show_dialog(menu_play)

    def btn_config_click(self, param):
        self.menu_options = FormMenuOptions(self._master, 
        x= 200, 
        y= 100, 
        w= 400, 
        h= 300, 
        color_background = EColors.BLACK.value, 
        color_border = EColors.WHITE.value, 
        active = True, 
        path_image = "Modules\Assets\Images\Menu\window.png")

        self.show_dialog(self.menu_options)

    def btn_quit_click(self, param):
        self.exit = True