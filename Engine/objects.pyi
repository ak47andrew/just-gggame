from Engine.script import GameScript
from pygame import Surface


class GameObject:
    global_pos: list[int]
    global_size: list[int]
    img: Surface
    scripts: list[GameScript]

    def __init__(self, pos: list[int], size: list[int], img: str): ...
    def update(self): ...
    def draw(self, surf: Surface, cam: Camera): ...
    def add_component(self, component: type): ...
    def remove_component(self, component: GameScript): ...
    def get_component(self, component: GameScript) -> GameScript | None: ...
    def get_components(self) -> list[GameScript]: ...


class Camera:
    position: list[int]
    size: list[int]

    def __init__(self, position: list[int], size: list[int]): ...
