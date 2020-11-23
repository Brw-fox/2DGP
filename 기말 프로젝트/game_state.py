from pico2d import *
import gfw
import gobj
from player import Player
from boss import  Boss

def enter():
    gfw.world.init(['bullet', 'player', 'boss'])

    global player
    player = Player()
    gfw.world.add(gfw.layer.player, player)

    global  boss
    boss = Boss()
    gfw.world.add(gfw.layer.boss, boss)

def exit():
    pass


def update():
    gfw.world.update()

    check_collsion(boss)
    print(gfw.world.count_at(gfw.layer.bullet))


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

    for b in gfw.world.objects_at(gfw.layer.bullet):
        if gobj.Collsion_AABB(b, Boss):
            b.remove()
            return

if __name__ == '__main__':
    gfw.run_main()
