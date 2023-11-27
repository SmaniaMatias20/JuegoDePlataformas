from Modules.Characters.Object import Object
from Modules.Values.Assets import *



class Trap(Object):

    def __init__(self, size, position=(0,0), type = "One") -> None:

        if type == "One":
            super().__init__(size, position, TRAP_ONE)
        elif type == "Two":
            super().__init__(size, position, TRAP_TWO)
    
    def update(self, screen, traps):
        self.blit_traps(screen, traps)

    def blit_traps(self, screen, traps):
        for trap in traps:
            trap.blit(screen)