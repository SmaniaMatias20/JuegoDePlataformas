from Modules.Levels.LevelOne import LevelOne
from Modules.Levels.LevelThree import LevelThree
from Modules.Levels.LevelTwo import LevelTwo


class DriverLevels:
    def __init__(self) -> None:
        self.levels = {"level_one": LevelOne, "level_two": LevelTwo, "level_three": LevelThree}

    def get_level(self, name_level):
        return self.levels[name_level]((800, 500))