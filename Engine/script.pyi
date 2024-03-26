from Engine.objects import GameObject

class GameScript:
    go_data: GameObject

    def __init__(self, go_data: GameObject): ...
    def update(self): ...
