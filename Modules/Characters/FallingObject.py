from Modules.Characters.Object import Object
from Modules.Values.Assets import *
import random

class FallingObject(Object):
    def __init__(self, size_surface, position, type= "Stone") -> None:

        self.type = type

        if self.type == "Stone":
            path = STONE
            # super().__init__(size_surface, position, STONE)
        elif self.type == "Star":
            path = STAR
            # super().__init__(size_surface, position, STAR)
        
        super().__init__(size_surface, position, path)

        self.set_random_position()
        speed = random.randrange(3, 7)
        self.set_speed(speed)


    def move_down(self):
        if self.rect_main.y > 500:
            self.set_random_position()
        else:
            super().move_down()
            
        self.all_rects()

    def set_random_position(self):        
        self.rect_main.x = random.randrange(self.rect_main.width, 800 - self.rect_main.width)
        self.rect_main.y = random.randrange(-100, -40)