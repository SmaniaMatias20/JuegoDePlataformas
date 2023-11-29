from Modules.Characters.Platform import *
from Modules.Characters.Object import Object
from Modules.Values.Assets import *


class Enemy(Object):
    def __init__(self, size, move_position, position=(0,0), speed=3):
        """
        Brief: Inicializa un objeto de tipo Enemy.

        Descripción:
            Este método inicializa un objeto de tipo Enemy con un tamaño específico, posición inicial,
            velocidad y animaciones. La posición de movimiento determina la dirección hacia la cual el
            enemigo se moverá.

        Parámetros:
            - size (tuple): Tamaño del enemigo en píxeles (ancho, alto).
            - move_position (tuple): Posición límite hacia la cual se moverá el enemigo.
            - position (tuple, opcional): Posición inicial del enemigo en la pantalla. Por defecto, (0, 0).
            - speed (int, opcional): Velocidad de movimiento del enemigo. Por defecto, 3.

        Retorno:
            Ninguno
        """
        self.size = size
        self.move_position = move_position
        self.animations = self.set_animations()
        self.state = "Left"
        self.current_animation = self.animations[self.state]
        self.step_counter = 0
        self.dead = False
        self.set_speed(speed)
        super().__init__(size, position, self.current_animation[self.step_counter]) 

    def update(self, screen):
        """
        Brief: Actualiza el estado y posición del enemigo.

        Descripción:
            Este método actualiza el estado y la posición del enemigo en la pantalla. Llama a los métodos
            para mover al enemigo y realizar la animación correspondiente.

        Parámetros:
            - screen (py.Surface): Superficie de la pantalla en la que se renderiza el enemigo.

        Retorno:
            Ninguno
        """
        super().update()
        self.move_enemy()
        self.animation(screen)
        
    
    def move_enemy(self):
        """
        Brief: Mueve al enemigo en la dirección especificada.

        Descripción:
            Este método mueve al enemigo en la dirección especificada por su estado actual. Si el enemigo está
            en el estado "Left", se moverá hacia la izquierda hasta alcanzar la posición límite definida por
            move_position[0]. Si está en el estado "Right", se moverá hacia la derecha hasta alcanzar la posición
            límite definida por move_position[1].

        Parámetros:
            Ninguno

        Retorno:
            Ninguno
        """
        if self.state == "Left":
            self.current_animation = self.animations[self.state]
            super().move_left()
            if self.rect_main.x < self.move_position[0]: 
                self.state = "Right"
        elif self.state == "Right":
            self.current_animation = self.animations[self.state]
            super().move_right()
            if self.rect_main.x + 30 > self.move_position[1]:
                self.state = "Left"   


    def set_animations(self):
        """
        Brief: Establece las animaciones del enemigo.

        Descripción:
            Este método carga las imágenes necesarias para las animaciones del enemigo, tanto para el movimiento
            hacia la derecha como hacia la izquierda. Las imágenes se cargan desde los archivos especificados en
            la lista de rutas y se escalan al tamaño deseado.

        Parámetros:
            Ninguno

        Retorno:
            dict: Un diccionario que contiene las animaciones del enemigo, con claves "Right" y "Left".
        """
        enemy_walk_right = []
        list_path = [ENEMY_WALK_RIGHT_A,ENEMY_WALK_RIGHT_A,ENEMY_WALK_RIGHT_B,ENEMY_WALK_RIGHT_B,ENEMY_WALK_RIGHT_C,ENEMY_WALK_RIGHT_C, ENEMY_WALK_RIGHT_D,ENEMY_WALK_RIGHT_D,ENEMY_WALK_RIGHT_E,ENEMY_WALK_RIGHT_E,ENEMY_WALK_RIGHT_F,ENEMY_WALK_RIGHT_F,ENEMY_WALK_RIGHT_G,ENEMY_WALK_RIGHT_G,ENEMY_WALK_RIGHT_H,ENEMY_WALK_RIGHT_H]

        for path in list_path:
            image_enemy_walk_right = self.load_image(path, self.size) 
            enemy_walk_right.append(image_enemy_walk_right)

        animations = {}
        animations["Right"] = enemy_walk_right
        animations["Left"]  = flip_images(enemy_walk_right)

        return animations
    
    def animation(self, screen: py.Surface):
        """
        Brief: Realiza la animación del enemigo en la pantalla.

        Descripción:
            Este método realiza la animación del enemigo en la pantalla, mostrando la siguiente imagen de la
            animación en cada llamada. La animación se reinicia cuando alcanza su última imagen.

        Parámetros:
            - screen (py.Surface): Superficie de la pantalla en la que se renderiza el enemigo.

        Retorno:
            Ninguno
        """
        long = len(self.current_animation)
        if self.step_counter >= long:
            self.step_counter = 0
        
        screen.blit(self.current_animation[self.step_counter], self.rect_main)
        self.step_counter += 1


            

        


