from Modules.Characters.Object import Object
from Modules.Characters.Platform import Platform
from Modules.Values.Assets import *
import pygame as py




class Projectile(Object):
    def __init__(self, size, direction, position=(0,0), type="One"):
        self.type = type
        
        if self.type == "One":
            self.current_animation = self.load_image(PROJECTILE, size)
            if direction == "Left":
                self.current_animation = py.transform.flip(self.current_animation,True,False)
                
            super().__init__(size, position, self.current_animation) 
            self.direction = direction
            self.set_speed(7)
        else:
            self.current_animation = self.load_image(FIRE, size)
            
            super().__init__(size, position, self.current_animation) 
            self.direction = direction
            self.set_speed(7)
            
    
    def update(self):
        if self.type == "One":
            if self.direction == "Right":
                self.rect_main.x += self.speed      #Cambiar por super
            elif self.direction == "Left":
                self.rect_main.x -= self.speed
        else:
            if self.direction == "Quiet":
                self.rect_main.x -= self.speed
        
        self.all_rects()
        

            


