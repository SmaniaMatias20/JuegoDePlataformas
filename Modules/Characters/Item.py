from Modules.Characters.Object import Object
from Modules.Values.Assets import *


class Item(Object):

    def __init__(self, size, position=(0,0), type = "Coin") -> None:

        self.type = type

        if self.type == "Coin":
            super().__init__(size, position, COIN)
        elif self.type == "Crown":
            super().__init__(size, position, CROWN)  