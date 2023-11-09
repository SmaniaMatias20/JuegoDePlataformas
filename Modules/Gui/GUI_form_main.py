import pygame as py

from Modules.Gui.GUI_button import *
from Modules.Gui.GUI_slider import *
from Modules.Gui.GUI_textbox import *
from Modules.Gui.GUI_label import *
from Modules.Gui.GUI_form import *
from Modules.Gui.GUI_button_image import *
from Modules.Gui.GUI_form_menu_score import *
from Modules.Gui.GUI_form_menu_score import *
from Modules.Gui.GUI_form_options import *
from Modules.Levels.DriverLevels import *

from Modules.Gui.GUI_picture_box import PictureBox

class FormMain(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border = "Black", border_size = -1, active = True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.volumen = 0.2
        self.flag_play = True

        self.jugar = False

        py.mixer.init()

        #### CONTROLS ####

        # SOLO PARA ESCRIBIR
        #self.txtbox = TextBox(self._slave, x, y, 50, 50, 150, 30, "Gray", "White", "Red", "Blue", 2, "Comic Sans", 15, "Black")

        # BOTON DE LA MUSICA
        #self.btn_play = Button(self._slave, x, y, 100, 100, 100, 50, "Red", "Blue", self.btn_play_click, "Nombre", "Pause", "Verdana", 15, "White")
        
        # PORCENTAJE MUSICA
        #self.label_volumen = Label(self._slave, 650, 190, 100, 50, "20%", "Comic Sans", 15, "White", "Table.png")
        # control volumen
        #self.slider_volumen = Slider(self._slave, x, y, 100, 200, 500, 15, self.volumen, "Blue", "White")

        # BACKGROUND
        # TITLE
        # self.title = PictureBox(self._slave, x, y, 600, 200, "title.png")

        # PLAY
        # self.btn_level_selector = Button_Image(self._slave, x, y, 100, 200, 50, 50, "Modules\Assets\Images\Menu\Menu_BTN.png", self.btn_level_selector_click, "lalala")

        # RANKING
        self.btn_tabla = Button_Image(self._slave, x, y, 100, 300, 50, 50, "Modules\Assets\Images\Menu\Menu_BTN.png", self.btn_tabla_click, "lalala")

        # OPTIONS
        self.btn_options = Button_Image(self._slave, x, y, 100, 100, 50, 50, "Modules\Assets\Images\Menu\Menu_BTN.png", self.btn_options_click, "lalala")
        #### ####

        #### APPEND CONTROLS IN LIST ####
        # self.lista_widgets.append(self.txtbox)
        # self.lista_widgets.append(self.btn_play)
        # self.lista_widgets.append(self.label_volumen)
        # self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.btn_tabla)
        # self.lista_widgets.append(self.title)
        self.lista_widgets.append(self.btn_options)
        # self.lista_widgets.append(self.btn_level_selector)
        

        # MUSIC
        # py.mixer.music.load("sounds/music/menu_music.mp3")

        # py.mixer.music.set_volume(self.volumen)
        # py.mixer.music.play(-1)

        self.render()
    
    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                #self.update_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos)
            if self.hijo.tipo == "Options":
                #print(self.hijo.flag_play)
                self.flag_play = self.hijo.flag_play
                self.btn_play_click("asdf")
            elif self.hijo.tipo == "LevelSelector":   # "LevelSelector"
                if self.hijo.playing["Play"] == True:
                    self.jugar = True

    def render(self):
        self._slave.fill(self._color_background)

    def btn_play_click(self, texto):

        #### TRAIGO LO QUE ESCRIBO EN EL CUADRO DE TEXTO
        # nombre = self.txtbox.get_text()
        # print(nombre)

        if self.flag_play:
            py.mixer.music.pause()
        else:
            py.mixer.music.unpause()
           
        
        #self.flag_play = not self.flag_play
    
    def update_volumen(self, lista_eventos):   
        self.volumen = self.slider_volumen.value
        #self.label_volumen.set_text("{:.0%}" .format(self.volumen))
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        
        py.mixer.music.set_volume(self.volumen)
    
    def btn_options_click(self, texto):
        form_options = FormMenuOptions(self._master,
                                        500,
                                        250,
                                        500,
                                        500,
                                        (220, 0, 220),
                                        (255,255,255),
                                        True,
                                        "Modules\Assets\Images\Menu\Window.png",
                                        self.volumen,
                                        self.flag_play)
        self.show_dialog(form_options)

    def btn_tabla_click(self, texto):
        #SQL
        dic_score = [{"Jugador": "Gio", "Score": 1000},
                     {"Jugador": "Fausto", "Score": 900},
                     {"Jugador": "Gonza", "Score": 750}]

        form_puntaje = FormMenuScore(self._master, 
                                     250,
                                     250,
                                     500,
                                     500,
                                     (220, 0, 220),
                                     (255,255,255),
                                     True,
                                     "Modules\Assets\Images\Menu\Window.png",
                                     dic_score,
                                     100,
                                     100,
                                     10)

        self.show_dialog(form_puntaje)

    # def btn_level_selector_click(self, texto):
        
    #     form_level_selector = DriverLevels(self._master, 
    #                                  200,
    #                                  100,
    #                                  1500,
    #                                  700,
    #                                  (220, 0, 220),
    #                                  "White",
    #                                  True,
    #                                  "Modules\Assets\Images\Menu\Window.png")
        
    #     self.show_dialog(form_level_selector)




































# class FormMain(Form):
#     def __init__(self, screen, x,y,w,h,color_background, color_border = "Black", border_size = -1, active = True):
#         super().__init__(screen, x,y,w,h,color_background, color_border, border_size, active)

#         ##COMPLETAR
    




#     def render(self):
#         self._slave.fill(self._color_background)






#     def update(self, lista_eventos):
#         if self.verificar_dialog_result():
#             if self.active:
#                 self.draw()
#                 self.render()
#                 for widget in self.lista_widgets:
#                     widget.update(lista_eventos)
#                 self.update_volumen(lista_eventos)
                
#         else:
#             self.hijo.update(lista_eventos)




#     def update_volumen(self, lista_eventos):
#         self.volumen = self.slider_volumen.value
#         self.label_volumen.update(lista_eventos)
#         self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
#         pygame.mixer.music.set_volume(self.volumen)
        
        
    
#     def btn_play_click(self, param):
#        pass
    
    
#     def btn_tabla_click(self, param):
#        pass