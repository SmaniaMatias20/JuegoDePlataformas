from Modules.Data.Data import *
from Modules.Gui.GUI_button_image import *
from Modules.Gui.GUI_form import *
from Modules.Gui.GUI_form_menu_pause import FormMenuPause
from Modules.Values.EColors import *

class FormContainerLevel(Form):
    def __init__(self, screen: pygame.Surface, level):
        super().__init__(screen, 0, 0, screen.get_width(), screen.get_height(), color_background = EColors.ALICE_BLUE.value)
        level.screen = self._slave
        self.level = level

        self._btn_home = Button_Image(screen = self._slave, 
                        master_x = self._x,
                        master_y= self._y,
                        x = self._w - 50,
                        y = self._h - 40,
                        w = 30,
                        h = 30,
                        onclick = self.btn_home_click,
                        onclick_param = "",
                        path_image = "Modules\Assets\Images\Menu\home.png") 
        
        self._btn_pause = Button_Image(screen = self._slave, 
                        master_x = self._x,
                        master_y= self._y,
                        x = self._w - 110,
                        y = self._h - 40,
                        w = 30,
                        h = 30,
                        onclick = self.btn_pause_click,
                        onclick_param = "",
                        path_image = "Modules\Assets\Images\Menu\pause.png") 
        
        self._btn_sound = Button_Image(screen = self._slave, 
                        master_x = self._x,
                        master_y= self._y,
                        x = self._w - 170,
                        y = self._h - 40,
                        w = 30,
                        h = 30,
                        onclick = self.btn_pause_click,
                        onclick_param = "",
                        path_image = "Modules\Assets\Images\Menu\sound.png") 
        
        self.lista_widgets.append(self.level)
        self.lista_widgets.append(self._btn_home)
        self.lista_widgets.append(self._btn_pause)
        self.lista_widgets.append(self._btn_sound)

    def render(self):
        self._slave.fill(self._color_background)

    def update(self, events):
        if not self.level.complete and self.level.hero.lives > 0 and self.level.time_remaining != 0:
            if self.verificar_dialog_result():
                if self.active:
                    self.draw()
                    self.render()
                    for widget in self.lista_widgets:
                        widget.update(events)
                    # self.update_volumen(lista_eventos)   
            else:
                self.hijo.update(events)
        else:
            insert_player_data("Modules\Data\scores.db", self.level.hero.name, self.level.hero.points, self.level.type)
            del self.level
            self.end_dialog()

    def btn_home_click(self, param):
        del self.level
        self.end_dialog()
    
    def btn_pause_click(self, param):
        self.level.pause_game()

        menu_pause = FormMenuPause(self._master, 
        x= 200, 
        y= 25, 
        w= 400, 
        h= 400, 
        color_background = EColors.WHITE.value, 
        color_border = EColors.WHITE.value, 
        active = True,
        level= self.level, 
        path_image = "Modules\Assets\Images\Menu\window.png")
    
        self.show_dialog(menu_pause)

        

          
 