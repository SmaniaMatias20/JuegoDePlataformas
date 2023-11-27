from Modules.Characters.Object import Object
from Modules.Values.Assets import *



class Platform(Object):

    def __init__(self, size, position=(0,0), type = "One") -> None:

        if type == "One":
            super().__init__(size, position, PLATFORM_IMAGE)
        
    def update(self, screen, platforms):
        super().update()
        self.blit_platforms(screen, platforms)


    def blit_platforms(self, screen, platforms):
        for platform in platforms:
            platform.blit(screen)
    

                 

