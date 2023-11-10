
from Modules.Gui.GUI_button_image import *
from Modules.Gui.GUI_form import *
from Modules.Values.EColors import *

class FormContainerLevel(Form):
    def __init__(self, screen: pygame.Surface, nivel):
        super().__init__(screen, 0, 0, screen.get_width(), screen.get_height(), color_background = EColors.ALICE_BLUE.value)
        nivel.screen = self._slave
        self.nivel = nivel

        self._btn_home = Button_Image(screen = self._slave, 
                        master_x = self._x,
                        master_y= self._y,
                        x = self._w - 100,
                        y = self._h - 100,
                        w = 50,
                        h = 50,
                        onclick = self.btn_home_click,
                        onclick_param = "",
                        path_image = "Modules\Assets\Images\Menu\home.png") 
        
        self.lista_widgets.append(self.nivel)
        self.lista_widgets.append(self._btn_home)

    def update(self, events):
        self.nivel.update(events)
        for widget in self.lista_widgets:
            widget.update(events)
        self.draw()

    def btn_home_click(self, param):
        del self.nivel
        self.end_dialog()