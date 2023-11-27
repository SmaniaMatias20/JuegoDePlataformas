import pygame as py

from Modules.Values.EOrientation import EOrientation

class Object:

    def __init__(self, size_surface, position, image = None) -> None:

        if type(image) == py.surface.Surface:
            self.image = image
        elif image == None:
            self.image = py.Surface(size_surface)
        else:
            self.image = self.load_image(image, size_surface)

        self.rect_main = self.image.get_rect()
        self.rect_main.x = position[0]
        self.rect_main.y = position[1]
        self.rect = self.get_rectangles(self.rect_main)
        self.direction = EOrientation.IDLE
    
    def update(self):
        self.all_rects()


    def get_rectangles(self, main:py.Rect):
        dictionary = {}
        if len(main) > 0 and isinstance(main, py.Rect):
            dictionary["main"] = main
            dictionary["bottom"] = py.Rect(main.left, main.bottom - 10, main.width, 10)
            dictionary["right"] = py.Rect(main.right - 10, main.top, 10, main.height)
            dictionary["left"] = py.Rect(main.left, main.top, 10, main.height)
            dictionary["top"] = py.Rect(main.left, main.top , main.width, 10)
        return dictionary

    def all_rects(self):    
        self.rect["bottom"].y = self.rect["main"].y + self.rect["main"].h - 10
        self.rect["right"].y = self.rect["main"].y
        self.rect["left"].y = self.rect["main"].y
        self.rect["top"].y = self.rect["main"].y
        self.rect["bottom"].x = self.rect["main"].x 
        self.rect["right"].x = self.rect["main"].x + self.rect["main"].w - 10
        self.rect["left"].x = self.rect["main"].x
        self.rect["top"].x = self.rect["main"].x

    
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
            self.rect_main.x -= self.speed
        elif self.direction == EOrientation.RIGHT:
            self.rect_main.x += self.speed
        elif self.direction == EOrientation.UP:
            self.rect_main.y -= self.speed
        elif self.direction == EOrientation.DOWN:
            self.rect_main.y += self.speed
        elif self.direction == EOrientation.IDLE:
            pass
        else:
            raise ValueError('Invalid direction')
   
    def load_image(self, path, size_surface):
        image = py.image.load(path)
        image = py.transform.scale(image, size_surface)

        return image
    
    def sound_effects(self, path, volume):
        music = py.mixer.Sound(path)
        music.set_volume(volume)
        music.play()

    def blit(self, screen):
        screen.blit(self.image, self.rect_main)
