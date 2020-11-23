from pico2d import *
import gfw
import gobj
from bullet import *
from boss import *
import random
BORDER = 50


def init():
    global BOUNDARY_LEFT, BOUNDARY_RIGHT, BOUNDARY_DOWN, BOUNDARY_UP, time
    BOUNDARY_LEFT = -BORDER
    BOUNDARY_DOWN = -BORDER
    BOUNDARY_RIGHT = get_canvas_width() + BORDER
    BOUNDARY_UP = get_canvas_height() + BORDER
    time = 0

def update():
    global time
    time += gfw.delta_time
    if time > 0.2:
        shot_curve()

def shot_curve():
    global boss, time
    time = 0
    b = Boss.boss
    #p1 = b.pos[0] + 50, b.pos[1] - 50
    #p2 = b.pos[0] , b.pos[1] - 200
    #p3 = b.pos[0] - 50, b.pos[1] - 50
    b1_rect = (352, 960 - 30, 31, 30)

    bullet1 = Bullet(random.uniform(b.pos[0]-50,b.pos[0]+50),random.uniform(b.pos[1]-40,b.pos[1]-50), random.uniform(-1,1), random.uniform(0.5,1) - 1, *b1_rect,300)
    gfw.world.add(gfw.layer.bullet, bullet1)
    degree = 5
    bullet1.rotate(degree)