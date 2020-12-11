from pico2d import *
import gfw
import gobj
import math
SIZE = 50

class Bullet:
    def __init__(self, x, y,l,b,w,h, degree= 0, speed= 100):
        self.image = gfw.image.load('./res/shotdata.png')
        self.l, self.b ,self.w, self.h = l, b, w, h
        self.x,self.y = x, y
        self.degree = gobj.radian(degree) - math.pi
        self.dx, self.dy = math.cos(degree), math.sin(degree)
        self.speed = speed
        self.time = 0

    def update(self):
        self.x += self.dx * self.speed * gfw.delta_time
        self.y += self.dy * self.speed * gfw.delta_time
        # self.degree = gobj.calc_degree(self.x, self.y)

        if self.y > get_canvas_height() + SIZE or self.y < -SIZE \
        or self.x > get_canvas_width() + SIZE or self.x < -SIZE:
            gfw.world.remove(self)

    def draw(self):
        self.image.clip_composite_draw(self.l, self.b,self.w, self.h\
                                       ,self.degree, '', self.x, self.y, self.w, self.h)

    def remove(self):
        gfw.world.remove(self)

    def rotate(self, degree):
        rad = math.radians(degree)
        self.degree = rad

    def get_BB(self):
        hw = self.w // 2
        hh = self.h // 2
        return (self.x - hw, self.x + hw, self.y - hh, self.y + hh)

class Bullet1(Bullet):
    def update(self):
        self.time += gfw.delta_time
        self.x += self.dx * self.speed * gfw.delta_time
        self.y += self.dy * self.speed * gfw.delta_time

        if self.time > 0.1:
            self.time = 0
            if self.speed > 50:
                self.speed -= 50

        if self.y > get_canvas_height() + SIZE or self.y < -SIZE \
        or self.x > get_canvas_width() + SIZE or self.x < -SIZE:
            gfw.world.remove(self)





