from pico2d import *
from math import *


def pos_add(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return x1+x2, y1+y2

def Collsion_AABB(a, b):
    (aMinX, aMaxX, aMinY, aMaxY) = a.get_BB()
    (bMinX, bMaxX, bMinY, bMaxY) = b.get_BB()

    if aMinX > bMaxX:
        return False
    if aMaxX < bMinX:
        return False
    if aMinY > bMaxY:
        return False
    if aMaxY < bMinY:
        return False

    return True

def curve_line(p1, p2, p3, t):
    x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
    y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]
    print(x,y)
    return (x, y)

def calc_degree(x, y):
    a = (x / fabs(x), y / fabs(y))
    b = (1, 0)

    c = (a[0] - b[0], a[1] - b[1])
    c = (c[0] / fabs(c[0]), c[1] / fabs(c[1]))

    return degrees(acos(c))


def radian(d):
    return math.radians(d)

def set_image_alpha(image, alpha):
    pico2d.SDL_SetTextureAlphaMod(image.texture, int(alpha))