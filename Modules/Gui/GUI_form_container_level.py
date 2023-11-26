from Modules.Gui.GUI_button_image import *
from Modules.Gui.GUI_form import *
from Modules.Gui.GUI_form_menu_pause import FormMenuPause
from Modules.Values.EColors import *

class FormContainerLevel(Form):
    def __init__(self, screen: pygame.Surface, nivel):
        super().__init__(screen, 0, 0, screen.get_width(), screen.get_height(), color_background = EColors.ALICE_BLUE.value)
        nivel.screen = self._slave
        self.nivel = nivel

        self._btn_home = Button_Image(screen = self._slave, 
                        master_x = self._x,
                        master_y= self._y,
                        x = self._w - 50,
                        y = self._h - 50,
                        w = 30,
                        h = 30,
                        onclick = self.btn_home_click,
                        onclick_param = "",
                        path_image = "Modules\Assets\Images\Menu\home.png") 
        
        self._btn_pause = Button_Image(screen = self._slave, 
                        master_x = self._x,
                        master_y= self._y,
                        x = self._w - 150,
                        y = self._h - 50,
                        w = 30,
                        h = 30,
                        onclick = self.btn_pause_click,
                        onclick_param = "",
                        path_image = "Modules\Assets\Images\Menu\home.png") 
        
        self.lista_widgets.append(self.nivel)
        self.lista_widgets.append(self._btn_home)
        self.lista_widgets.append(self._btn_pause)

    def render(self):
        self._slave.fill(self._color_background)

    def update(self, events):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(events)
                # self.update_volumen(lista_eventos)   
        else:
            self.hijo.update(events)
        # if not self.nivel.pause:
        # for widget in self.lista_widgets:
        #     widget.update(events)
        # self.draw()



    def btn_home_click(self, param):
        del self.nivel
        self.end_dialog()
    
    def btn_pause_click(self, param):
      self.nivel.pause = True

      if self.nivel.pause:
        print("Pause")
        menu_options = FormMenuPause(self._master, 
        x= 200, 
        y= 25, 
        w= 400, 
        h= 400, 
        color_background = EColors.WHITE.value, 
        color_border = EColors.WHITE.value, 
        active = True, 
        path_image = "Modules\Assets\Images\Menu\window.png")

        self.show_dialog(menu_options)
          
 