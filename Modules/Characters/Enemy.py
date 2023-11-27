from Modules.Characters.Platform import *
from Modules.Characters.Object import Object
from Modules.Values.Assets import *


class Enemy(Object):
    def __init__(self, size, move_position, position=(0,0), speed=3):
        self.size = size
        self.move_position = move_position
        self.animations = self.set_animations()
        self.state = "Left"
        self.current_animation = self.animations[self.state]
        self.step_counter = 0
        self.dead = False
        self.set_speed(speed)
        super().__init__(size, position, self.current_animation[self.step_counter]) 

    def update(self, screen):
        super().update()
        self.move_enemy()
        self.animation(screen)
        
    
    def move_enemy(self):
        if self.state == "Left":
            self.current_animation = self.animations[self.state]
            super().move_left()
            if self.rect_main.x < self.move_position[0]: 
                self.state = "Right"
        elif self.state == "Right":
            self.current_animation = self.animations[self.state]
            super().move_right()
            if self.rect_main.x + 30 > self.move_position[1]:
                self.state = "Left"   


    def set_animations(self):
        enemy_walk_right = []
        list_path = [ENEMY_WALK_RIGHT_A,ENEMY_WALK_RIGHT_A,ENEMY_WALK_RIGHT_B,ENEMY_WALK_RIGHT_B,ENEMY_WALK_RIGHT_C,ENEMY_WALK_RIGHT_C, ENEMY_WALK_RIGHT_D,ENEMY_WALK_RIGHT_D,ENEMY_WALK_RIGHT_E,ENEMY_WALK_RIGHT_E,ENEMY_WALK_RIGHT_F,ENEMY_WALK_RIGHT_F,ENEMY_WALK_RIGHT_G,ENEMY_WALK_RIGHT_G,ENEMY_WALK_RIGHT_H,ENEMY_WALK_RIGHT_H]

        for path in list_path:
            image_enemy_walk_right = self.load_image(path, self.size) 
            enemy_walk_right.append(image_enemy_walk_right)

        animations = {}
        animations["Right"] = enemy_walk_right
        animations["Left"]  = flip_images(enemy_walk_right)

        return animations
    
    def animation(self, screen: py.Surface):
        long = len(self.current_animation)
        if self.step_counter >= long:
            self.step_counter = 0
        
        screen.blit(self.current_animation[self.step_counter], self.rect_main)
        self.step_counter += 1


            

        


