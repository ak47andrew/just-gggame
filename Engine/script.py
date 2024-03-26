class GameScript:
    def __init__(self, go_data):
        self.go_data = go_data

    def __eq__(self, other):
        return isinstance(self, other if isinstance(self, type) else type(other))

    def update(self): ...
