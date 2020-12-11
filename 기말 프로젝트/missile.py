from pico2d import *
import gfw
import math
import gobj
SPEED = 3000
DEGREE_90 = math.radians(90)

class Missile:
    def __init__(self, x, y, delta = (0,1)):
        self.pos = x, y
        self.delta = delta
        self.image = gfw.image.load('./res/player.png')
        self.power = 2

    def update(self):
        x,y = self.pos
        dx, dy = self.delta
        x += dx * SPEED * gfw.delta_time
        y += dy * SPEED * gfw.delta_time

        if y > get_canvas_height() + self.image.h:
            gfw.world.remove(self)

        self.pos = x, y

    def draw(self):
        self.image.clip_composite_draw(68, 72, 56, 8, DEGREE_90, '', *self.pos, 56, 8)

    def remove(self):
        gfw.world.remove(self)

    def get_BB(self):
        hw = 4
        hh = 28
        return (self.pos[0] - hw, self.pos[0] + hw, self.pos[1] - hh, self.pos[1] + hh)
