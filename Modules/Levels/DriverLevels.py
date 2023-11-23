from Modules.Levels.LevelOne import LevelOne
from Modules.Levels.LevelTwo import LevelTwo


class DriverLevels:
    def __init__(self) -> None:
        # Reciba un screen para pasarle a level one y ese level one pasarle a level
        self.levels = {"level_one": LevelOne, "level_two": LevelTwo}

    def get_level(self, name_level):
        return self.levels[name_level]((800, 500))