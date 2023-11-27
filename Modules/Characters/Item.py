from Modules.Characters.Object import Object
from Modules.Values.Assets import *


class Item(Object):

    def __init__(self, size, position=(0,0), type = "Coin") -> None:
        self.type = type
        if self.type == "Coin":
            path = COIN
        elif self.type == "Crown":
            path = CROWN
        elif self.type == "Gem":
            path = GEM
            
        super().__init__(size, position, path)
        

    def update(self, screen, items):
        self.blit_platforms(screen, items)

    def blit_platforms(self, screen, items):
        for item in items:
            item.blit(screen)