from Modules.Levels.LevelConfig import LevelConfig
from Modules.Characters.Platform import Platform
from Modules.Values.Assets import *
from Modules.Characters.Hero import *
from Modules.Values.Assets import *
from Modules.Values.EColors import *
from Modules.Levels.LevelOne import *



class LevelTwo(LevelConfig):

    def __init__(self, size, FPS, caption="Title", icon=""):
        super().__init__(size, FPS, caption, icon)

        self.set_background_image(BACKGROUND_IMAGE)

        self.set_platforms()
        self.set_hero()
        # self.set_falling_objects(28)        
        self.set_icon(GAME_ICON)
        self.pressed_keys = []

        # self.set_music(MARIO_MUSIC)
        
    # def set_falling_objects(self, size):
    #     self.falling_objects = FallingObject.create_list(size, self.size)

    def update(self, list_events):
        super().update(list_events)
        self.blit_platforms()
        self.draw_hitbox()
        self.get_pressed()
        self.hero.update(self.screen, self.pressed_keys, self.platforms)
        # self.blit_hero()

    def set_platforms(self):
        # self.platforms = Platform.create_list()
        self.platforms = self.create_list_platforms() 
    
    def set_hero(self):
        x = self.size[0] * 0
        y = self.size[1] - 100

        self.hero = Hero((50, 50), (x, y), 7)

    # def set_platform(self):
    #     x = self.size[0] * 0
    #     y = self.size[1] - 10
    #     self.platform = Platform((self.size[0], 100), (x, y))


    def blit_hero(self):
        self.hero.blit(self.screen)
        

    # def blit_platform(self):
    #     self.platform.blit(self.screen)


    # def blit_falling_objects(self):
    #     for fo in self.falling_objects:
    #         fo.move_down()
    #         fo.blit(self.screen)

    def blit_platforms(self):
        for platform in self.platforms:
            platform.blit(self.screen)

    def create_list_platforms(self):
        list = []

        platform = Platform((800, 56), (0, 445))
        platform_b = Platform((800, 56), (0, 0))
        platform_c = Platform((75,30), (100, 350))

        list.append(platform)
        list.append(platform_b)
        list.append(platform_c)
        
        return list

    
    # def check_collides(self):
    #     self.heroe.collide_with_falling_objects(self.falling_objects)

    #     self.show_score(self.heroe.points)