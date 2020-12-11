from pico2d import *
import gfw
import gobj
import life_gauge
class Boss:
    MAX_LIFE = 1000
    def __init__(self):
        self.image = gfw.image.load('./res/enm01/enm1.png')
        self.pos = get_canvas_width()//2, 500
        self.delta = 0, 0
        self.target = 0, 0
        self.fidx = 0
        self.life = Boss.MAX_LIFE
        self.action = 0
        self.time = 0
        self.speed = 1
        self.mass = 0
        self.nodamage = False
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
        rate = self.life / Boss.MAX_LIFE
        life_gauge.draw(50, 580, 700, rate)

    def decrease_life(self, amount):
        self.life -= amount
        return self.life <= 0

    def get_BB(self):
        hw = 40
        hh = 40
        return (self.pos[0] - hw, self.pos[0] + hw, self.pos[1] - hh, self.pos[1] + hh)


