from pico2d import *
import gfw
import gobj
from bullet import *
from boss import *
from player import *
import random
from helper import *
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

    p1 = b.pos[0] + 30, b.pos[1]
    p2 = b.pos[0] , b.pos[1] - 60
    p3 = b.pos[0] - 30, b.pos[1] - 10
    pos = gobj.curve_line(p1, p2, p3,i)

    b1_rect = (352, 960 - 30, 31, 30)
    dx = pos[0]-b.pos[0]
    dy = pos[1]-b.pos[1]
    rx = random.uniform(dx-10, dx+10)
    ry = random.uniform(dy-10, dy+10)
    rs = random.uniform(100,200)
    bullet1 = Bullet(*pos, *b1_rect, math.atan2(ry, rx), rs)
    gfw.world.add(gfw.layer.bullet, bullet1)

def shot_circle_to_player():
    global player, boss
    b = Boss.boss
    p = Player.player

    dx = p.pos[0] - b.pos[0]
    dy = p.pos[1] - b.pos[1]
    b1_rect = (768, 960 - 15, 16, 15)
    to_player = math.atan2(dy, dx)
    print(to_player)
    bullet1 = Bullet(b.pos[0], b.pos[1], *b1_rect, to_player, 400)
    gfw.world.add(gfw.layer.bullet, bullet1)


def shot_to_player():
    global player, boss
    b = Boss.boss
    p = Player.player

    dx = p.pos[0] - b.pos[0]
    dy = p.pos[1] - b.pos[1]

    b1_rect = (737,98,766,124)

    to_player = math.atan2(dy, dx)
    bullet1 = Bullet(b.pos[0], b.pos[1], *b1_rect, to_player, 400)
    gfw.world.add(gfw.layer.bullet, bullet1)
class Pattern1:
    def __init__(self):
        self.ptime = 0
        self.time = 0

    def update(self):
        self.ptime += gfw.delta_time
        self.time += gfw.delta_time
        if self.time > 0.08:
            self.time = 0
            shot_curve(self.ptime)

class Pattern2:
    target = (400, 300)
    def __init__(self):
        self.time = 0
        self.btime = 0
        self.wtime = 0
    def update(self):
        global boss
        b = Boss.boss
        self.wtime += gfw.delta_time
        self.btime += gfw.delta_time
        self.time += gfw.delta_time

        if self.wtime < 2:
            set_target(b, Pattern2.target)
            move_toward_obj(b)
            return

        if self.btime > 3:
            self.time = 0
            shot_to_player()

        b.nodamage = False
        if self.time > 1:
            self.time = 0
            shot_circle_to_player()
