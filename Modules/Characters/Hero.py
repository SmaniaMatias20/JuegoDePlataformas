import pygame as py
from Modules.Characters.Boss import Boss
from Modules.Characters.Enemy import Enemy
from Modules.Characters.FallingObject import FallingObject
from Modules.Characters.Item import Item
from Modules.Characters.Object import *
from Modules.Characters.Projectile import Projectile
from Modules.Characters.Trap import Trap
from Modules.Values.Assets import *
from Modules.Characters.Platform import *



class Hero(Object):

    def __init__(self, size, position=(0,0), speed=3) -> None:
        """
        Brief: Inicializa el objeto del héroe.

        Descripción:
            Este método inicializa el objeto del héroe con un tamaño específico, posición inicial y velocidad.
            Configura atributos como la animación, estado, contadores, poder de salto, gravedad, puntos, vidas,
            y más.

        Parámetros:
            - size (tuple): Tamaño del héroe.
            - position (tuple): Posición inicial del héroe.
            - speed (int): Velocidad del héroe (3 por defecto).

        Retorno:
            Ninguno
        """
        self.name = ""
        self.size = size
        self.animations = self.set_animations()
        self.state = "Quiet"
        self.current_animation = self.animations[self.state]
        self.step_counter = 0
        self.move_y = 0
        self.jump_power = -15
        self.jump_speed_limit = 15
        self.gravity = 1
        self.jump = False
        self.points = 0
        self.lives = 3
        self.flag_shot = False
        self.time_last_shot = 0
        self.list_projectile = []  
        self.level_complete = False
        self.set_speed(speed)
        super().__init__(size, position, self.current_animation[self.step_counter]) 

    def update(self, screen, pressed_keys, platforms, items, enemys, traps, stones, boss=None):
        """
        Brief: Actualiza el estado del héroe en el juego.

        Descripción:
            Este método actualiza el estado del héroe en el juego, gestionando su movimiento, la aplicación de gravedad,
            las colisiones con diferentes elementos del juego como plataformas, enemigos, trampas, objetos que caen,
            ítems y el jefe (si está presente). También se encarga de mostrar la cantidad de vidas del héroe en la pantalla.

        Parámetros:
            - screen (py.Surface): Superficie de la pantalla del juego.
            - pressed_keys (list): Lista que representa las teclas presionadas.
            - platforms (list): Lista de plataformas en el juego.
            - items (list): Lista de ítems en el juego.
            - enemys (list): Lista de enemigos en el juego.
            - traps (list): Lista de trampas en el juego.
            - stones (list): Lista de objetos que caen (piedras) en el juego.
            - boss (Boss): Objeto del jefe (puede ser None si no hay jefe en el nivel).

        Retorno:
            Ninguno
        """
        super().update()
        self.show_lives(screen)
        self.move_hero(screen, pressed_keys)
        self.update_projectile(screen)
        self.apply_gravity(screen, platforms)
        self.collide_with_enemys(enemys)
        self.collide_with_traps(traps)
        self.collide_with_falling_objects(stones)
        self.collide_with_items(items)
        self.collide_with_boss(boss)
        
    
    def move_hero(self, screen: py.Surface, pressed_keys):
        """
        Brief: Gestiona el movimiento y las acciones del héroe en el juego.

        Descripción:
            Este método determina el estado del héroe basado en las teclas presionadas y realiza las acciones correspondientes.
            Puede cambiar entre los estados "Quiet" (quieto), "Right" (derecha), "Left" (izquierda) y "Up" (saltando).
            Además, permite al héroe disparar proyectiles con la tecla 'F'.

        Parámetros:
            - screen (py.Surface): Superficie de la pantalla del juego.
            - pressed_keys (list): Lista que representa las teclas presionadas.

        Retorno:
            Ninguno
        """
        self.change_state(pressed_keys)

        match self.state:
            case "Quiet":
                self.current_animation = self.animations[self.state]
                self.animation(screen)
            case "Right":
                self.current_animation = self.animations[self.state]
                self.move_right(screen.get_width()) 
                self.animation(screen)
                self.flag_shot = True
            case "Left":
                self.current_animation = self.animations[self.state]
                self.move_left(0) 
                self.animation(screen)
                self.flag_shot = True
            case "Up": 
                if not self.jump: 
                    self.jump = True
                    self.move_y = self.jump_power
                    self.current_animation = self.animations[self.state]
                    self.move_up(0)
                    self.animation(screen)

        if self.flag_shot and pressed_keys[py.K_f]:
            time = py.time.get_ticks()
            if time - self.time_last_shot >= 1000:   
                self.shot_projectile() 
                self.sound_effects(PROJECTILE_SOUND, 0.2)
                self.flag_shot = False
                self.time_last_shot = time
     

    def show_lives(self, screen):
        """
        Brief: Muestra la cantidad de vidas del héroe en la pantalla.

        Descripción:
            Este método carga y muestra las imágenes correspondientes a la cantidad de vidas restantes del héroe en la esquina superior izquierda de la pantalla.

        Parámetros:
            - screen (py.Surface): Superficie de la pantalla del juego.

        Retorno:
            Ninguno
        """
        one_live = self.load_image(ONE_LIVE, (75, 30))
        two_live = self.load_image(TWO_LIVE, (75, 30))
        three_live = self.load_image(THREE_LIVE, (75, 30))

        if self.lives >= 3:
            self.lives = 3
            screen.blit(three_live, [5, 20])
        elif self.lives == 2:
            screen.blit(two_live, [5, 20])
        elif self.lives == 1:
            screen.blit(one_live, [5, 20])


    def shot_projectile(self):
        """
        Brief: Dispara un proyectil desde la posición actual del héroe.

        Descripción:
            Este método determina la posición de disparo según la dirección actual del héroe (derecha o izquierda) y crea un nuevo proyectil en esa posición. El proyectil se añade a la lista de proyectiles del héroe.

        Parámetros:
            Ninguno

        Retorno:
            Ninguno
        """
        x = None
        margin = 47
        y = self.rect_main.centery - 10
        if self.state == "Right":
            x = self.rect_main.right - margin
        elif self.state == "Left":
            x = self.rect_main.left - 50 + margin 

        if x is not None:
            self.list_projectile.append(Projectile((30, 10), self.state, (x, y)))

    def update_projectile(self, screen: py.Surface):
        """
        Brief: Actualiza y muestra los proyectiles en la pantalla.

        Descripción:
            Este método itera a través de la lista de proyectiles del héroe, actualiza la posición de cada proyectil y los muestra en la pantalla. Además, elimina los proyectiles que salen de la pantalla.

        Parámetros:
            screen (pygame.Surface): La superficie de la pantalla donde se muestran los proyectiles.

        Retorno:
            Ninguno
        """
        indice = 0
        while indice < len(self.list_projectile):
            projectile = self.list_projectile[indice]
            screen.blit(projectile.image, projectile.rect_main)
            projectile.update()
            if projectile.rect_main.centerx < 0 or projectile.rect_main.centerx > screen.get_width():
                self.list_projectile.pop(indice)
                indice -= 1
            indice +=1

    def change_state(self, pressed_keys):
        """
        Brief: Cambia el estado del héroe según las teclas presionadas.

        Descripción:
            Este método cambia el estado del héroe en función de las teclas que se presionan.

        Parámetros:
            pressed_keys (List): Lista que contiene el estado de todas las teclas del teclado.

        Retorno:
            Ninguno
        """
        if pressed_keys[py.K_RIGHT]:
            self.state = "Right"
        elif pressed_keys[py.K_LEFT]:
            self.state = "Left"
        elif pressed_keys[py.K_UP]:
            self.state = "Up"
        else:
            self.state = "Quiet"

    def set_animations(self):
        """
        Brief: Configura las animaciones del héroe.

        Descripción:
            Este método carga las imágenes necesarias para las animaciones del héroe.

        Parámetros:
            Ninguno

        Retorno:
            dict: Un diccionario que contiene listas de imágenes para diferentes estados de animación del héroe.
                Las claves del diccionario representan los estados, como "Quiet", "Right", "Left", y "Up".
        """
        hero_quiet = []
        hero_walk_right = []
        hero_jump = []  
        list_path = [HERO_WALK_RIGHT_A,HERO_WALK_RIGHT_A,HERO_WALK_RIGHT_B,HERO_WALK_RIGHT_B,HERO_WALK_RIGHT_C,HERO_WALK_RIGHT_C,HERO_WALK_RIGHT_D,HERO_WALK_RIGHT_D,HERO_WALK_RIGHT_E,HERO_WALK_RIGHT_E]

        for path in list_path:
            image_hero_walk_right = self.load_image(path, self.size) 
            hero_walk_right.append(image_hero_walk_right)

        image_hero_quiet = self.load_image(HERO_QUIET, self.size)
        image_hero_jump = self.load_image(HERO_JUMP, self.size)
        hero_quiet.append(image_hero_quiet)
        hero_jump.append(image_hero_jump)

        animations = {}
        animations["Quiet"] = hero_quiet
        animations["Right"] = hero_walk_right
        animations["Left"]  = flip_images(hero_walk_right)
        animations["Up"] = hero_jump

        return animations

    def animation(self, screen: py.Surface):
        """
        Brief: Reproduce la animación actual del objeto en la pantalla.

        Descripción:
            Este método muestra la imagen actual de la animación en la pantalla. La animación avanza a través de los frames en cada llamada al método.

        Parámetros:
            screen (py.Surface): La superficie de la pantalla donde se mostrará la animación.

        Retorno:
            Ninguno
        """
        long = len(self.current_animation)
        if self.step_counter >= long:
            self.step_counter = 0
        
        screen.blit(self.current_animation[self.step_counter], self.rect_main)
        self.step_counter += 1

    def move_right(self, top_right): 
        """
        Brief: Mueve el objeto hacia la derecha en la pantalla.

        Descripción:
            Este método desplaza el objeto hacia la derecha en la pantalla.

        Parámetros:
            top_right (int): La coordenada x máxima permitida en la pantalla.

        Retorno:
            Ninguno
        """
        new_x = self.rect_main.x + self.speed

        if new_x >= 0 and new_x <= top_right - self.rect_main.width:
            self.image = self.current_animation

            super().move_right()

    def move_left(self, top_left):
        """
        Brief: Mueve el objeto hacia la izquierda en la pantalla.

        Descripción:
            Este método desplaza el objeto hacia la izquierda en la pantalla. 

        Parámetros:
            top_left (int): La coordenada X mínima permitida en la pantalla.

        Retorno:
            Ninguno
        """
        new_x = self.rect_main.x - self.speed

        if new_x >= top_left:
            self.image = self.current_animation

            super().move_left()

    def move_up(self, top_up):
        """
        Brief: Mueve el objeto hacia arriba en la pantalla.

        Descripción:
            Este método desplaza el objeto hacia arriba en la pantalla. 

        Parámetros:
            top_up (int): La coordenada Y mínima permitida en la pantalla.

        Retorno:
            Ninguno
        """
        new_y = self.rect_main.y - self.speed

        if new_y >= top_up:
            self.image = self.current_animation

            super().move_up()

    def apply_gravity(self, screen, platforms: list["Platform"]):
        """
        Brief: Aplica la gravedad al objeto y maneja las colisiones con las plataformas.

        Descripción:
            Este método aplica la gravedad al objeto si no está en un salto y maneja las colisiones con las plataformas para evitar que el objeto atraviese el suelo o el techo.

        Parámetros:
            screen (py.Surface): La superficie de la pantalla donde se dibuja el objeto.
            platforms (list[Platform]): Una lista de objetos de tipo "Platform" con los que se verifican las colisiones.

        Retorno:
            Ninguno
        """
        if self.jump:
            self.animation(screen)
            self.rect_main.y += self.move_y
            if self.move_y + self.gravity < self.jump_speed_limit:
                self.move_y += self.gravity
            
        for pl in platforms:
            if self.rect_main.colliderect(pl.rect_main):
                if self.move_y > 0:  
                    self.move_y = 0
                    self.jump = False
                    self.rect_main.bottom = pl.rect_main.top
                elif self.move_y < 0: 
                    self.move_y = 0
                    self.rect_main.top = pl.rect_main.bottom
                break
            else:
                self.jump = True

    def collide_with_boss(self, boss: Boss):
        """
        Brief: Maneja las colisiones entre el héroe y el jefe.

        Descripción:
            Este método verifica las colisiones entre el héroe y los proyectiles y el jefe (boss).

        Parámetros:
            boss (Boss): El objeto del jefe contra el cual se verifican las colisiones.

        Retorno:
            Ninguno
        """
        try:
            for fire in boss.list_projectiles:
                if fire.rect_main.colliderect(self.rect_main) or self.rect_main.colliderect(boss.rect_main):
                    self.sound_effects(SCREAM_SOUND, 0.2)
                    boss.list_projectiles.remove(fire)
                    self.lives -= 1 
                    self.rect_main.x = 0
                    self.rect_main.y = 400 

            self.kill_boss(boss)
        except AttributeError:
            pass
        except Exception:
            pass



    def collide_with_items(self, items:list['Item']):
        """
        Brief: Maneja las colisiones entre el héroe y los elementos (items) en el juego.

        Descripción:
            Este método verifica las colisiones entre el héroe y los elementos en el juego (por ejemplo, monedas, gemas, etc.).

        Parámetros:
            items (list): La lista de elementos en el juego.

        Retorno:
            Ninguno
        """
        indice = 0
        while indice < len(items):
            if self.rect_main.colliderect(items[indice].rect_main):
                if items[indice].type == "Coin":
                    self.points += 25
                    items.pop(indice)
                    self.sound_effects(COIN_SOUND, 0.2)
                    indice -= 1
                elif items[indice].type == "Gem":
                    self.points += 100
                    items.pop(indice)
                    self.sound_effects(GEM_SOUND, 0.3) # Cambiar por sonido de gema
                    indice -= 1
                else:
                    self.points += 100
                    items.pop(indice)
                    indice -= 1
                    self.level_complete = True
            indice +=1
    
    def collide_with_traps(self, traps:list['Trap']):
        """
        Brief: Maneja las colisiones entre el héroe y las trampas en el juego.

        Descripción:
            Este método verifica las colisiones entre el héroe y las trampas en el juego. Si hay una colisión, se reproducen efectos de sonido correspondientes y se reduce la vida del héroe. Además, la posición del héroe se reinicia a un valor predeterminado.

        Parámetros:
            traps (list): La lista de trampas en el juego.

        Retorno:
            Ninguno
        """
        indice = 0
        while indice < len(traps):
            if self.rect_main.colliderect(traps[indice].rect_main):
                self.sound_effects(TRAP_SOUND, 0.3)
                self.lives -= 1
                self.rect_main.x = 0
                self.rect_main.y = 400
                break
            indice +=1

    def collide_with_falling_objects(self, objects:list['FallingObject']):
        """
        Brief: Maneja las colisiones entre el héroe y los objetos que caen en el juego.

        Descripción:
            Este método verifica las colisiones entre el héroe y los objetos que caen en el juego. Si hay una colisión con una piedra, se reproducen efectos de sonido y se reduce la vida del héroe. Si hay una colisión con una estrella, se reproduce un efecto de sonido y se incrementa la vida del héroe.

        Parámetros:
            objects (list): La lista de objetos que caen en el juego.

        Retorno:
            Ninguno
        """
        indice = 0
        while indice < len(objects):
            if self.rect["top"].colliderect(objects[indice].rect_main):
                if objects[indice].type == "Stone":
                    self.sound_effects(BANG_SOUND, 0.1)
                    self.lives -= 1
                    self.rect_main.x = 0
                    self.rect_main.y = 400
                    objects.pop(indice)
                    indice -= 1
                elif objects[indice].type == "Star" and self.lives < 3:
                    self.sound_effects(STAR_SOUND, 0.2)
                    self.lives += 1
                    objects.pop(indice)
                    indice -= 1
            indice +=1


    def collide_with_enemys(self, enemys:list['Enemy']):
        """
        Brief: Maneja las colisiones entre el héroe y los enemigos en el juego.

        Descripción:
            Este método verifica las colisiones entre el héroe y los enemigos en el juego. Si hay una colisión, se reduce la vida del héroe y lo devuelve a una posición predeterminada.

        Parámetros:
            enemys (list): La lista de enemigos en el juego.

        Retorno:
            Ninguno
        """
        indice = 0
        while indice < len(enemys):
            if self.rect_main.colliderect(enemys[indice].rect_main):
                self.sound_effects(SCREAM_SOUND, 0.2)
                self.lives -= 1
                self.rect_main.x = 0
                self.rect_main.y = 400
                break
            indice +=1
        
        self.kill_enemy(enemys)
    
    def kill_enemy(self, enemys:list['Enemy']):
        """
        Brief: Maneja la eliminación de enemigos cuando son alcanzados por proyectiles.

        Descripción:
            Este método se encarga de verificar si los proyectiles del héroe han alcanzado a los enemigos. Si es así, reproduce un sonido, elimina el proyectil y el enemigo, y otorga puntos al héroe.

        Parámetros:
            enemys (list): La lista de enemigos en el juego.

        Retorno:
            Ninguno
        """
        for projectile in self.list_projectile:
            for enemy in enemys:
                if projectile.rect_main.colliderect(enemy.rect_main):
                    self.sound_effects(BANG_SOUND, 0.1)
                    self.list_projectile.remove(projectile)
                    self.points += 50
                    enemys.remove(enemy)
                    del enemy
    
    def kill_boss(self, boss:Boss):
        """
        Brief: Maneja la eliminación del jefe cuando es alcanzado por proyectiles.

        Descripción:
            Este método se encarga de verificar si los proyectiles del héroe han alcanzado al jefe. Si es así, reproduce un sonido, elimina el proyectil, reduce la vida del jefe y otorga puntos al héroe si la vida del jefe llega a cero.

        Parámetros:
            boss (Boss): Instancia del jefe en el juego.

        Retorno:
            Ninguno
        """
        try:
            for projectile in self.list_projectile:
                if projectile.rect_main.colliderect(boss.rect_main):
                    self.sound_effects(BANG_SOUND, 0.1)
                    self.list_projectile.remove(projectile)
                    boss.lives -= 1
                    if boss.lives == 0:
                        self.points += 300
                        del boss
        except UnboundLocalError as e:
            print(f"Error: {e}") 
        except Exception as exc:
            print(f"Error: {exc}")




