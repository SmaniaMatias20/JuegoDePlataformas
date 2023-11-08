# from modulos.characters.FallingObject import FallingObject
from Modules.Characters.Hero import *
from Modules.Characters.Platform import Platform
from Modules.Values.Assets import *
from Modules.Values.EColors import *
# from Modules.Config import Config


# class Game(Config):

    # def __init__(self, size, FPS, caption="Title", icon=""):
    #     super().__init__(size, FPS, caption, icon)

    #     self.set_background_image(BACKGROUND_IMAGE)

    #     self.set_plataforms()
    #     self.set_hero()
        # self.set_falling_objects(28)        
        # self.set_icon(GAME_ICONO)
        # self.pressed_keys = []

        # self.set_music(MARIO_MUSIC)
        
    # def set_falling_objects(self, size):
    #     self.falling_objects = FallingObject.create_list(size, self.size)
    # def set_plataforms(self):
    #     self.platforms = Platform.create_list()
    


    # def set_hero(self):
    #     x = self.size[0] * 0
    #     y = self.size[1] - 100

    #     self.hero = Hero((50, 50), (x, y), 7)

    # def set_platform(self):
    #     x = self.size[0] * 0
    #     y = self.size[1] - 10
    #     self.platform = Platform((self.size[0], 100), (x, y))


    # def blit_hero(self):
    #     self.hero.blit(self.screen)
        

    # def blit_platform(self):
    #     self.platform.blit(self.screen)


    # def blit_falling_objects(self):
    #     for fo in self.falling_objects:
    #         fo.move_down()
    #         fo.blit(self.screen)
    # def blit_platforms(self):
    #     for platform in self.platforms:
    #         platform.blit(self.screen)
    



    # def check_collides(self):
    #     self.heroe.collide_with_falling_objects(self.falling_objects)

    #     self.show_score(self.heroe.points)



# def init():
#     py.init()

#     while nivel_actual.running: # self.running

#         events = py.event.get()
#         for event in events:
#             if event.type == py.QUIT:
#                 nivel_actual.running = False
            

#         nivel_actual.update(events)
        # self.fill_screen()
        
        # self.clock.tick(self.FPS)            

        # for event in py.event.get():
        #     if event.type == py.QUIT:
        #         self.running = False
        #     elif event.type == py.KEYDOWN:
        #         if event.key == py.K_TAB:
        #             self.change_mode()

        # posicion = py.mouse.get_pos()
        # print(posicion)

        # self.get_pressed()

        # self.blit_platform()
        # self.blit_platforms()
        # self.draw_hitbox(EColors.ROJO.value)      #--- dibujar los rectangulos de las imagenes ---

        # self.hero.update(self.screen, self.pressed_keys, self.platforms) # Agregar una lista de dict de plataformas como parametro

        # self.blit_hero()


        # self.blit_falling_objects()

        # self.check_collides()
        
        
    #     py.display.flip()
    
    # py.quit()

    # def get_pressed(self):
    #     self.pressed_keys = py.key.get_pressed()

    # def show_score(self, text):
    #     # TODO: Hacer reutilizable
    #     font = py.font.SysFont('Arial', 30)
    #     text = font.render(f"Score: {text}", True, EColors.BLANCO.value)
    #     self.screen.blit(text, (0, 0))

    # def draw_hitbox(self, color):
    #     if self.get_mode():
    #         for pl in self.platforms:
    #             py.draw.rect(self.screen, color, pl, 3)

    #         py.draw.rect(self.screen, color, self.hero.rect, 3)


    # --------------MODIFICAR 
