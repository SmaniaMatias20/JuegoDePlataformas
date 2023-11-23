from Modules.Characters.Object import Object
from Modules.Values.Assets import *


class Item(Object):

    def __init__(self, size, position=(0,0), tipo = "Coin") -> None:

        # self.image = self.load_image(PLATFORM_IMAGE, size)
        if tipo == "Coin":
            super().__init__(size, position, COIN)
        else:
            super().__init__(size, position, COIN)   # Otra imagen 