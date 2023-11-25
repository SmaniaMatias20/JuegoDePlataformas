from Modules.Characters.Object import Object
from Modules.Values.Assets import *



class Platform(Object):

    def __init__(self, size, position=(0,0), type = "One") -> None:

        # self.image = self.load_image(PLATFORM_IMAGE, size)
        if type == "One":
            super().__init__(size, position, PLATFORM_IMAGE)
        else:
            super().__init__(size, position, PLATFORM_IMAGE)   # Otra imagen de Plataforma

    
    

    # @staticmethod
    # def create_list():
    #     list = []

    #     platform = Platform((800, 56), (0, 445))
    #     platform_b = Platform((800, 56), (0, 0))
    #     platform_c = Platform((75,30), (100, 350))

    #     list.append(platform)
    #     list.append(platform_b)
    #     list.append(platform_c)
        
    #     return list