import pygame.image


class Camera:
    position: list[int]
    size: list[int]

    def __init__(self, position, size):
        self.position = position
        self.size = size


class GameObject:
    def __init__(self, pos: list[int], size: list[int], img: str):
        self.global_pos = pos
        self.global_size = size
        self.img = pygame.image.load(img).convert_alpha()
        self.scripts = []

    def update(self):
        for script in self.scripts:
            script.update()

    def draw(self, surf: pygame.Surface, cam: Camera):
        if (
                self.global_pos[0] + self.global_size[0] <= cam.position[0]
                and
                self.global_pos[1] + self.global_size[1] <= cam.position[1]
        ) or (
                self.global_pos[0] >= cam.position[0] + cam.size[0]
                and
                self.global_pos[1] >= cam.position[1] + cam.size[1]
        ):
            return
        surf.blit(self.img,
                  (
                      self.global_pos[0] - cam.position[0],
                      self.global_pos[1] - cam.position[1]
                  )
                  )

    def add_component(self, component_type):
        self.scripts.append(component_type(self))

    def remove_component(self, component):
        self.scripts.remove(component)

    def get_component(self, component):
        try:
            return self.scripts[self.scripts.index(component)]
        except ValueError:
            return None

    def get_components(self):
        return self.scripts
