__import__("os").environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame
from Engine import objects
from Engine import gm
from Engine import script


class Player(script.GameScript):
    def update(self):
        self.go_data.global_pos[0] += 1


def main():
    display = pygame.display.set_mode([1280, 720])
    clock = pygame.time.Clock()

    game_manager = gm.GameManager()
    game_manager.change_camera_size([1280, 720])

    go = objects.GameObject(
        pos=[1, 1],
        size=[288, 48],
        img="sprites/1/D_Walk.png"
    )
    go.add_component(Player)

    game_manager.add_game_object(go)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        display.fill((0, 0, 0))

        game_manager.update()
        game_manager.draw(display)

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
