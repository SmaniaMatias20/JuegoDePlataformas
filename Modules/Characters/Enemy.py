from Modules.Characters.Object import Object


class Enemy(Object):
    def __init__(self, size, position=(0,0), speed=5) -> None:


        
        super().__init__(size, position, self.current_animation[self.step_counter]) 