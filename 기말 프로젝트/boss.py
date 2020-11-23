from pico2d import *
import gfw
import gobj

class Boss:
    def __init__(self):
        self.image = gfw.image.load('./res/enm01/enm1.png')
        self.pos = get_canvas_width()//2, 500
        self.delta = 0, 0
        self.fidx = 0
        self.action = 0
        self.time = 0
        self.speed =0
        self.mass = 0
        self.life = 1000
        Boss.boss = self

    def update(self):
        self.time += gfw.delta_time
        frame = self.time * 10
        self.fidx = int(frame) % 6

    def draw(self):
        width, height = 80, 80
        sx = self.fidx * width
        sy = (self.image.h - 80) - (self.action * height)

        self.image.clip_draw(sx, sy, width, height, *self.pos)

    def get_BB(self):
        hw = 40
        hh = 40
        return (self.pos[0] - hw, self.pos[0] + hw, self.pos[1] - hh, self.pos[1] + hh)


