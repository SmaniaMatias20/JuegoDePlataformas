from Modules.Levels.LevelOne import LevelOne
from Modules.Levels.LevelThree import LevelThree
from Modules.Levels.LevelTwo import LevelTwo


class DriverLevels:
    def __init__(self) -> None:
        """
        Brief: Constructor de la clase DriverLevels.

        Descripción:
            Inicializa un objeto DriverLevels con un diccionario que asocia nombres de niveles con las clases
            correspondientes de esos niveles.

        Parámetros:
            Ninguno

        Retorno:
            Ninguno
        """
        self.levels = {"level_one": LevelOne, "level_two": LevelTwo, "level_three": LevelThree}

    def get_level(self, name_level):
        """
        Brief: Obtiene una instancia de un nivel específico.

        Descripción:
            Este método devuelve una instancia de la clase correspondiente al nivel especificado.

        Parámetros:
            - name_level (str): Nombre del nivel para el cual se desea obtener una instancia.

        Retorno:
            object: Instancia de la clase del nivel especificado.
        """
        return self.levels[name_level]((800, 500))