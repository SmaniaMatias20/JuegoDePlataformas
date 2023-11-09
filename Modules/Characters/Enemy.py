from Modules.Characters.Object import Object
from Modules.Characters.Platform import Platform
from Modules.Values.Assets import *


class Enemy(Object):
    def __init__(self, size, position=(0,0), speed=5):

        self.animations = self.set_animations()
        self.state = "Left"
        self.current_animation = self.animations[self.state]
        self.step_counter = 0
        self.dead = False
        self.set_speed(speed)
        super().__init__(size, position, self.current_animation[self.step_counter]) 

    def update(self, screen):
        # self.animation(screen)
        pass



    def set_animations(self):
        enemy_quiet = []
        enemy_walk_right = []
 
        image_enemy_quiet = self.load_image(ENEMY_QUIET, (50, 50))
        image_enemy_walk_right_a = self.load_image(ENEMY_WALK_RIGHT_A, (50, 50))
        image_enemy_walk_right_b = self.load_image(ENEMY_WALK_RIGHT_B, (50, 50))

        enemy_quiet.append(image_enemy_quiet)
        enemy_walk_right.append(image_enemy_walk_right_a)
        enemy_walk_right.append(image_enemy_walk_right_b)

        animations = {}
        animations["Quiet"] = enemy_quiet
        animations["Right"] = enemy_walk_right
        animations["Left"]  = flip_images(enemy_walk_right)


        return animations
    
    def animation(self, screen: py.Surface):
        long = len(self.current_animation)
        if self.step_counter >= long:
            self.step_counter = 0
        
        screen.blit(self.current_animation[self.step_counter], self.rect_main)
        self.step_counter += 1

    # def apply_gravity(self, screen, platforms: list["Platform"]):

    #     if self.jump:
    #         self.animation(screen)
    #         self.rect_main.y += self.move_y
    #         if self.move_y + self.gravity < self.jump_speed_limit:
    #             self.move_y += self.gravity
            
    #     for pl in platforms:
    #         if self.rect_main.colliderect(pl.rect_main):
    #             self.move_y = 0
    #             self.jump = False
    #             self.rect_main.bottom = pl.rect_main.top
    #             break
    #         # elif self.rect.colliderect(pl.rect.bottom):
    #         #     self.move_y = 0
    #         #     self.jump = False
    #         #     self.rect.bottom = pl.rect.top
    #         #     break
    #         else:
    #             self.jump = True
        
    #     self.all_rects()
            

        


