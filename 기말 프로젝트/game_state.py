from pico2d import *
import gfw
import gobj
import pattern
from player import Player
from boss import Boss
from background import VertScrollBackground

STATE_IN_GAME, STATE_PAUSED = range(2)

def enter():
    gfw.world.init(['bg','missile','bullet', 'player', 'boss'])
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

    global state
    state = STATE_IN_GAME


def exit():
    pass


def update():
    if state == STATE_PAUSED:
        return

    gfw.world.update()
    pattern.update()
    check_collsion()
    print(gfw.world.count_at(gfw.layer.bullet))



def draw():
    gfw.world.draw()


def handle_event(e):
    global state
    if e.type == SDL_Quit:
        gfw.quit()
    if e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            state = STATE_PAUSED

    player.handle_event(e)

def check_collsion():
    if gobj.Collsion_AABB(player, boss):
        pass

    for m in gfw.world.objects_at(gfw.layer.missile):
        if gobj.Collsion_AABB(m, boss):
            m.remove()
            return

    for b in gfw.world.objects_at(gfw.layer.bullet):
        if gobj.Collsion_AABB(b, player):
            b.remove()
            player.deathcount += 1
            return


if __name__ == '__main__':
    gfw.run_main()
