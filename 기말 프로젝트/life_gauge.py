from pico2d import *
import gfw
import gobj

def load():
    global lg
    lg = gfw.image.load("./res/life_gauge.png")

def draw(x, y, width, rate):
    w = round(width * rate)
    lg.draw_to_origin(x, y, w, lg.h)
