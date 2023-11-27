from Modules.Characters.Platform import *
from Modules.Characters.Object import Object
from Modules.Characters.Projectile import Projectile
from Modules.Values.Assets import *


class Boss(Object):
    def __init__(self, size, move_position, position=(0,0), speed=3):
        self.size = size
        self.lives = 12
        self.move_position = move_position
        self.animations = self.set_animations()
        self.state = "Left"
        self.current_animation = self.animations[self.state]
        self.step_counter = 0
        self.dead = False
        self.set_speed(speed)
        self.time_last = 0

        #######################
        self.flag_shot = False
        self.time_last_shot = 0
        self.list_projectile = []  
        #######################
        super().__init__(size, position, self.current_animation[self.step_counter]) 

    def update(self, screen, time_remaining):
        super().update()
        self.move_boss(time_remaining)
        self.animation(screen)
        self.update_projectile(screen)

    def shot_projectile(self):
        x = None
        margin = 50
        y = self.rect_main.centery - 10
        if self.state == "Quiet":
            x = self.rect_main.right - margin

        if x is not None:
            self.list_projectile.append(Projectile((50, 50), self.state, (x, y),"Two"))

    def update_projectile(self, screen: py.Surface):
        indice = 0
        while indice < len(self.list_projectile):
            projectile = self.list_projectile[indice]
            screen.blit(projectile.image, projectile.rect_main)
            projectile.update()
            if projectile.rect_main.centerx < 0 or projectile.rect_main.centerx > screen.get_width():
                self.list_projectile.pop(indice)
                indice -= 1
            indice +=1

    
    def move_boss(self, time_remaining): #poner el super().move
        # time = py.time.get_ticks()
        if self.state == "Left":
            self.current_animation = self.animations[self.state]
            super().move_left()                        
            if self.rect_main.x < self.move_position[0]:
                self.state = "Right"
        elif self.state == "Right":
            self.current_animation = self.animations[self.state]
            super().move_right() 
            if self.rect_main.x + 30 > self.move_position[1]:
                self.state = "Quiet"
        elif self.state == "Quiet":
            time = py.time.get_ticks()
            self.current_animation = self.animations[self.state]
            if time - self.time_last >= 15000:
                self.state = "Left" 
                self.time_last = time

        if not self.flag_shot:
            time_shot = py.time.get_ticks()
            if time_shot - self.time_last_shot >= 2000:
                self.shot_projectile() 
                # Efecto de sonido fuego
                self.time_last_shot = time_shot





    def set_animations(self):
        boss_walk_right = []
        boss_quiet = []

        list_path_quiet = [BOSS_QUIET_A,BOSS_QUIET_A,BOSS_QUIET_A,BOSS_QUIET_A, BOSS_QUIET_A,BOSS_QUIET_A,BOSS_QUIET_B,BOSS_QUIET_B,BOSS_QUIET_B,BOSS_QUIET_B,BOSS_QUIET_B,BOSS_QUIET_B,BOSS_QUIET_C,BOSS_QUIET_C,BOSS_QUIET_C,BOSS_QUIET_C,BOSS_QUIET_C,BOSS_QUIET_C,BOSS_QUIET_C,BOSS_QUIET_C,BOSS_QUIET_C,BOSS_QUIET_C,BOSS_QUIET_C,BOSS_QUIET_C]

        list_path_walk = [BOSS_WALK_RIGHT_A,BOSS_WALK_RIGHT_A,BOSS_WALK_RIGHT_B,BOSS_WALK_RIGHT_B,BOSS_WALK_RIGHT_C,BOSS_WALK_RIGHT_C,BOSS_WALK_RIGHT_D,BOSS_WALK_RIGHT_D,BOSS_WALK_RIGHT_E,BOSS_WALK_RIGHT_E,BOSS_WALK_RIGHT_F,BOSS_WALK_RIGHT_F,BOSS_WALK_RIGHT_G,BOSS_WALK_RIGHT_G,BOSS_WALK_RIGHT_H,BOSS_WALK_RIGHT_H,BOSS_WALK_RIGHT_I,
        BOSS_WALK_RIGHT_I]
        
        for path in list_path_walk:
            image_boss_walk_right = self.load_image(path, self.size) 
            boss_walk_right.append(image_boss_walk_right)
        
        for path in list_path_quiet:
            image_boss_path = self.load_image(path, self.size)
            boss_quiet.append(image_boss_path)

        animations = {}
        animations["Quiet"] = boss_quiet
        animations["Right"] = boss_walk_right
        animations["Left"]  = flip_images(boss_walk_right)

        return animations
    
    def animation(self, screen: py.Surface):
        long = len(self.current_animation)
        if self.step_counter >= long:
            self.step_counter = 0
        
        screen.blit(self.current_animation[self.step_counter], self.rect_main)
        self.step_counter += 1
