from Modules.Characters.Object import Object
from Modules.Values.Assets import *
import random

class FallingObject(Object):
    def __init__(self, size_surface, position, type= "Stone") -> None:
        """
        Brief: Inicializa un objeto que cae.

        Descripción:
            Este método inicializa un objeto que cae con un tipo específico (por defecto "Stone").
            La posición y velocidad también son configuradas durante la inicialización.

        Parámetros:
            - size_surface (tuple): Tamaño del objeto.
            - position (tuple): Posición inicial del objeto.
            - type (str): Tipo del objeto ("Stone" por defecto).

        Retorno:
            Ninguno
        """
        self.type = type

        if self.type == "Stone":
            path = STONE
        elif self.type == "Star":
            path = STAR

        super().__init__(size_surface, position, path)

        self.set_random_position()
        speed = random.randrange(3, 7)
        self.set_speed(speed)


    def move_down(self):
        """
        Brief: Mueve el objeto hacia abajo en la pantalla.

        Descripción:
            Este método mueve el objeto hacia abajo en la pantalla. Si la posición y alcanza o supera 500 píxeles,
            se reinicia la posición del objeto en la parte superior de la pantalla. Luego, actualiza todos los rectángulos
            del objeto.

        Parámetros:
            Ninguno

        Retorno:
            Ninguno
        """
        if self.rect_main.y > 500:
            self.set_random_position()
        else:
            super().move_down()
            
        self.all_rects()

    def set_random_position(self):
        """
        Brief: Establece una posición aleatoria para el objeto.

        Descripción:
            Este método establece una posición aleatoria para el objeto dentro de los límites de la pantalla.
            La posición en el eje x se selecciona aleatoriamente entre el ancho del objeto y el ancho de la pantalla
            menos el ancho del objeto. La posición en el eje y se selecciona aleatoriamente entre -100 y -40 para
            que el objeto aparezca inicialmente fuera de la pantalla.

        Parámetros:
            Ninguno

        Retorno:
            Ninguno
        """        
        self.rect_main.x = random.randrange(self.rect_main.width, 800 - self.rect_main.width)
        self.rect_main.y = random.randrange(-100, -40)