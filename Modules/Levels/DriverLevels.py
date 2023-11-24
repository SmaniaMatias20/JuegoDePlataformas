from Modules.Levels.LevelOne import LevelOne
from Modules.Levels.LevelTwo import LevelTwo


class DriverLevels:
    def __init__(self) -> None:
        self.levels = {"level_one": LevelOne, "level_two": LevelTwo}

    def get_level(self, name_level):
        return self.levels[name_level]((800, 500))