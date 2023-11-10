import pygame
from pygame.locals import *

from Modules.Gui.GUI_button import *
from Modules.Gui.GUI_form_container_level import *
from Modules.Gui.GUI_form_menu_play import *
from Modules.Gui.GUI_slider import *
from Modules.Gui.GUI_textbox import *
from Modules.Gui.GUI_label import *
from Modules.Gui.GUI_form import *
from Modules.Gui.GUI_button_image import *
from Modules.Gui.GUI_form_menu_score import *
from Modules.Levels.LevelOne import LevelOne
from Modules.Values.EColors import *


    
class FormMain(Form):
    def __init__(self, screen, FPS, x,y,w,h,color_background, color_border = "Black", border_size = -1, active = True):
        super().__init__(screen, x,y,w,h,color_background, color_border, border_size, active)
        
        self.FPS = FPS
        self.flag_play = True
        self.end = False
        # Musica de fondo
        self.volumen = 0.2
        pygame.mixer.init()
        pygame.mixer.music.load("Modules\Assets\Music\Vengeance (Loopable).wav")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)

        self.txt_name = TextBox(self._slave, 
                                        x, 
                                        y, 
                                        50, 
                                        50, 
                                        150, 
                                        30, 
                                        EColors.DARK_GOLDENROD.value, 
                                        EColors.DARK_GOLDENROD.value, 
                                        EColors.DARK_GOLDENROD.value, 
                                        EColors.DARK_GOLDENROD.value, 
                                        2, 
                                        "Comic Sans MS", 
                                        15, 
                                        EColors.DARK_GOLDENROD.value)
        
        self.btn_play = Button(self._slave, 
                                        x, 
                                        y, 
                                        100, 
                                        100, 
                                        100, 
                                        50, 
                                        EColors.DARK_ORANGE.value, 
                                        EColors.DARK_ORANGE.value, 
                                        self.btn_play_click, 
                                        "hola", 
                                        "Pausa", 
                                        "Verdana", 
                                        15, 
                                        EColors.DARK_ORANGE.value)

        self.slider_volumen = Slider(self._slave, 
                                            x, 
                                            y, 
                                            100, 
                                            200, 
                                            400, 
                                            15, 
                                            self.volumen, 
                                            EColors.DARK_ORANGE.value, 
                                            EColors.DARK_ORANGE.value)


        porcentaje_volumen = f"{self.volumen * 100}%"
        self.label_volumen = Label(self._slave, 
                                            650, 
                                            190, 
                                            100, 
                                            50, 
                                            porcentaje_volumen, 
                                            "Comic Sans MS", 
                                            15, 
                                            EColors.DARK_ORANGE.value,
                                            "Modules\Assets\Images\Menu\Table.png")

        # Boton para acceder a las puntuaciones
        self.btn_tabla = Button_Image(self._slave, 
                                            x, 
                                            y, 
                                            225, 
                                            100, 
                                            50, 
                                            50, 
                                            "Modules\Assets\Images\Menu\Menu_BTN.png", 
                                            self.btn_tabla_click, 
                                            "hola")
        
        # Boton para acceder al contenedor de niveles
        self.btn_levels = Button_Image(self._slave, 
                                            x, 
                                            y, 
                                            300, 
                                            100, 
                                            50, 
                                            50, 
                                            "Modules\Assets\Images\Menu\Menu_BTN.png", 
                                            self.btn_levels_click, 
                                            "hola")
        


        # Boton para salir del juego
        self.btn_end = Button_Image(self._slave, 
                                            x, 
                                            y, 
                                            300, 
                                            200, 
                                            50, 
                                            50, 
                                            "Modules\Assets\Images\Menu\Menu_BTN.png", 
                                            self.btn_end_click, 
                                            "hola")

        self.lista_widgets.append(self.txt_name)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.btn_tabla)
        self.lista_widgets.append(self.btn_levels)
        self.lista_widgets.append(self.btn_end)
    
    def render(self):
        self._slave.fill(self._color_background)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.update_volumen(lista_eventos)
                
        else:
            self.hijo.update(lista_eventos)

    def update_volumen(self, lista_eventos):
        # Subir o bajar el volumen
        self.volumen = self.slider_volumen.value
        self.label_volumen.update(lista_eventos)
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)
        
        
    


    # Acciones de los botones

    def btn_play_click(self, param):
        # Pausar musica
        if self.flag_play:
            pygame.mixer.music.pause()
            self.btn_play._color_background = EColors.DARK_ORANGE.value
            self.btn_play.set_text("Play")
        else:
            pygame.mixer.music.unpause()
            self.btn_play._color_background = EColors.DARK_ORANGE.value
            self.btn_play.set_text("Pause")

        self.flag_play = not self.flag_play

    def btn_tabla_click(self, param):
        # Sacar la informacion de un archivo.
        diccionario = [{"Jugador": "Mario", "Score": 250},
                      {"Jugador": "Gio", "Score": 150},
                      {"Jugador": "Fausto", "Score": 100},]
        
        nuevo_form = FormMenuScore(screen = self._master, 
        x = 250, 
        y = 25, 
        w = 500, 
        h = 550, 
        color_background = EColors.DARK_ORANGE.value, 
        color_border = EColors.DARK_ORANGE.value, 
        active = True, 
        path_image = "Modules\Assets\Images\Menu\Window.png", 
        scoreboard = diccionario, 
        margen_x = 10, 
        margen_y = 100, 
        espacio = 10
        )

        self.show_dialog(nuevo_form)
    
    def btn_levels_click(self, param):

        menu_play = FormMenuPlay(self._master, 
        FPS = self.FPS,
        x=250, 
        y= 25, 
        w= 500, 
        h=550, 
        color_background = EColors.DARK_ORANGE.value, 
        color_border = EColors.DARK_ORANGE.value, 
        active = True, 
        path_image = "Modules\Assets\Images\Menu\Window.png")

        self.show_dialog(menu_play)

    def btn_end_click(self, param):
        self.end = True