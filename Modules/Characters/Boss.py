from Modules.Characters.Platform import *
from Modules.Characters.Object import Object
from Modules.Characters.Projectile import Projectile
from Modules.Values.Assets import *


class Boss(Object):
    def __init__(self, size, move_position, position=(0,0), speed=3):
        """
        Brief: Constructor de la clase Boss.

        Descripción:
            Inicializa un objeto Boss con parámetros específicos, incluyendo tamaño, vidas, posición inicial,
            posición de movimiento, velocidad, animaciones, estado, contador de pasos, estado de muerte, velocidad
            de movimiento, tiempo de la última actualización, indicador de disparo y tiempo del último disparo.

        Parámetros:
            - size (tuple): Tamaño del objeto Boss.
            - move_position (tuple): Posición a la que se moverá el Boss.
            - position (tuple, opcional): Posición inicial del Boss. Por defecto, (0, 0).
            - speed (int, opcional): Velocidad de movimiento del Boss. Por defecto, 3.

        Retorno:
            Ninguno
        """
        self.size = size
        self.lives = 5
        self.move_position = move_position
        self.animations = self.set_animations()
        self.state = "Left"
        self.current_animation = self.animations[self.state]
        self.step_counter = 0
        self.dead = False
        self.set_speed(speed)
        self.time_last = 0
        self.flag_shot = False
        self.time_last_shot = 0
        self.list_projectiles = []  
        super().__init__(size, position, self.current_animation[self.step_counter]) 

    def update(self, screen):
        """
        Brief: Actualiza el estado del Boss.

        Descripción:
            Este método actualiza el estado del objeto Boss, incluyendo su movimiento, animación y
            actualización de proyectiles.

        Parámetros:
            - screen: Superficie de la pantalla en la que se renderiza el juego.

        Retorno:
            Ninguno
        """

        super().update()
        self.move_boss()
        self.animation(screen)
        self.update_projectile(screen)

    def shot_projectile(self):
        """
        Brief: Dispara un proyectil desde el Boss.

        Descripción:
            Este método determina la posición de disparo del proyectil en función del estado actual
            del Boss. Si el estado es "Quiet", el proyectil se dispara desde el lado derecho del Boss.
            Después de disparar el proyectil, se agrega a la lista de proyectiles del Boss y se reproduce
            un efecto de sonido de disparo.

        Parámetros:
            Ninguno

        Retorno:
            Ninguno
        """
        x = None
        margin = 50
        y = self.rect_main.centery - 10
        if self.state == "Quiet":
            x = self.rect_main.right - margin

        if x is not None:
            self.list_projectiles.append(Projectile((50, 50), self.state, (x, y),"Two"))
            self.sound_effects(FIRE_SOUND, 0.1)

    def update_projectile(self, screen: py.Surface):
        """
        Brief: Actualiza y muestra los proyectiles del Boss en la pantalla.

        Descripción:
            Este método itera a través de la lista de proyectiles del Boss, actualiza su posición
            y los muestra en la pantalla. Si un proyectil sale de los límites de la pantalla, se
            elimina de la lista.

        Parámetros:
            - screen (py.Surface): Superficie de la pantalla en la que se renderizan los proyectiles.

        Retorno:
            Ninguno
        """
        indice = 0
        while indice < len(self.list_projectiles):
            projectile = self.list_projectiles[indice]
            screen.blit(projectile.image, projectile.rect_main)
            projectile.update()
            
            if projectile.rect_main.centerx < 0 or projectile.rect_main.centerx > screen.get_width():
                self.list_projectiles.pop(indice)
                indice -= 1
            indice +=1

    
    def move_boss(self): 
        """
        Brief: Controla el movimiento y el estado del Boss.

        Descripción:
            Este método determina y controla el movimiento y estado del Boss según su estado actual.
            Si el Boss está en estado "Left", se mueve hacia la izquierda hasta alcanzar la posición de
            movimiento. Luego cambia al estado "Right" y se mueve hacia la derecha hasta alcanzar otra posición.
            Después cambia al estado "Quiet" y permanece inmóvil por un tiempo antes de volver al estado "Left".
            Además, el Boss dispara proyectiles periódicamente si no está en el estado de disparo.

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
                self.state = "Quiet"
        elif self.state == "Quiet":
            time = py.time.get_ticks()
            self.current_animation = self.animations[self.state]
            if time - self.time_last >= 15000:
                self.state = "Left" 
                self.time_last = time

        if not self.flag_shot:
            time_shot = py.time.get_ticks()
            if time_shot - self.time_last_shot >= 2000:
               
                self.shot_projectile() 
                self.time_last_shot = time_shot

    def set_animations(self):
        """
        Brief: Configura las animaciones del Boss.

        Descripción:
            Este método carga las imágenes necesarias para las animaciones del Boss, incluyendo las animaciones
            de quieto, caminata hacia la derecha y caminata hacia la izquierda. Las animaciones se almacenan
            en un diccionario con claves correspondientes a los estados del Boss.

        Parámetros:
            Ninguno

        Retorno:
            dict: Diccionario de animaciones con claves "Quiet", "Right" y "Left".
        """
        boss_walk_right = []
        boss_quiet = []

        list_path_quiet = [BOSS_QUIET_A,BOSS_QUIET_A,BOSS_QUIET_A,BOSS_QUIET_A, BOSS_QUIET_A,BOSS_QUIET_A,BOSS_QUIET_B,BOSS_QUIET_B,BOSS_QUIET_B,BOSS_QUIET_B,BOSS_QUIET_B,BOSS_QUIET_B,BOSS_QUIET_C,BOSS_QUIET_C,BOSS_QUIET_C,BOSS_QUIET_C,BOSS_QUIET_C,BOSS_QUIET_C,BOSS_QUIET_C,BOSS_QUIET_C,BOSS_QUIET_C,BOSS_QUIET_C,BOSS_QUIET_C,BOSS_QUIET_C]

        list_path_walk = [BOSS_WALK_RIGHT_A,BOSS_WALK_RIGHT_A,BOSS_WALK_RIGHT_B,BOSS_WALK_RIGHT_B,BOSS_WALK_RIGHT_C,BOSS_WALK_RIGHT_C,BOSS_WALK_RIGHT_D,BOSS_WALK_RIGHT_D,BOSS_WALK_RIGHT_E,BOSS_WALK_RIGHT_E,BOSS_WALK_RIGHT_F,BOSS_WALK_RIGHT_F,BOSS_WALK_RIGHT_G,BOSS_WALK_RIGHT_G,BOSS_WALK_RIGHT_H,BOSS_WALK_RIGHT_H,BOSS_WALK_RIGHT_I,
        BOSS_WALK_RIGHT_I]
        
        for path in list_path_walk:
            image_boss_walk_right = self.load_image(path, self.size) 
            boss_walk_right.append(image_boss_walk_right)
        
        for path in list_path_quiet:
            image_boss_path = self.load_image(path, self.size)
            boss_quiet.append(image_boss_path)

        animations = {}
        animations["Quiet"] = boss_quiet
        animations["Right"] = boss_walk_right
        animations["Left"]  = flip_images(boss_walk_right)

        return animations
    
    def animation(self, screen: py.Surface):
        """
        Brief: Realiza la animación del Boss en la pantalla.

        Descripción:
            Este método realiza la animación del Boss en la pantalla, mostrando la imagen correspondiente
            al paso actual en la animación. El método controla el contador de pasos para avanzar a la siguiente
            imagen en la secuencia.

        Parámetros:
            - screen (py.Surface): Superficie de la pantalla en la que se renderiza la animación.

        Retorno:
            Ninguno
        """
        long = len(self.current_animation)
        if self.step_counter >= long:
            self.step_counter = 0
        
        screen.blit(self.current_animation[self.step_counter], self.rect_main)
        self.step_counter += 1
