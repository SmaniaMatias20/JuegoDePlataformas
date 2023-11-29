from Modules.Characters.Object import Object
from Modules.Values.Assets import *



class Platform(Object):

    def __init__(self, size, position=(0,0), type = "One") -> None:
        """
        Brief: Inicializa un objeto de la clase Platform.

        Descripción:
            Este método inicializa un objeto de la clase Platform con las propiedades específicas
            del tipo de plataforma especificado por el parámetro "type".

        Parámetros:
            size (tuple): El tamaño de la plataforma.
            position (tuple, opcional): La posición inicial de la plataforma. Por defecto, es (0, 0).
            type (str, opcional): El tipo de plataforma. Por defecto, es "One".

        Retorno:
            Ninguno
        """
        if type == "One":
            super().__init__(size, position, PLATFORM_IMAGE)
        
    def update(self, screen, platforms):
        """
        Brief: Actualiza el objeto y lo muestra en la pantalla junto con las plataformas.

        Descripción:
            Este método actualiza el objeto y muestra tanto el objeto como las plataformas en la pantalla.

        Parámetros:
            screen (pygame.Surface): La superficie de la pantalla.
            platforms (list): Lista de plataformas a mostrar.

        Retorno:
            Ninguno
        """
        super().update()
        self.blit_platforms(screen, platforms)


    def blit_platforms(self, screen, platforms):
        """
        Brief: Muestra las plataformas en la pantalla.

        Descripción:
            Este método muestra las plataformas en la pantalla.

        Parámetros:
            screen (pygame.Surface): La superficie de la pantalla.
            platforms (list): Lista de plataformas a mostrar.

        Retorno:
            Ninguno
        """
        for platform in platforms:
            platform.blit(screen)
    

                 

