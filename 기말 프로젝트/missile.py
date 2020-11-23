from pico2d import *
import gfw

SPEED = 3000
DEGREE_90 = 90 * 3.14 / 180
class Missile:
    def __init__(self, x, y, delta = (0,1)):
        self.pos = x, y
        self.delta = delta
        self.image = gfw.image.load('./res/player.png').clip_image(68, 72, 56, 8)
        self.image.opacify(0.1)
    def update(self):
        x,y = self.pos
        dx, dy = self.delta
        x += dx * SPEED * gfw.delta_time
        y += dy * SPEED * gfw.delta_time

        if y > get_canvas_height() + self.image.h:
            gfw.world.remove(self)

        self.pos = x, y

    def draw(self):
        self.image.rotate_draw(DEGREE_90, *self.pos)

    def remove(self):
        gfw.world.remove(self)

    def get_BB(self):
        hw = 4
        hh = 28
        return (self.pos[0] - hw, self.pos[0] + hw, self.pos[1] - hh, self.pos[1] + hh)
