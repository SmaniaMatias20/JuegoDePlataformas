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
import pygame


    
class FormMain(Form):
    def __init__(self,screen,x,y,w,h,color_background, color_border = "Black", border_size = -1, active = True):

        super().__init__(screen, x,y,w,h,color_background, color_border, border_size, active)
        self.flag_play = True
        self.exit = False
        
        ########################################################
        # WIDTH = 800
        # HEIGHT = 500
        # self.screen = pygame.display.set_mode(size)
        # self.clock = pygame.time.Clock()
        # self.FPS = 30
        ########################################################


        # Musica de fondo
        # self.volumen = 0.2
        # pygame.mixer.init()
        # pygame.mixer.music.load("Modules\Assets\Music\Vengeance (Loopable).wav")
        # pygame.mixer.music.set_volume(self.volumen)
        # pygame.mixer.music.play(-1)
        ########################################################################


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

        # Boton para acceder a las puntuaciones
        self.btn_scores = Button_Image(self._slave, 
                                            x, 
                                            y, 
                                            150, 
                                            185, 
                                            200, 
                                            80, 
                                            "Modules\Assets\Images\Menu\star.png", 
                                            self.btn_scores_click, 
                                            "")
        
        # Boton para acceder al contenedor de niveles
        self.btn_levels = Button_Image(self._slave, 
                                            x, 
                                            y, 
                                            150, 
                                            75, 
                                            200, 
                                            80, 
                                            "Modules\Assets\Images\Menu\levels.png", 
                                            self.btn_levels_click, 
                                            "",
                                            color_background = EColors.BLACK.value)
        


        # Boton para salir del juego
        self.btn_quit = Button_Image(self._slave, 
                                            x, 
                                            y, 
                                            150, 
                                            300, 
                                            200, 
                                            80, 
                                            "Modules\Assets\Images\Menu\exit.png", 
                                            self.btn_quit_click, 
                                            "hola")
        
        # Boton para configuracion
        self.btn_config = Button_Image(self._slave, 
                                            x, 
                                            y, 
                                            425, 
                                            20, 
                                            50, 
                                            50, 
                                            "Modules\Assets\Images\Menu\config.png", 
                                            self.btn_config_click, 
                                            "hola")

        # self.lista_widgets.append(self.txt_name)
        # self.lista_widgets.append(self.btn_play_music)
        # self.lista_widgets.append(self.slider_volumen)
        # self.lista_widgets.append(self.label_volumen)
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
                # self.update_volumen(lista_eventos)   
        else:
            self.hijo.update(lista_eventos)


    # def update_volumen(self, lista_eventos):
    #     self.volumen = self.slider_volumen.value
    #     self.label_volumen.update(lista_eventos)
    #     self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
    #     pygame.mixer.music.set_volume(self.volumen)
        
    # Acciones de los botones
    def btn_play_click(self, param):
        if self.flag_play:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

        self.flag_play = not self.flag_play

    def btn_scores_click(self, param):
        # Sacar la informacion de un archivo.
        diccionario = [{"Jugador": "Mario", "Score": 250},
                      {"Jugador": "Gio", "Score": 150},
                      {"Jugador": "Fausto", "Score": 100},]
        
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
        menu_options = FormMenuOptions(self._master, 
        x= 200, 
        y= 25, 
        w= 400, 
        h= 400, 
        color_background = EColors.WHITE.value, 
        color_border = EColors.WHITE.value, 
        active = True, 
        path_image = "Modules\Assets\Images\Menu\window.png")

        self.show_dialog(menu_options)

    def btn_quit_click(self, param):
        self.exit = True