from Modules.Characters.Object import Object
from Modules.Values.Assets import *


class Item(Object):

    def __init__(self, size, position=(0,0), type = "Coin") -> None:
        """
        Brief: Inicializa un objeto de tipo Item.

        Descripción:
            Constructor de la clase Item que crea un objeto de tipo Item con el tamaño y la posición especificados.

        Parámetros:
            size (tuple): Tamaño del objeto (ancho, alto).
            position (tuple, opcional): Posición inicial del objeto (coordenada x, coordenada y).
            type (str, opcional): Tipo de item, por defecto es "Coin".

        Retorno:
            Ninguno
        """
        self.type = type
        if self.type == "Coin":
            path = COIN
        elif self.type == "Crown":
            path = CROWN
        elif self.type == "Gem":
            path = GEM
            
        super().__init__(size, position, path)
        

    def update(self, screen, items):
        """
        Brief: Actualiza el objeto Item.

        Descripción:
            Este método actualiza el objeto Item en la pantalla, blitando los items en la posición actual.

        Parámetros:
            screen (pygame.Surface): La superficie de la pantalla.
            items (list): Lista de objetos Item.

        Retorno:
            Ninguno
        """
        self.blit_platforms(screen, items)

    def blit_platforms(self, screen, items):
        for item in items:
            item.blit(screen)