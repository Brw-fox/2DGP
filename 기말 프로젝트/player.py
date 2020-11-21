from pico2d import *
import gobj
import gfw

class Player:
    KEY_MAP = {
        (SDL_KEYDOWN, SDLK_UP):     (0,  1),
        (SDL_KEYDOWN, SDLK_DOWN):   (0, -1),
        (SDL_KEYDOWN, SDLK_LEFT):   (-1, 0),
        (SDL_KEYDOWN, SDLK_RIGHT):  ( 1, 0),
        (SDL_KEYUP, SDLK_UP):       (0, -1),
        (SDL_KEYUP, SDLK_DOWN):     (0,  1),
        (SDL_KEYUP, SDLK_LEFT):     ( 1, 0),
        (SDL_KEYUP, SDLK_RIGHT):    (-1, 0)
    }

    def __init__(self):
        self.image = gfw.image.load('./res/player.png')
        self.pos = get_canvas_width() // 2, 100
        self.delta = 0, 0
        self.fidx = 0
        self.action = 0
        self.time = 0
        self.speed = 300


    def update(self):
        x, y = self.pos
        dx, dy = self.delta
        x += dx * self.speed * gfw.delta_time
        y += dy * self.speed * gfw.delta_time

        self.pos = x, y

        self.time += gfw.delta_time
        frame = self.time * 10
        if self.action != 0:
            self.fidx = (int(frame) % 4) + 4
        else:
            self.fidx = int(frame) % 8

    def draw(self):
        width, height = 32, 48
        sx = self.fidx * width
        sy = (self.image.h - 48) - (self.action * height)

        self.image.clip_draw(sx, sy, width, height, *self.pos)

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Player.KEY_MAP:
            self.delta = gobj.pos_add(self.delta, Player.KEY_MAP[pair])
            dx = self.delta[0]
            self.action = \
                1 if dx < 0 else \
                2 if dx > 0 else 0
