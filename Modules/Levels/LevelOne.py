from Modules.Characters.Enemy import Enemy
from Modules.Levels.Level import Level
from Modules.Characters.Platform import Platform
from Modules.Values.Assets import *
from Modules.Characters.Hero import *
from Modules.Values.Assets import *
from Modules.Values.EColors import *
from Modules.Levels.LevelOne import *



class LevelOne(Level):

    def __init__(self, size, FPS, caption="Title", icon=""):
        super().__init__(size, FPS, caption, icon)

        self.set_background_image(BACKGROUND_IMAGE)
        self.set_enemys()
        self.set_platforms()
        self.set_hero()
        self.pressed_keys = []
        # self.set_falling_objects(28)        

        # self.set_music(MARIO_MUSIC)
        
    # def set_falling_objects(self, size):
    #     self.falling_objects = FallingObject.create_list(size, self.size)

    def update(self, list_events):
        super().update(list_events)
        self.blit_platforms()
        self.blit_enemys()
        self.get_pressed()
        self.hero.update(self.screen, self.pressed_keys, self.platforms)
        # self.enemys[0].update(self.screen)
        self.show_score("0")
        self.draw_hitbox()


    def set_platforms(self):
        self.platforms = self.create_list_platforms() 
    
    def set_enemys(self):
        self.enemys = self.create_list_enemy()
    
    def set_hero(self):
        x = self.size[0] * 0
        y = self.size[1] - 100

        self.hero = Hero((50, 50), (x, y), 7)

    def blit_hero(self):
        self.hero.blit(self.screen)
        
    def blit_platforms(self):
        for platform in self.platforms:
            platform.blit(self.screen)

    def blit_enemys(self):
        for enemy in self.enemys:
            enemy.blit(self.screen)

    def create_list_platforms(self):
        list = []

        platform = Platform((800, 56), (0, 445))
        platform_b = Platform((800, 56), (0, 0))
        platform_c = Platform((75,30), (100, 350))
        platform_d = Platform((75,30), (300, 350))
        platform_e = Platform((75,30), (500, 350))

        list.append(platform)
        list.append(platform_b)
        list.append(platform_c)
        list.append(platform_d)
        list.append(platform_e)
        
        return list
    
    def create_list_enemy(self):
        list = []

        enemy = Enemy((50,50), (350, 395))
        enemy_b = Enemy((50,50), (400, 395))
        enemy_c = Enemy((50,50), (450, 395))
        enemy_d = Enemy((50,50), (500, 395))

        list.append(enemy)
        list.append(enemy_b)
        list.append(enemy_c)
        list.append(enemy_d)


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







