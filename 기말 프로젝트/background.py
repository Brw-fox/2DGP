import gfw
from gobj import *

class VertScrollBackground:
    def __init__(self, imageName):
        self.imageName = imageName
        self.image = gfw.image.load(imageName)
        self.cw, self.ch = get_canvas_width(), get_canvas_height()
        self.scroll = 0
        self.speed = 15

    def update(self):
        self.scroll += self.speed * gfw.delta_time

    def set_scroll(self, scroll):
        self.scroll = scroll

    def draw(self):
        left, bottom = 0, 0
        page = self.image.h * self.cw // self.image.w
        curr = int(-self.scroll) % page
        if curr > 0:
            sh = int(1 + self.image.w * curr / self.cw)
            sb = self.image.h - sh
            src = 0, sb, self.image.w, sh
            dh = int(sh * self.cw / self.image.w)
            dst = 0, curr - dh, self.cw, dh
            self.image.clip_draw_to_origin(*src, *dst)
        dst_hegiht = round(self.image.h * self.cw / self.image.w)
        while curr + dst_hegiht < self.ch:
            dst = 0, curr, self.cw, dst_hegiht
            self.image.draw_to_origin(*dst)
            curr += dst_hegiht
        if curr < self.ch:
            dh = self.ch - curr
            sh = int(1 + self.image.w * dh / self.cw)
            src = 0, 0, self.image.w, sh
            dh = int(sh * self.cw / self.image.w)
            dst = 0, curr, self.cw, dh
            self.image.clip_draw_to_origin(*src, *dst)