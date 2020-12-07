from pico2d import *
import gfw
import gobj
from bullet import *
from boss import *
import random
BORDER = 50

patterns = []

def init():
    global BOUNDARY_LEFT, BOUNDARY_RIGHT, BOUNDARY_DOWN, BOUNDARY_UP, patterns
    BOUNDARY_LEFT = -BORDER
    BOUNDARY_DOWN = -BORDER
    BOUNDARY_RIGHT = get_canvas_width() + BORDER
    BOUNDARY_UP = get_canvas_height() + BORDER
    patterns = []

def add(obj):
    patterns.append(obj)

def shot_curve(t):
    global boss
    frame = t * 100
    i = (frame%100) / 100
    b = Boss.boss
    print (i)
    p1 = b.pos[0] + 30, b.pos[1] - 10
    p2 = b.pos[0] , b.pos[1] - 60
    p3 = b.pos[0] - 30, b.pos[1] - 10
    pos = gobj.curve_line(p1, p2, p3,i)

    b1_rect = (352, 960 - 30, 31, 30)
    dx = pos[0]-b.pos[0]
    dy = pos[1]-b.pos[1]
    bullet1 = Bullet(*pos, *b1_rect, math.atan2(dy, dx))
    gfw.world.add(gfw.layer.bullet, bullet1)
    degree = 5
    bullet1.rotate(degree)


class Pattern1:
    def __init__(self):
        self.ptime = 0
        self.time = 0

    def update(self):
        self.ptime += gfw.delta_time
        self.time += gfw.delta_time
        if self.time > 0.1:
            self.time = 0
            shot_curve(self.ptime)
