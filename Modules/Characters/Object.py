from Modules.Values.EOrientation import EOrientation
import pygame as py


class Object:

    def __init__(self, size_surface, position, image = None) -> None:
        """
        Brief: Inicializa un objeto de la clase Object.

        Descripción:
            Este método inicializa un objeto de la clase Object. Puede recibir una imagen
            preexistente o crear una superficie vacía.

        Parámetros:
            size_surface (tuple): Tamaño de la superficie del objeto.
            position (tuple): Posición inicial del objeto en la pantalla.
            image (pygame.surface.Surface, opcional): Imagen preexistente para el objeto.

        Retorno:
            Ninguno
        """
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
        """
        Brief: Actualiza los rectángulos asociados al objeto.

        Descripción:
            Este método debe llamarse para mantener sincronizados los rectángulos
            del objeto después de realizar cambios en su posición.

        Parámetros:
            Ninguno

        Retorno:
            Ninguno
        """
        self.all_rects()

    def get_rectangles(self, main:py.Rect):
        """
        Brief: Obtiene los rectángulos asociados al rectángulo principal.

        Descripción:
            Este método devuelve un diccionario que contiene el rectángulo principal
            y sus lados (superior, inferior, derecho, izquierdo).

        Parámetros:
            main (py.Rect): El rectángulo principal.

        Retorno:
            dict: Diccionario que contiene los rectángulos asociados al principal.
        """
        dictionary = {}
        if len(main) > 0 and isinstance(main, py.Rect):
            dictionary["main"] = main
            dictionary["bottom"] = py.Rect(main.left, main.bottom - 10, main.width, 10)
            dictionary["right"] = py.Rect(main.right - 10, main.top, 10, main.height)
            dictionary["left"] = py.Rect(main.left, main.top, 10, main.height)
            dictionary["top"] = py.Rect(main.left, main.top , main.width, 10)
        return dictionary

    def all_rects(self):
        """
        Brief: Actualiza los rectángulos asociados al objeto.

        Descripción:
            Este método debe llamarse para mantener sincronizados los rectángulos
            del objeto después de realizar cambios en su posición.

        Parámetros:
            Ninguno

        Retorno:
            Ninguno
        """
        self.rect["bottom"].y = self.rect["main"].y + self.rect["main"].h - 10
        self.rect["right"].y = self.rect["main"].y
        self.rect["left"].y = self.rect["main"].y
        self.rect["top"].y = self.rect["main"].y
        self.rect["bottom"].x = self.rect["main"].x 
        self.rect["right"].x = self.rect["main"].x + self.rect["main"].w - 10
        self.rect["left"].x = self.rect["main"].x
        self.rect["top"].x = self.rect["main"].x
        
    def set_speed(self, speed):
        """
        Brief: Establece la velocidad del objeto.

        Descripción:
            Este método establece la velocidad del objeto.

        Parámetros:
            speed (int): La velocidad del objeto.

        Retorno:
            Ninguno
        """
        self.speed = speed

    def move_right(self, speed=None):
        """
        Brief: Mueve el objeto hacia la derecha.

        Descripción:
            Este método mueve el objeto hacia la derecha. Si se proporciona la velocidad,
            actualiza la velocidad del objeto antes de moverlo.

        Parámetros:
            speed (int, opcional): La velocidad del objeto. Si se proporciona, actualiza la velocidad.

        Retorno:
            Ninguno
        """
        if speed:
            self.set_speed(speed=None)

        self.direction = EOrientation.RIGHT
        self.move()

    def move_left(self, speed=None):
        """
        Brief: Mueve el objeto hacia la izquierda.

        Descripción:
            Este método mueve el objeto hacia la izquierda. Si se proporciona la velocidad,
            actualiza la velocidad del objeto antes de moverlo.

        Parámetros:
            speed (int, opcional): La velocidad del objeto. Si se proporciona, actualiza la velocidad.

        Retorno:
            Ninguno
        """
        if speed:
            self.set_speed(speed=None)
        self.direction = EOrientation.LEFT
        self.move()

    def move_up(self, speed=None):
        """
        Brief: Mueve el objeto hacia arriba.

        Descripción:
            Este método mueve el objeto hacia arriba. Si se proporciona la velocidad,
            actualiza la velocidad del objeto antes de moverlo.

        Parámetros:
            speed (int, opcional): La velocidad del objeto. Si se proporciona, actualiza la velocidad.

        Retorno:
            Ninguno
        """
        if speed:
            self.set_speed(speed=None)

        self.direction = EOrientation.UP
        self.move()
    
    def move_down(self, speed=None):
        """
        Brief: Mueve el objeto hacia abajo.

        Descripción:
            Este método mueve el objeto hacia abajo. Si se proporciona la velocidad,
            actualiza la velocidad del objeto antes de moverlo.

        Parámetros:
            speed (int, opcional): La velocidad del objeto. Si se proporciona, actualiza la velocidad.

        Retorno:
            Ninguno
        """
        if speed:
            self.set_speed(speed)

        self.direction = EOrientation.DOWN
        self.move()
    
    def stop(self):
        """
        Brief: Detiene el movimiento del objeto.

        Descripción:
            Este método detiene el movimiento del objeto.

        Parámetros:
            Ninguno

        Retorno:
            Ninguno
        """
        self.direction = EOrientation.IDLE
        self.move()

    def move(self):
        """
        Brief: Mueve el objeto en la dirección especificada.

        Descripción:
            Este método mueve el objeto en la dirección especificada por la propiedad "direction".
            Si la dirección es "LEFT", la posición en el eje x disminuirá.
            Si la dirección es "RIGHT", la posición en el eje x aumentará.
            Si la dirección es "UP", la posición en el eje y disminuirá.
            Si la dirección es "DOWN", la posición en el eje y aumentará.
            Si la dirección es "IDLE", el objeto no se moverá.

        Parámetros:
            Ninguno

        Retorno:
            Ninguno
        """
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
        """
        Brief: Carga una imagen desde un archivo y la escala al tamaño especificado.

        Descripción:
            Este método carga una imagen desde un archivo en la ruta especificada y la escala al tamaño
            dado por el parámetro "size_surface".

        Parámetros:
            path (str): La ruta al archivo de imagen.
            size_surface (tuple): La tupla que representa el tamaño deseado de la imagen (ancho, alto).

        Retorno:
            py.surface.Surface: La imagen cargada y escalada.
        """
        image = py.image.load(path)
        image = py.transform.scale(image, size_surface)

        return image
    
    def sound_effects(self, path, volume):
        """
        Brief: Reproduce un efecto de sonido.

        Descripción:
            Este método carga y reproduce un efecto de sonido desde el archivo especificado en "path".
            Se puede ajustar el volumen mediante el parámetro "volume".

        Parámetros:
            path (str): La ruta al archivo de sonido.
            volume (float): El volumen del sonido, un valor entre 0.0 (sin sonido) y 1.0 (volumen máximo).

        Retorno:
            Ninguno
        """
        music = py.mixer.Sound(path)
        music.set_volume(volume)
        music.play()

    def blit(self, screen):
        """
        Brief: Dibuja el objeto en la pantalla.

        Descripción:
            Este método dibuja el objeto en la pantalla en la posición especificada por sus rectángulos.

        Parámetros:
            screen (py.Surface): La superficie de la pantalla donde se dibujará el objeto.

        Retorno:
            Ninguno
        """
        screen.blit(self.image, self.rect_main)
