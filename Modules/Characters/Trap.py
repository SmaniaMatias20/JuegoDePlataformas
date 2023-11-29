from Modules.Characters.Object import Object
from Modules.Values.Assets import *



class Trap(Object):

    def __init__(self, size, position=(0,0), type = "One") -> None:
        """
        Brief: Inicializa un objeto trampa.

        Descripción:
            Constructor de la clase Trap que inicializa un objeto trampa según el tipo proporcionado.

        Parámetros:
            size (tuple): El tamaño del objeto trampa.
            position (tuple): La posición inicial del objeto trampa en la pantalla.
            type (str): El tipo de trampa, puede ser "One" o "Two".

        Retorno:
            Ninguno
        """
        if type == "One":
            super().__init__(size, position, TRAP_ONE)
        elif type == "Two":
            super().__init__(size, position, TRAP_TWO)
    
    def update(self, screen, traps):
        """
        Brief: Actualiza la representación gráfica de las trampas en la pantalla.

        Descripción:
            Este método actualiza la representación gráfica de las trampas en la pantalla.

        Parámetros:
            screen (pygame.Surface): La superficie de la pantalla.
            traps (list): La lista de objetos trampa.

        Retorno:
            Ninguno
        """
        self.blit_traps(screen, traps)

    def blit_traps(self, screen, traps):
        """
        Brief: Dibuja las trampas en la pantalla.

        Descripción:
            Este método dibuja las trampas en la pantalla.

        Parámetros:
            screen (pygame.Surface): La superficie de la pantalla.
            traps (list): La lista de objetos trampa.

        Retorno:
            Ninguno
        """
        for trap in traps:
            trap.blit(screen)