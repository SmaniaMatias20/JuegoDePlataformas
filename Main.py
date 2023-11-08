from Modules.Game import *
from Modules.Levels.LevelOne import LevelOne
from Modules.Levels.LevelTwo import LevelTwo

nivel_actual = LevelOne((800, 500), 60)

py.init()

while nivel_actual.running: 
    
    nivel_actual.clock.tick(nivel_actual.FPS)

    events = py.event.get()

    nivel_actual.update(events)
    nivel_actual.get_pressed()

    
    
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

