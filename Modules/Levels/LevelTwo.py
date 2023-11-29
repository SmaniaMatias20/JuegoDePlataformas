from Modules.Characters.Enemy import Enemy
from Modules.Characters.FallingObject import FallingObject
from Modules.Characters.Item import Item
from Modules.Characters.Trap import Trap
from Modules.Levels.LevelConfig import LevelConfig
from Modules.Characters.Platform import Platform
from Modules.Values.Assets import *
from Modules.Characters.Hero import *
from Modules.Values.Assets import *
from Modules.Values.EColors import *
from Modules.Levels.LevelOne import *

class LevelTwo(LevelConfig):
    def __init__(self, size):
        """
        Brief: Inicializa un objeto de la clase LevelTwo.

        Descripción:
            Este método inicializa un objeto de la clase LevelTwo, que representa el segundo nivel del juego.
            Configura el tamaño, tipo, fondo, enemigos, plataformas, objetos, héroe, trampas, objetos que caen y música del nivel.

        Parámetros:
            - size (tuple): Una tupla que especifica el tamaño del nivel.

        Retorno:
            Ninguno
        """
        super().__init__(size)
        self.type = "Level Two"
        self.set_background_image(BACKGROUND_IMAGE)
        self.set_enemys()
        self.set_platforms()
        self.set_items()
        self.set_hero()
        self.set_traps()
        self.set_falling_objects()  
        self.pressed_keys = []
        self.set_music(GAME_SOUND)

    def update(self, list_events):
        """
        Brief: Actualiza el estado del nivel.

        Descripción:
            Este método actualiza el estado del nivel, incluyendo la actualización de plataformas,
            objetos, trampas, enemigos, objetos que caen, héroe y la visualización de información
            como la puntuación, la caja de colisiones y el tiempo restante.

        Parámetros:
            - list_events (list): Lista de eventos que afectan el estado del nivel.

        Retorno:
            Ninguno
        """
        super().update(list_events)

        for platform in self.platforms:
            platform.update(self.screen, self.platforms)

        for item in self.items:
            item.update(self.screen, self.items)

        for trap in self.traps:
            trap.update(self.screen, self.traps)

        for enemy in self.enemys:
            enemy.update(self.screen)

        self.hero.update(self.screen, self.pressed_keys, self.platforms, self.items, self.enemys, self.traps, self.falling_objects)
        self.blit_falling_objects()
        self.show_score(f"{self.hero.points}")
        self.draw_hitbox()
        self.show_time()
        self.complete = self.hero.level_complete
        
    def set_falling_objects(self):
        """
        Brief: Configura objetos que caen en el nivel.

        Descripción:
            Este método configura los objetos que caen en el nivel mediante la creación de una lista
            de objetos que caen. La cantidad de objetos que caen se especifica como un parámetro.

        Parámetros:
            Ninguno

        Retorno:
            Ninguno
        """
        self.falling_objects = self.create_list_falling_objects(5)

    def set_platforms(self):
        """
        Brief: Configura las plataformas en el nivel.

        Descripción:
            Este método configura las plataformas en el nivel mediante la creación de una lista
            de plataformas.

        Parámetros:
            Ninguno

        Retorno:
            Ninguno
        """
        self.platforms = self.create_list_platforms() 
    
    def set_enemys(self):
        """
        Brief: Configura enemigos en el nivel.

        Descripción:
            Este método configura los enemigos en el nivel mediante la creación de una lista
            de enemigos.

        Parámetros:
            Ninguno

        Retorno:
            Ninguno
        """
        self.enemys = self.create_list_enemys()
    
    def set_items(self):
        """
        Brief: Configura items en el nivel.

        Descripción:
            Este método configura los items en el nivel mediante la creación de una lista
            de items.

        Parámetros:
            Ninguno

        Retorno:
            Ninguno
        """
        self.items = self.create_list_items()
    
    def set_traps(self):
        """
        Brief: Configura trampas en el nivel.

        Descripción:
            Este método configura las trampas en el nivel mediante la creación de una lista
            de trampas.

        Parámetros:
            Ninguno

        Retorno:
            Ninguno
        """
        self.traps = self.create_list_traps()
    
    def set_hero(self):
        """
        Brief: Configura al héroe del juego.

        Descripción:
            Este método configura al héroe del juego, definiendo su posición inicial
            y otros atributos como tamaño y velocidad.

        Parámetros:
            Ninguno

        Retorno:
            Ninguno
        """
        x = self.size[0] * 0
        y = self.size[1] - 105

        self.hero = Hero((50, 50), (x, y), 7)

    def blit_falling_objects(self):
        """
        Brief: Muestra y actualiza la posición de objetos que caen en la pantalla.

        Descripción:
            Este método mueve hacia abajo y muestra en la pantalla cada objeto que cae en el nivel.

        Parámetros:
            Ninguno

        Retorno:
            Ninguno
        """
        for fo in self.falling_objects:
            fo.move_down()
            fo.blit(self.screen)

    def create_list_platforms(self):
        """
        Brief: Crea y retorna una lista de plataformas.

        Descripción:
            Este método crea una lista de plataformas con configuraciones predefinidas
            y la retorna.

        Parámetros:
            Ninguno

        Retorno:
            list: Lista de objetos de la clase Platform.
        """
        list = []

        platform = Platform((800, 56), (0, 445))
        platform_b = Platform((800, 56), (0, 0))
        platform_c = Platform((300, 50), (225, 325))
        platform_d = Platform((300, 50), (50, 200))
        platform_e = Platform((300, 50), (440, 200))

        list.append(platform)
        list.append(platform_b)
        list.append(platform_c)
        list.append(platform_d)
        list.append(platform_e)
  
        
        return list
    
    def create_list_enemys(self):
        """
        Brief: Crea y retorna una lista de enemigos.

        Descripción:
            Este método crea una lista de enemigos con configuraciones predefinidas
            y la retorna.

        Parámetros:
            Ninguno

        Retorno:
            list: Lista de objetos de la clase Enemy.
        """
        list = []

        enemy = Enemy((40, 50), (250, 520), (350, 397), 3)
        enemy_b = Enemy((40, 50), (250, 475), (300, 277), 3)
        enemy_c = Enemy((40, 50), (500, 660), (500, 150), 3)
        enemy_d = Enemy((40, 50), (60, 150), (60, 150), 3)
    
        list.append(enemy)
        list.append(enemy_b)
        list.append(enemy_c)
        list.append(enemy_d)

        return list

    def create_list_items(self):
        """
        Brief: Crea y retorna una lista de items en el nivel.

        Descripción:
            Este método crea una lista de items (por ejemplo, monedas y coronas) con configuraciones
            predefinidas y la retorna.

        Parámetros:
            Ninguno

        Retorno:
            list: Lista de objetos de la clase Item.
        """
        list = []
        x = 0 
        
        for i in range(10):
            coin = Item((20, 20), (x + 230, 380), "Coin")
            coin_b = Item((20, 20),(x + 230, 300), "Coin")
            coin_c = Item((20, 20),(x + 50, 130), "Coin")
            coin_d = Item((20, 20),(x + 440, 170), "Coin")
            coin_e = Item((20, 20),(x + 440, 260), "Coin")
            x += 30
            list.append(coin)
            list.append(coin_b)
            list.append(coin_c)
            list.append(coin_d)
            list.append(coin_e)
        
        crown = Item((50, 40), (735, 380), "Crown")
        gem = Item((30, 30), (580, 100), "Gem")
        

        list.append(crown)
        list.append(gem)

        return list
    
    def create_list_traps(self):
        """
        Brief: Crea y retorna una lista de trampas en el nivel.

        Descripción:
            Este método crea una lista de trampas con configuraciones predefinidas
            y la retorna.

        Parámetros:
            Ninguno

        Retorno:
            list: Lista de objetos de la clase Trap.
        """
        list = []

        trap = Trap((60, 20), (170, 180), "One")
        trap_b = Trap((60, 20), (540, 425), "One")
        trap_c = Trap((60, 20), (600, 425), "One")
        trap_d = Trap((60, 20), (660, 425), "One")
 

        list.append(trap)
        list.append(trap_b)
        list.append(trap_c)
        list.append(trap_d)

        return list
    
    def create_list_falling_objects(self, size):
        """
        Brief: Crea y retorna una lista de objetos que caen en el nivel.

        Descripción:
            Este método crea una lista de objetos que caen (por ejemplo, piedras y estrellas) con
            configuraciones predefinidas y la retorna.

        Parámetros:
            - size (int): El tamaño de la lista de objetos que caen.

        Retorno:
            list: Lista de objetos de la clase FallingObject.
        """
        list = []

        for i in range(size):
            falling_object = FallingObject((20, 20), (0, 0), "Stone")
            list.append(falling_object)
        
        
        for j in range(2):
            star = FallingObject((30, 30), (0, 0), "Star")
            list.append(star)

        return list

    