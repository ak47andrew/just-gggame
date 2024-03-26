import pygame

from Engine.objects import Camera


class GameManager:
    def __init__(self):
        self.gameObjects = []
        self.camera = Camera(
            position=[0, 0],
            size=[0, 0]
        )

    def add_game_object(self, obj):
        self.gameObjects.append(obj)

    def delete_game_object(self, obj):
        self.gameObjects.remove(obj)

    def get_game_object(self, obj):
        return self.gameObjects[self.gameObjects.index(obj)]

    def get_game_objects(self):
        return self.gameObjects

    def draw(self, surface: pygame.Surface):
        for gameObject in self.gameObjects:
            gameObject.draw(surface, self.camera)

    def update(self):
        for gameObject in self.gameObjects:
            gameObject.update()

    def change_camera_position(self, position):
        self.camera.position = position

    def change_camera_size(self, size):
        self.camera.size = size
