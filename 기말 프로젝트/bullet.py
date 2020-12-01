from pico2d import *
import gfw
import gobj
import math
SIZE = 50

class Bullet:
    def __init__(self, x, y, dx, dy,l,b,w,h, speed= 100, degree= 0):
        self.image = gfw.image.load('./res/shotdata.png')
        self.rect = (l,b,w,h)
        self.x,self.y = x, y
        self.dx, self.dy = dx, dy
        self.speed = speed
        self.degree = degree

    def update(self):
        self.x += self.dx * self.speed * gfw.delta_time
        self.y += self.dy * self.speed * gfw.delta_time
        # self.degree = gobj.calc_degree(self.x, self.y)

        if self.y > get_canvas_height() + SIZE or self.y < -SIZE \
        or self.x > get_canvas_width() + SIZE or self.x < -SIZE:
            gfw.world.remove(self)

    def draw(self):
        self.image.clip_composite_draw(*self.rect, self.degree, '', self.x, self.y, 31, 30)

    def remove(self):
        gfw.world.remove(self)

    def rotate(self, degree):
        rad = math.radians(degree)
        self.degree = rad

    def get_BB(self):
        hw = self.image.w // 2
        hh = self.image.h // 2
        return (self.x - hw, self.x + hw, self.y - hh, self.y + hh)
