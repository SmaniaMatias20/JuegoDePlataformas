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

# MARIO_MUSIC = os.path.join('assets', 'music', 'mario_fondo.flac')
# MARIO_COIN_SOUND = os.path.join('assets', 'music', 'mario-coin.mp3')
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
COIN = os.path.join('Modules','Assets', 'Images', 'Item', 'coin.png')
CROWN = os.path.join('Modules','Assets', 'Images', 'Item', 'crown.png')
ONE_LIVE = os.path.join('Modules','Assets', 'Images', 'Hero', '1-3.png')
TWO_LIVE = os.path.join('Modules','Assets', 'Images', 'Hero', '2-3.png')
THREE_LIVE = os.path.join('Modules','Assets', 'Images', 'Hero', '3-3.png')

# ENEMY IMAGE
ENEMY_QUIET = os.path.join('Modules','Assets', 'Images', 'Enemy', 'enemy.png')
ENEMY_WALK_RIGHT_A = os.path.join('Modules','Assets', 'Images', 'Enemy', 'enemy-1.png')
ENEMY_WALK_RIGHT_B = os.path.join('Modules','Assets', 'Images', 'Enemy', 'enemy-2.png')
ENEMY_WALK_RIGHT_C = os.path.join('Modules','Assets', 'Images', 'Enemy', 'enemy-3.png')
ENEMY_WALK_RIGHT_D = os.path.join('Modules','Assets', 'Images', 'Enemy', 'enemy-4.png')
ENEMY_WALK_RIGHT_E = os.path.join('Modules','Assets', 'Images', 'Enemy', 'enemy-5.png')
ENEMY_WALK_RIGHT_F = os.path.join('Modules','Assets', 'Images', 'Enemy', 'enemy-6.png')



