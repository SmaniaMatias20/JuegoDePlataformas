import pygame as py
from Modules.Characters.Object import Object
from Modules.Values.Assets import PLATFORM_IMAGE


class Platform(Object):

    def __init__(self, size, position=(0,0)) -> None:
        super().__init__(size, position, PLATFORM_IMAGE)

    def blit(self, screen):
        # screen.blit(self.image, self.image.rect)
        super().blit(screen)


    @staticmethod
    def create_list():
        list = []

        # Plataforma principal
        platform = Platform((800, 56), (0, 445))
        platform_b = Platform((800, 56), (0, 0))

        
        list.append(platform)
        list.append(platform_b)



        return list