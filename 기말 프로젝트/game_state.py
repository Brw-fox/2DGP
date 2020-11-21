from pico2d import *
import gfw
from player import Player


def enter():
    gfw.world.init(['player'])

    global player
    player = Player()
    gfw.world.add(gfw.layer.player, player)

def exit():
    pass


def update():
    gfw.world.update()


def draw():
    gfw.world.draw()


def handle_event(e):
    if e.type == SDL_Quit:
        gfw.quit()
    if e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    player.handle_event(e)


if __name__ == '__main__':
    gfw.run_main()
