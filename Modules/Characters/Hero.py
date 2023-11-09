import pygame as py
from Modules.Characters.Object import *
from Modules.Values.Assets import *
from Modules.Characters.Platform import *



class Hero(Object):

    def __init__(self, size, position=(0,0), speed=5) -> None:
        
        self.animations = self.set_animations()
        self.state = "Quiet"
        self.current_animation = self.animations[self.state]
        self.step_counter = 0
        self.move_y = 0
        self.jump_power = -12
        self.jump_speed_limit = 12
        self.gravity = 1
        self.jump = False
        self.points = 0
        self.set_speed(speed)
        super().__init__(size, position, self.current_animation[self.step_counter]) 

    def update(self, screen, pressed_keys, platforms):
        self.move_hero(screen, pressed_keys)
        self.apply_gravity(screen, platforms)
        
    def move_hero(self, screen: py.Surface, pressed_keys):
        self.change_state(pressed_keys)

        match self.state:
            case "Quiet":
                self.current_animation = self.animations["Quiet"]
                self.animation(screen)
            case "Right":
                self.current_animation = self.animations["Right"]
                self.animation(screen)
                self.move_right(screen.get_width()) 
            case "Left":
                self.current_animation = self.animations["Left"]
                self.animation(screen)
                self.move_left(0) 
            case "Up": 
                if not self.jump:
                    self.jump = True
                    self.move_y = self.jump_power
                    self.current_animation = self.animations["Up"]
                    self.animation(screen)
                    self.move_up(0) # El tope debe ser el bottom de las plataformas
   
    def change_state(self, pressed_keys):

        if pressed_keys[py.K_RIGHT]:
            self.state = "Right"
        elif pressed_keys[py.K_LEFT]:
            self.state = "Left"
        elif pressed_keys[py.K_UP]:
            self.state = "Up"
        else:
            self.state = "Quiet"

    def set_speed(self, speed):
        self.speed = speed

    def set_animations(self):
        hero_quiet = []
        hero_walk_right = []
        hero_jump = []  
        
        image_hero_quiet = self.load_image(HERO_QUIET, (50, 50))
        image_hero_walk_right_a = self.load_image(HERO_WALK_RIGHT_A, (50, 50))
        image_hero_walk_right_b = self.load_image(HERO_WALK_RIGHT_B, (50, 50))
        image_hero_jump = self.load_image(HERO_JUMP, (50, 50))

        hero_quiet.append(image_hero_quiet)
        hero_walk_right.append(image_hero_walk_right_a)
        hero_walk_right.append(image_hero_walk_right_b)
        hero_jump.append(image_hero_jump)

        animations = {}
        animations["Quiet"] = hero_quiet
        animations["Right"] = hero_walk_right
        animations["Left"]  = flip_images(hero_walk_right)
        animations["Up"] = hero_jump

        return animations

    def animation(self, screen: py.Surface):
        long = len(self.current_animation)
        if self.step_counter >= long:
            self.step_counter = 0
        
        screen.blit(self.current_animation[self.step_counter], self.rect_main)
        self.step_counter += 1

    def move_right(self, top_right): 
        new_x = self.rect_main.x + self.speed

        if new_x >= 0 and new_x <= top_right - self.rect_main.width:
            self.image = self.current_animation

            super().move_right()

    def move_left(self, top_left):
        new_x = self.rect_main.x - self.speed

        if new_x >= top_left:
            self.image = self.current_animation

            super().move_left()

    def move_up(self, top_up):
        new_y = self.rect_main.y - self.speed

        if new_y >= top_up:
            self.image = self.current_animation

            super().move_up()

    def apply_gravity(self, screen, platforms: list["Platform"]):

        if self.jump:
            self.animation(screen)
            self.rect_main.y += self.move_y
            if self.move_y + self.gravity < self.jump_speed_limit:
                self.move_y += self.gravity
            
        for pl in platforms:
            if self.rect_main.colliderect(pl.rect_main):
                self.move_y = 0
                self.jump = False
                self.rect_main.bottom = pl.rect_main.top
                break
            # elif self.rect.colliderect(pl.rect.bottom):
            #     self.move_y = 0
            #     self.jump = False
            #     self.rect.bottom = pl.rect.top
            #     break
            else:
                self.jump = True
        
        self.all_rects()

    # def collide_with_falling_objects(self, falling_objects:list['FallingObject']):
    #     for fo in falling_objects:
    #         # if self.rect.colliderect(fo.rect):
    #         if self.mouth.rect.colliderect(fo.rect):
    #             fo.set_random_position()
    #             self.collide_fo_effects()
    #             self.points += 1
            
    # def collide_fo_effects(self):
    #     # TODO: Refactorizar
    #     #  FIXME: Refactorizar
    #     music = py.mixer.Sound(MARIO_COIN_SOUND)
    #     music.set_volume(0.5)
    #     music.play()

    # def blit(self, screen):
        # screen.blit(self.mouth.image, self.mouth.rect)
        # super().blit(screen)