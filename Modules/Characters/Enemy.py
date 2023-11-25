from Modules.Characters.Platform import *
from Modules.Characters.Object import Object
from Modules.Characters.Platform import Platform
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
        self.move_enemy(screen)
        self.animation(screen)
    
    def move_enemy(self, screen: py.Surface):
        if self.state == "Left":
            self.current_animation = self.animations[self.state]
            self.rect_main.x -= self.speed
            if self.rect_main.x < self.move_position[0]: # Hasta que posision se va a mover cada enemigo
                self.state = "Right"
        elif self.state == "Right":
            self.current_animation = self.animations[self.state]
            self.rect_main.x += self.speed
            if self.rect_main.x + 30 > self.move_position[1]:
                self.state = "Left" 
                
        self.all_rects()

    def set_animations(self):
        enemy_quiet = []
        enemy_walk_right = []
 
        image_enemy_quiet = self.load_image(ENEMY_QUIET, self.size)
        image_enemy_walk_right_a = self.load_image(ENEMY_WALK_RIGHT_A, self.size)
        image_enemy_walk_right_b = self.load_image(ENEMY_WALK_RIGHT_B, self.size)
        image_enemy_walk_right_c = self.load_image(ENEMY_WALK_RIGHT_C, self.size)
        image_enemy_walk_right_d = self.load_image(ENEMY_WALK_RIGHT_D, self.size)
        image_enemy_walk_right_e = self.load_image(ENEMY_WALK_RIGHT_E, self.size)
        image_enemy_walk_right_f = self.load_image(ENEMY_WALK_RIGHT_F, self.size)


        enemy_quiet.append(image_enemy_quiet)
        enemy_walk_right.append(image_enemy_walk_right_a)
        enemy_walk_right.append(image_enemy_walk_right_b)
        enemy_walk_right.append(image_enemy_walk_right_c)
        enemy_walk_right.append(image_enemy_walk_right_d)
        enemy_walk_right.append(image_enemy_walk_right_e)
        enemy_walk_right.append(image_enemy_walk_right_f)

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

    
            

        


