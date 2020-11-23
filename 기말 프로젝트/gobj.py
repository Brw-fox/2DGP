from pico2d import *

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
        return  False
    if aMaxY < bMinY:
        return False

    return True
