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
BACKGROUND_IMAGE = os.path.join('Modules','Assets', 'Images', 'Atmosphere', 'background.jpg')


# HERO IMAGE
HERO_QUIET = os.path.join('Modules','Assets', 'Images', 'Hero', 'hero.png')
HERO_WALK_RIGHT_A = os.path.join('Modules','Assets', 'Images', 'Hero', 'hero-1.png')
HERO_WALK_RIGHT_B = os.path.join('Modules','Assets', 'Images', 'Hero', 'hero-2.png')
HERO_JUMP = os.path.join('Modules','Assets', 'Images', 'Hero', 'hero-3.png')

# ENEMY IMAGE
ENEMY_QUIET = os.path.join('Modules','Assets', 'Images', 'Enemy', 'enemy.png')
ENEMY_WALK_RIGHT_A = os.path.join('Modules','Assets', 'Images', 'Enemy', 'enemy-4.png')
ENEMY_WALK_RIGHT_B = os.path.join('Modules','Assets', 'Images', 'Enemy', 'enemy-3.png')


