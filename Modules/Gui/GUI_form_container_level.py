from Modules.Data.Data import *
from Modules.Gui.GUI_button_image import *
from Modules.Gui.GUI_form import *
from Modules.Gui.GUI_form_menu_pause import FormMenuPause
from Modules.Values.EColors import *

class FormContainerLevel(Form):
    def __init__(self, screen: pygame.Surface, level, name):
        super().__init__(screen, 0, 0, screen.get_width(), screen.get_height(), color_background = EColors.ALICE_BLUE.value)
        level.screen = self._slave
        self.level = level
        self.flag_music_play = True
        self.player_name = name

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
                        onclick = self.btn_sound_click,
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
            else:
                self.hijo.update(events)
        else:
            self.level.stop_music()
            if self.level.complete:
                insert_player_data("Modules\Data\scores.db", self.player_name, self.level.hero.points, self.level.type)
            del self.level
            self.end_dialog()

    def btn_home_click(self, param):
        self.level.stop_music()
        del self.level
        self.end_dialog()
    
    def btn_sound_click(self, param):
        if self.flag_music_play:
            self.level.stop_music()
        else:
            self.level.play_music()
        
        self.flag_music_play = not self.flag_music_play



    def btn_pause_click(self, param):
        self.level.pause_game()
        self.level.stop_music()

        menu_pause = FormMenuPause(self._master, 
        x= 200, 
        y= 100, 
        w= 400, 
        h= 300, 
        color_background = EColors.WHITE.value, 
        color_border = EColors.WHITE.value, 
        active = True,
        level= self.level, 
        path_image = "Modules\Assets\Images\Menu\window.png")
    
        self.show_dialog(menu_pause)

        

          
 