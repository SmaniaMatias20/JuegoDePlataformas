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

    def update(self, list_events):
        super().update(list_events)

        for platform in self.platforms:
            platform.update(self.screen, self.platforms)

        for item in self.items:
            item.update(self.screen, self.items)

        for trap in self.traps:
            trap.update(self.screen, self.traps)

        for enemy in self.enemys:
            enemy.update(self.screen)

        self.blit_falling_objects()
        self.hero.update(self.screen, self.pressed_keys, self.platforms, self.items, self.enemys, self.traps, self.falling_objects)
        self.show_score(f"{self.hero.points}")
        self.draw_hitbox()
        self.show_time()
        self.complete = self.hero.level_complete
        
    def set_falling_objects(self):
        self.falling_objects = self.create_list_falling_objects(5)

    def set_platforms(self):
        self.platforms = self.create_list_platforms() 
    
    def set_enemys(self):
        self.enemys = self.create_list_enemys()
    
    def set_items(self):
        self.items = self.create_list_items()
    
    def set_traps(self):
        self.traps = self.create_list_traps()
    
    def set_hero(self):
        x = self.size[0] * 0
        y = self.size[1] - 105

        self.hero = Hero((50, 50), (x, y), 7)

    def blit_falling_objects(self):
        for fo in self.falling_objects:
            fo.move_down()
            fo.blit(self.screen)

    def create_list_platforms(self):
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
        list = []

        for i in range(size):
            falling_object = FallingObject((20, 20), (0, 0), "Stone")
            list.append(falling_object)
        
        
        for j in range(2):
            star = FallingObject((30, 30), (0, 0), "Star")
            list.append(star)

        return list

    