import os
import pygame as py

def rescale_images(animations: dict, widht: int, high: int):
    for key in animations:
        for i in range(len(animations[key])):
            img = animations[key][i]
            animations[key][i] = py.transform.scale(img, (widht, high))

def flip_images(images: list):
    list_images = []
    for i in range(len(images)):
        flip_image = py.transform.flip(images[i],True,False)
        list_images.append(flip_image)
    
    return list_images

# ATMOSPHERE
GAME_ICON = os.path.join('Modules','Assets', 'Images', 'icon.png') 
PLATFORM_IMAGE = os.path.join('Modules','Assets', 'Images', 'Atmosphere', 'platform.png') 
BACKGROUND_IMAGE = os.path.join('Modules','Assets', 'Images', 'Atmosphere', 'background.png')

# HERO
HERO_QUIET = os.path.join('Modules','Assets', 'Images', 'Hero', 'hero.png')
HERO_WALK_RIGHT_A = os.path.join('Modules','Assets', 'Images', 'Hero', 'hero-1.png')
HERO_WALK_RIGHT_B = os.path.join('Modules','Assets', 'Images', 'Hero', 'hero-2.png')
HERO_WALK_RIGHT_C = os.path.join('Modules','Assets', 'Images', 'Hero', 'hero-3.png') 
HERO_WALK_RIGHT_D = os.path.join('Modules','Assets', 'Images', 'Hero', 'hero-4.png') 
HERO_WALK_RIGHT_E = os.path.join('Modules','Assets', 'Images', 'Hero', 'hero-5.png') 
HERO_JUMP = os.path.join('Modules','Assets', 'Images', 'Hero', 'hero-6.png')
PROJECTILE = os.path.join('Modules','Assets', 'Images', 'Hero', 'projectile.png')
ONE_LIVE = os.path.join('Modules','Assets', 'Images', 'Hero', '1-3.png')
TWO_LIVE = os.path.join('Modules','Assets', 'Images', 'Hero', '2-3.png')
THREE_LIVE = os.path.join('Modules','Assets', 'Images', 'Hero', '3-3.png')

# ITEMS
COIN = os.path.join('Modules','Assets', 'Images', 'Item', 'coin.png')
CROWN = os.path.join('Modules','Assets', 'Images', 'Item', 'crown.png')
STAR = os.path.join('Modules','Assets', 'Images', 'Item', 'star.png')

# ENEMY
ENEMY_WALK_RIGHT_A = os.path.join('Modules','Assets', 'Images', 'Enemy', 'enemy-1.png')
ENEMY_WALK_RIGHT_B = os.path.join('Modules','Assets', 'Images', 'Enemy', 'enemy-2.png')
ENEMY_WALK_RIGHT_C = os.path.join('Modules','Assets', 'Images', 'Enemy', 'enemy-3.png')
ENEMY_WALK_RIGHT_D = os.path.join('Modules','Assets', 'Images', 'Enemy', 'enemy-4.png')
ENEMY_WALK_RIGHT_E = os.path.join('Modules','Assets', 'Images', 'Enemy', 'enemy-5.png')
ENEMY_WALK_RIGHT_F = os.path.join('Modules','Assets', 'Images', 'Enemy', 'enemy-6.png')
ENEMY_WALK_RIGHT_G = os.path.join('Modules','Assets', 'Images', 'Enemy', 'enemy-7.png')
ENEMY_WALK_RIGHT_H = os.path.join('Modules','Assets', 'Images', 'Enemy', 'enemy-8.png')

# TRAP
TRAP_ONE = os.path.join('Modules','Assets', 'Images', 'Trap', 'trap.png') 
TRAP_TWO = os.path.join('Modules','Assets', 'Images', 'Trap', 'trap-1.png') 

# FALLING OBJECTS
STONE = os.path.join('Modules','Assets', 'Images', 'Falling', 'stone.png')  

# SOUND
COIN_SOUND = os.path.join('Modules','Assets', 'Music', 'coin.mp3')  
ZOMBIE_SOUND = os.path.join('Modules','Assets', 'Music', 'zombie.mp3')  
PROJECTILE_SOUND = os.path.join('Modules','Assets', 'Music', 'projectile.mp3')  
BANG_SOUND = os.path.join('Modules','Assets', 'Music', 'bang.mp3')  
STAR_SOUND = os.path.join('Modules','Assets', 'Music', 'star.mp3')  



