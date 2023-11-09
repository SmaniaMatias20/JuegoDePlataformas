import pygame as py
from Modules.Gui.GUI_form_main import FormMain
from Modules.Levels.Level import Level 
from Modules.Levels.LevelOne import LevelOne
from Modules.Levels.LevelTwo import LevelTwo
from Modules.Values.Assets import *
from Modules.Values.EColors import EColors


py.init()

W,H = 1900, 900
TAMAÑO = (W,H)
FPS = 60
RELOJ = py.time.Clock()
PANTALLA = py.display.set_mode(TAMAÑO)


nivel_actual = LevelOne((800, 500), 60)
# form_principal = FormMain(PANTALLA, 500, 250 , 900, 350, EColors.ROJO.value, EColors.AGUA.value, 5, True) # Meterlo en la clase level

bandera = True
while bandera: 
    # RELOJ.tick(FPS)
    events = py.event.get()
    for event in events:
                if event.type == py.QUIT:
                    bandera = False

    nivel_actual.clock.tick(nivel_actual.FPS)


    # form_principal.update(events)

    nivel_actual.update(events)
    # nivel_actual.get_pressed()


    py.display.flip()

py.quit()




"""
- Clase Nivel
- Nivel 1
- Nivel 2
- Nivel 3
- Manejador de Niveles
- Conexion con interfaz grafica.      



"""

