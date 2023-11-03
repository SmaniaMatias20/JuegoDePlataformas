import pygame as py

from Modules.Values.EOrientation import EOrientation

class Object:

    def __init__(self, size_surface, position,path=None) -> None:
        # self.speed = 0

        # Version pre imagenes.
        if path == None:
            self.image = py.Surface(size_surface)
        else:
            # self.image = self.load_image(path, size_surface)
            self.image = py.image.load(path)
            self.image = py.transform.scale(self.image, size_surface)

        self.rect = self.image.get_rect()
        
        self.rect.x = position[0]
        self.rect.y = position[1]

        self.direction = EOrientation.IDLE
        
        self.set_speed(0)

    def load_image(self, path, size_surface):
        image = py.image.load(path)
        image = py.transform.scale(image, size_surface)

        return image
    
    def set_speed(self, speed):
        self.speed = speed

    def move_right(self, speed=None):
        if speed:
            self.set_speed(speed=None)

        self.direction = EOrientation.RIGHT
        self.move()

    def move_left(self, speed=None):
        if speed:
            self.set_speed(speed=None)
        self.direction = EOrientation.LEFT
        self.move()

    def move_up(self, speed=None):
        if speed:
            self.set_speed(speed=None)

        self.direction = EOrientation.UP
        self.move()
    
    def move_down(self, speed=None):
        if speed:
            self.set_speed(speed)

        self.direction = EOrientation.DOWN
        self.move()
    
    def stop(self):
        self.direction = EOrientation.IDLE
        self.move()

    def move(self):
        if self.direction == EOrientation.LEFT:
            self.rect.x -= self.speed
        elif self.direction == EOrientation.RIGHT:
            self.rect.x += self.speed
        elif self.direction == EOrientation.UP:
            self.rect.y -= self.speed
        elif self.direction == EOrientation.DOWN:
            self.rect.y += self.speed
        elif self.direction == EOrientation.IDLE:
            pass
        else:
            raise ValueError('Invalid direction')
   
    def blit(self, screen):
        screen.blit(self.image, self.rect)