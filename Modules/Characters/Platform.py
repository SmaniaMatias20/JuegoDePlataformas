from Modules.Characters.Object import Object
from Modules.Values.Assets import *



class Platform(Object):

    def __init__(self, size, position=(0,0), type = "One") -> None:


        if type == "One":
            super().__init__(size, position, PLATFORM_IMAGE)
        # else:
        #     super().__init__(size, position, PLATFORM_IMAGE)   # Otra imagen de Plataforma

    
