from Modules.Characters.Boss import Boss
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

class LevelThree(LevelConfig):
    def __init__(self, size):
        super().__init__(size)
        self.type = "Level Three"
        self.set_background_image(BACKGROUND_IMAGE)
        self.set_enemys()
        self.set_platforms()
        self.set_items()
        self.set_hero()
        self.set_traps()
        self.set_falling_objects()  
        self.set_boss()
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

        self.boss.update(self.screen, self.time_remaining)
        self.blit_falling_objects()
        self.hero.update(self.screen, self.pressed_keys, self.platforms, self.items, self.enemys, self.traps, self.falling_objects, self.boss)
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

        self.hero = Hero((50, 50), (x, y), 5)
    
    def set_boss(self):
        self.boss = Boss((50, 80), (450, 650),(500, 130), 3)

    def blit_falling_objects(self):
        for fo in self.falling_objects:
            fo.move_down()
            fo.blit(self.screen)

    def create_list_platforms(self):
        list = []

        platform = Platform((250, 56), (0, 445))
        platform_a = Platform((250, 56), (550, 445))
        platform_b = Platform((800, 56), (0, 0))
        platform_c = Platform((200, 50), (0, 330))
        platform_d = Platform((225, 50), (125, 210))
        platform_e = Platform((225, 50), (455, 210))
        platform_f = Platform((200, 50), (600, 330))

        list.append(platform)
        list.append(platform_a)
        list.append(platform_b)
        list.append(platform_c)
        list.append(platform_d)
        list.append(platform_e)
        list.append(platform_f)
  
        
        return list
    
    def create_list_enemys(self):
        list = []

        enemy = Enemy((40, 50), (630, 790), (700, 279), 4)
        enemy_b = Enemy((40, 50), (10, 180), (10, 279), 4)
        enemy_c = Enemy((40, 50), (550, 730), (700, 397), 4)

    
        list.append(enemy)
        list.append(enemy_b)
        list.append(enemy_c)


        return list

    def create_list_items(self):
        list = []
        x = 0 
        
        for i in range(6):
            coin = Item((20, 20), (x + 620, 300), "Coin")
            coin_b = Item((20, 20),(x + 10, 300), "Coin")
            coin_c = Item((20, 20),(x + 170, 180), "Coin")
            coin_d = Item((20, 20),(x + 460, 180), "Coin")
  
            
            x += 30
            list.append(coin)
            list.append(coin_b)
            list.append(coin_c)
            list.append(coin_d)
   
            
        
        crown = Item((50, 40), (735, 390), "Crown")
        list.append(crown)

        gem = Item((30, 30), (550, 100), "Gem")
        gem_b = Item((30, 30), (700, 250), "Gem")
        gem_c = Item((30, 30), (50, 250), "Gem")
        gem_d = Item((30, 30), (230, 100), "Gem")
        list.append(gem)
        list.append(gem_b)
        list.append(gem_c)
        list.append(gem_d)
        

        

        return list
    
    def create_list_traps(self):
        list = []

        # trap = Trap((60, 20), (170, 180), "One")
        # trap_b = Trap((60, 20), (500, 425), "One")
        trap_c = Trap((160, 50), (400, 475), "One")
        trap_d = Trap((160, 50), (240, 475), "One")
 

        # list.append(trap)
        # list.append(trap_b)
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