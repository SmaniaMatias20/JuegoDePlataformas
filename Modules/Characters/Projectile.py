from Modules.Characters.Object import Object
from Modules.Values.Assets import *
import pygame as py



class Projectile(Object):
    def __init__(self, size, direction, position=(0,0)):
        self.current_animation = self.load_image(PROJECTILE, size)
        if direction == "Left":
            self.current_animation = py.transform.flip(self.current_animation,True,False)
            
        super().__init__(size, position, self.current_animation) # Imagen de la flecha
        self.direction = direction
        self.speed = 10
            
    
    def update(self):
        if self.direction == "Right" or self.direction == "Quiet":
           self.rect_main.x += self.speed
        elif self.direction == "Left":
            self.rect_main.x -= self.speed
