from Modules.Characters.Object import Object
from Modules.Values.Assets import *
import pygame as py




class Projectile(Object):
    def __init__(self, size, direction, position=(0,0), type="One"):
        """
        Brief: Constructor de la clase Projectile.

        Descripción:
            Inicializa un objeto de la clase Projectile con los parámetros proporcionados.

        Parámetros:
            size (tuple): Tamaño del proyectil.
            direction (str): Dirección del proyectil ("Left" o "Right").
            position (tuple, opcional): Posición inicial del proyectil. Por defecto, (0, 0).
            type (str, opcional): Tipo de proyectil ("One" o "Fire"). Por defecto, "One".

        Retorno:
            Ninguno
        """
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
        """
        Brief: Actualiza la posición del proyectil.

        Descripción:
            Este método actualiza la posición del proyectil según su dirección y tipo.

        Parámetros:
            Ninguno

        Retorno:
            Ninguno
        """
        if self.type == "One":
            if self.direction == "Right":
                self.rect_main.x += self.speed    
            elif self.direction == "Left":
                self.rect_main.x -= self.speed
        else:
            if self.direction == "Quiet":
                self.rect_main.x -= self.speed
        
        self.all_rects()
        

            


