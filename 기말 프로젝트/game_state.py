from pico2d import *
import gfw


def enter():
    pass


def exit():
    pass


def update():
    pass


def draw():
    pass


def handle_event(e):
    if e.type == SDL_Quit:
        gfw.quit()
    if e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()


if __name__ == '__main__':
    gfw.run_main()
