from pico2d import *
import gfw
import gobj
import pattern
from player import Player
from boss import  Boss
from background import VertScrollBackground

def enter():
    gfw.world.init(['bg','missile', 'player', 'bullet', 'boss'])
    pattern.init()

    global player
    player = Player()
    gfw.world.add(gfw.layer.player, player)

    global boss
    boss = Boss()
    gfw.world.add(gfw.layer.boss, boss)

    global bg
    bg = VertScrollBackground('./res/world02.png')
    leaf = VertScrollBackground('./res/world02c2.png')
    gfw.world.add(gfw.layer.bg, bg)
    gfw.world.add(gfw.layer.bg, leaf)

    global pattern_index
    pattern_index = 0
    p1 = pattern.Pattern1()
    pattern.add(p1)

def exit():
    pass


def update():
    gfw.world.update()
    pattern.patterns[pattern_index].update()
    check_collsion(boss)


def draw():
    gfw.world.draw()


def handle_event(e):
    if e.type == SDL_Quit:
        gfw.quit()
    if e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    player.handle_event(e)

def check_collsion(Boss):
    if gobj.Collsion_AABB(player, Boss):
        pass

    for b in gfw.world.objects_at(gfw.layer.missile):
        if gobj.Collsion_AABB(b, Boss):
            b.remove()
            return

if __name__ == '__main__':
    gfw.run_main()
