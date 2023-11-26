import pygame as py
from Modules.Characters.Enemy import Enemy
from Modules.Characters.FallingObject import FallingObject
from Modules.Characters.Item import Item
from Modules.Characters.Object import *
from Modules.Characters.Projectile import Projectile
from Modules.Characters.Trap import Trap
from Modules.Values.Assets import *
from Modules.Characters.Platform import *



class Hero(Object):

    def __init__(self, size, position=(0,0), speed=3) -> None:
        self.size = size
        self.animations = self.set_animations()
        self.state = "Quiet"
        self.current_animation = self.animations[self.state]
        self.step_counter = 0
        self.move_y = 0
        self.jump_power = -15
        self.jump_speed_limit = 15
        self.gravity = 1
        self.jump = False
        self.points = 0
        self.lives = 3
        #########################
        self.flag_shot = False
        self.time_last_shot = 0
        self.list_projectile = []  
        #########################
        self.set_speed(speed)
        super().__init__(size, position, self.current_animation[self.step_counter]) 

    def update(self, screen, pressed_keys, platforms, items, enemys, traps, stones):
        self.show_lives(screen)
        self.move_hero(screen, pressed_keys)
        self.update_projectile(screen)
        self.apply_gravity(screen, platforms)
        self.collide_with_items(items)
        self.collide_with_enemys(enemys)
        self.collide_with_traps(traps)
        self.collide_with_falling_objects(stones)
        
    
    def move_hero(self, screen: py.Surface, pressed_keys):
        self.change_state(pressed_keys)

        match self.state:
            case "Quiet":
                self.current_animation = self.animations[self.state]
                self.animation(screen)
            case "Right":
                self.current_animation = self.animations[self.state]
                self.animation(screen)
                self.move_right(screen.get_width()) 
                self.flag_shot = True
            case "Left":
                self.current_animation = self.animations[self.state]
                self.animation(screen)
                self.move_left(0) 
                self.flag_shot = True
            case "Up": 
                if not self.jump: 
                    self.jump = True
                    self.move_y = self.jump_power
                    self.current_animation = self.animations[self.state]
                    self.animation(screen)
                    self.move_up(0)

        if self.flag_shot and pressed_keys[py.K_f]:
            time = py.time.get_ticks()
            if time - self.time_last_shot >= 1000:
                self.shot_projectile() 
                self.shot_projectile_effects()
                self.flag_shot = False
                self.time_last_shot = time
     

    def show_lives(self, screen):
        one_live = self.load_image(ONE_LIVE, (75, 30))
        two_live = self.load_image(TWO_LIVE, (75, 30))
        three_live = self.load_image(THREE_LIVE, (75, 30))

        if self.lives >= 3:
            self.lives = 3
            screen.blit(three_live, [10, 30])
        elif self.lives == 2:
            screen.blit(two_live, [10, 30])
        elif self.lives == 1:
            screen.blit(one_live, [10, 30])
        else:
            print("Fin del juego")

    def shot_projectile(self):
        x = None
        margin = 47
        y = self.rect_main.centery - 10
        if self.state == "Right":
            x = self.rect_main.right - margin
        elif self.state == "Left":
            x = self.rect_main.left - 100 + margin

        if x is not None:
            self.list_projectile.append(Projectile((30, 10), self.state, (x, y)))

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
        list_path = [HERO_WALK_RIGHT_A, HERO_WALK_RIGHT_B, HERO_WALK_RIGHT_C, HERO_WALK_RIGHT_D, HERO_WALK_RIGHT_E]

        for path in list_path:
            image_hero_walk_right = self.load_image(path, self.size) 
            hero_walk_right.append(image_hero_walk_right)

        image_hero_quiet = self.load_image(HERO_QUIET, self.size)
        image_hero_jump = self.load_image(HERO_JUMP, self.size)
        hero_quiet.append(image_hero_quiet)
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
                if self.move_y > 0:  
                    self.move_y = 0
                    self.jump = False
                    self.rect_main.bottom = pl.rect_main.top
                elif self.move_y < 0: 
                    self.move_y = 0
                    self.rect_main.top = pl.rect_main.bottom
                break
            else:
                self.jump = True
        
        self.all_rects()

    def collide_with_items(self, items:list['Item']):
        indice = 0
        while indice < len(items):
            if self.rect_main.colliderect(items[indice].rect_main):
                if items[indice].type == "Coin":
                    self.points += 10
                    items.pop(indice)
                    self.collide_coin_effects()
                    indice -= 1
                else:
                    self.points += 50
                    items.pop(indice)
                    indice -= 1
                    print("Fin del Nivel") # Retornar algo para finalizar el nivel
            indice +=1
    
    def collide_with_traps(self, traps:list['Trap']):
        indice = 0
        while indice < len(traps):
            if self.rect_main.colliderect(traps[indice].rect_main):
                self.lives -= 1
                self.rect_main.x = 0
                self.rect_main.y = 400
                break
            indice +=1

    def collide_with_falling_objects(self, objects:list['FallingObject']):
        indice = 0
        while indice < len(objects):
            if self.rect_main.colliderect(objects[indice].rect_main):
                if objects[indice].type == "Stone":
                    self.bang_effects()
                    self.lives -= 1
                    self.rect_main.x = 0
                    self.rect_main.y = 400
                    objects.pop(indice)
                    indice -= 1
                elif objects[indice].type == "Star":
                    self.collide_star_effects()
                    self.lives += 1
                    objects.pop(indice)
                    indice -= 1
            indice +=1


    def collide_with_enemys(self, enemys:list['Enemy']):
        indice = 0
        while indice < len(enemys):
            if self.rect_main.colliderect(enemys[indice].rect_main):
                self.lives -= 1
                self.rect_main.x = 0
                self.rect_main.y = 400
                break
            indice +=1
        
        self.kill_enemy(enemys)
    
    def kill_enemy(self, enemys:list['Enemy']):
        for projectile in self.list_projectile:
            for enemy in enemys:
                if projectile.rect_main.colliderect(enemy.rect_main):
                    self.bang_effects()
                    self.list_projectile.remove(projectile)
                    self.points += 50
                    enemys.remove(enemy)
                    del enemy

    

    def collide_coin_effects(self):
        music = py.mixer.Sound(COIN_SOUND)
        music.set_volume(0.2)
        music.play()

    def shot_projectile_effects(self):
        music = py.mixer.Sound(PROJECTILE_SOUND)
        music.set_volume(0.2)
        music.play()

    def bang_effects(self):
        music = py.mixer.Sound(BANG_SOUND)
        music.set_volume(0.1)
        music.play()
    
    def collide_star_effects(self):
        music = py.mixer.Sound(STAR_SOUND)
        music.set_volume(0.2)
        music.play()

