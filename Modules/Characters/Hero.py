import pygame as py

from Modules.Characters.Object import Object
from Modules.Values.Assets import *



class Hero(Object):

    def __init__(self, size, position=(0,0), speed=5) -> None:
        super().__init__(size, position)
        
        self.animations = self.set_animations()
        self.state = "Quiet"
        self.current_animation = self.animations["Quiet"]
        self.step_counter = 0


        self.points = 0
        self.set_speed(speed)


    def update(self, screen, pressed_keys):
        self.move_hero(screen, pressed_keys)
        

    def move_hero(self, screen, pressed_keys):
        self.change_state(pressed_keys)

        match self.state:
            case "Quiet":
                self.current_animation = self.animations["Quiet"]
                self.animation(screen)
            case "Right":
                self.current_animation = self.animations["Right"]
                self.animation(screen)
                self.move_right(800) 
            case "Left":
                self.current_animation = self.animations["Left"]
                self.animation(screen)
                self.move_left(0) 
        
    def change_state(self, pressed_keys):

        if pressed_keys[py.K_RIGHT]:
                self.state = "Right"
        elif pressed_keys[py.K_LEFT]:
            self.state = "Left"
        else:
            self.state = "Quiet"

    def set_speed(self, speed):
        self.speed = speed

    def set_animations(self):
        # Corregir         

        hero_quiet = [
            HERO_QUIET
        ]

        hero_walk_right = [
            HERO_WALK_RIGHT_A,
            HERO_WALK_RIGHT_B

        ]

        hero_walk_left = [
            HERO_WALK_RIGHT_A,
            HERO_WALK_RIGHT_B
        ]

        animations = {}
        animations["Quiet"] = hero_quiet
        animations["Right"] = hero_walk_right

        hero_walk_left = flip_images(hero_walk_left)
        animations["Left"] = hero_walk_left

        rescale_images(animations, 50, 50)

        return animations

    def animation(self, screen: py.Surface):
        long = len(self.current_animation)
        if self.step_counter >= long:
            self.step_counter = 0
        
        screen.blit(self.current_animation[self.step_counter], self.rect)
        self.step_counter += 1

    def move_right(self, top_right): 
        new_x = self.rect.x + self.speed
        if new_x >= 0 and new_x <= top_right - self.rect.width:
            self.image = self.current_animation
            super().move_right()

    def move_left(self, top_left):
        new_x = self.rect.x - self.speed

        if new_x >= top_left:
            self.image = self.current_animation

            super().move_left()

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

    def blit(self, screen):
        # screen.blit(self.mouth.image, self.mouth.rect)
        super().blit(screen)