from Modules.Characters.Enemy import Enemy
from Modules.Characters.Item import Item
from Modules.Levels.Level import Level
from Modules.Characters.Platform import Platform
from Modules.Values.Assets import *
from Modules.Characters.Hero import *
from Modules.Values.Assets import *
from Modules.Values.EColors import *
from Modules.Levels.LevelOne import *



class LevelOne(Level):

    def __init__(self, size):
        super().__init__(size)
        self.set_background_image(BACKGROUND_IMAGE)
        self.set_enemys()
        self.set_platforms()
        self.set_items()
        self.set_hero()
        self.pressed_keys = []
        # self.set_music(MARIO_MUSIC)
        


    def update(self, list_events):
        super().update(list_events)
        
        
        self.blit_platforms()
        self.blit_items()
        for enemy in self.enemys:
            enemy.update(self.screen)

        self.hero.update(self.screen, self.pressed_keys, self.platforms, self.items)
        self.show_score(f"{self.hero.points}")
        self.draw_hitbox()

    def set_platforms(self):
        self.platforms = self.create_list_platforms() 
    
    def set_enemys(self):
        self.enemys = self.create_list_enemys()
    
    def set_items(self):
        self.items = self.create_list_items()
    
    def set_hero(self):
        x = self.size[0] * 0
        y = self.size[1] - 100

        self.hero = Hero((50, 50), (x, y), 5)

    def blit_hero(self):
        self.hero.blit(self.screen)
        
    def blit_platforms(self):
        for platform in self.platforms:
            platform.blit(self.screen)

    # def blit_enemys(self):
    #     for enemy in self.enemys:
    #         enemy.blit(self.screen)
    #         enemy.update(self.screen)
    
    def blit_items(self):
        for item in self.items:
            item.blit(self.screen)

    def create_list_platforms(self):
        list = []

        platform = Platform((800, 56), (0, 445))
        platform_b = Platform((800, 56), (0, 0))
        platform_c = Platform((700, 50), (0, 325))
        platform_d = Platform((700, 50), (100, 200))
        

        # platform_g = Platform((100,30), (400, 250))
        # platform_h = Platform((100,30), (600, 250))

        list.append(platform)
        list.append(platform_b)
        list.append(platform_c)
        list.append(platform_d)
  
        # list.append(platform_g)
        # list.append(platform_h)
        
        return list
    
    def create_list_enemys(self):
        list = []

        enemy = Enemy((40, 50), (350, 395), 3)
        enemy_b = Enemy((40, 50), (550, 300), 3)
        # enemy_c = Enemy((50,50), (350, 300))
        # enemy_d = Enemy((50,50), (650, 200))

        list.append(enemy)
        list.append(enemy_b)
        # list.append(enemy_c)
        # list.append(enemy_d)


        return list

    def create_list_items(self):
        list = []

        coin = Item((20, 20), (250, 250), "Coin")
        coin_b = Item((20, 20), (300, 300), "Coin")

        list.append(coin)
        list.append(coin_b)

        return list


    







    # def set_platform(self):
    #     x = self.size[0] * 0
    #     y = self.size[1] - 10
    #     self.platform = Platform((self.size[0], 100), (x, y))



    # def blit_platform(self):
    #     self.platform.blit(self.screen)


    # def blit_falling_objects(self):
    #     for fo in self.falling_objects:
    #         fo.move_down()
    #         fo.blit(self.screen)


    
    # def check_collides(self):
    #     self.heroe.collide_with_falling_objects(self.falling_objects)

    #     self.show_score(self.heroe.points)







