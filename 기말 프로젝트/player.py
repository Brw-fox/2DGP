from pico2d import *
import gobj
from missile import Missile
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
    KEYDOWN_Z = (SDL_KEYDOWN, SDLK_z)
    KEYDOWN_SHIFT = (SDL_KEYDOWN, SDLK_LSHIFT)
    KEYUP_Z = (SDL_KEYUP, SDLK_z)
    KEYUP_SHIFT = (SDL_KEYUP, SDLK_LSHIFT)
    SHOOTHING_INTERVAL = 0.05
    ROTATING_SLOWEFF = 3.14 / 180
    def __init__(self):
        self.image = gfw.image.load('./res/player.png')
        self.font = gfw.font.load('res/ConsolaMalgun.ttf', 35)
        self.slowEffImage = gfw.image.load('./res/eff_sloweffect.png').clip_image(27,27,10,10) # 임시, 원래값: 0,0,64,64
        self.pos = get_canvas_width() // 2, 100
        self.delta = 0, 0
        self.fidx = 0
        self.action = 0
        self.time = 0
        self.shooting_time = 0
        self.speed = 300
        self.degree = 0
        self.slowing = False
        self.shooting = False
        self.deathcount = 0
        global BOUNDARY_LEFT, BOUNDARY_RIGHT, BOUNDARY_DOWN, BOUNDARY_UP
        BOUNDARY_LEFT = 16
        BOUNDARY_DOWN = 24
        BOUNDARY_RIGHT = get_canvas_width() - BOUNDARY_LEFT
        BOUNDARY_UP = get_canvas_height() - BOUNDARY_DOWN

    def update(self):
        x, y = self.pos
        dx, dy = self.delta
        x += dx * self.speed * gfw.delta_time
        y += dy * self.speed * gfw.delta_time

        x = clamp(BOUNDARY_LEFT, x, BOUNDARY_RIGHT)
        y = clamp(BOUNDARY_DOWN, y, BOUNDARY_UP)
        self.pos = x, y

        self.time += gfw.delta_time
        self.shooting_time += gfw.delta_time
        frame = self.time * 10
        if self.action != 0:
            self.fidx = (int(frame) % 4) + 4
        else:
            self.fidx = int(frame) % 8

        if self.shooting and self.shooting_time > Player.SHOOTHING_INTERVAL:
            self.fire()

        self.degree += Player.ROTATING_SLOWEFF

    def draw(self):
        width, height = 32, 48
        sx = self.fidx * width
        sy = (self.image.h - 48) - (self.action * height)

        pos = 600,500

        self.font.draw(*pos, 'Death : %.1i' % self.deathcount, (0,0,0))

        self.image.clip_draw(sx, sy, width, height, *self.pos)

        if self.slowing:
            self.slowEffImage.rotate_draw(self.degree, *self.pos)

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Player.KEY_MAP:
            self.delta = gobj.pos_add(self.delta, Player.KEY_MAP[pair])
            dx = self.delta[0]
            self.action = \
                1 if dx < 0 else \
                2 if dx > 0 else 0

        if pair == Player.KEYDOWN_Z:
            self.shooting = True
        elif pair == Player.KEYUP_Z:
            self.shooting = False

        if pair == Player.KEYDOWN_SHIFT:
            self.slowing = True
            self.speed = 100
        elif pair == Player.KEYUP_SHIFT:
            self.slowing = False
            self.speed = 300


    def fire(self):
        self.shooting_time = 0
        x, y = self.pos
        halfX = 16 # 32 // 2
        halfY = 24 # 48 // 2
        m1 = Missile(x - halfX, y + halfY)
        m2 = Missile(x + halfX, y + halfY)
        gfw.world.add(gfw.layer.missile, m1)
        gfw.world.add(gfw.layer.missile, m2)

    def get_BB(self):
        hw = 5
        hh = 5
        return (self.pos[0] - hw, self.pos[0] + hw, self.pos[1] - hh, self.pos[1] +hh)

