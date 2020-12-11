from pico2d import *
import gfw
import gobj
import pattern
from player import Player
from boss import  Boss
from background import VertScrollBackground
import life_gauge

MAX_PATTERN = 2
STATE_IN_GAME, STATE_PAUSED, STATE_GAME_OVER = range(3)
def enter():
    gfw.world.init(['bg', 'missile', 'player', 'bullet', 'boss'])
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

    global sound_damage, sound_pldead, music_bg
    music_bg = load_music('res/bg_sound.mp3')
    sound_damage = load_wav('res/se_damage00.wav')
    sound_pldead = load_wav('res/se_pldead00.wav')
    sound_damage.set_volume(20)
    sound_pldead.set_volume(20)
    music_bg.set_volume(50)

    global pattern_index
    pattern_index = 0
    p1 = pattern.Pattern1()
    pattern.add(p1)
    p2 = pattern.Pattern2()
    pattern.add(p2)
    life_gauge.load()

    start_game()

def exit():
    pass


def start_game():
    global game_state
    game_state = STATE_IN_GAME

    gfw.world.clear_at(gfw.layer.missile)
    gfw.world.clear_at(gfw.layer.bullet)
#    gfw.world.remove(highscore)

    music_bg.repeat_play()

def pause_game():
    global game_state
    game_state = STATE_PAUSED
    music_bg.pause()
    player.score = max(0, player.score - 2)

def resume_game():
    global game_state
    game_state = STATE_IN_GAME
    music_bg.resume()

def update():
    gfw.world.update()
#    if MAX_PATTERN == pattern_index:
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
    global pattern_index
    if gobj.Collsion_AABB(player, Boss):
        sound_pldead.play()

    for b in gfw.world.objects_at(gfw.layer.bullet):
        if gobj.Collsion_AABB(b, player) and player.nodamage == False:
            sound_pldead.play()
            player.nodamage = True
            player.death += 1

    for b in gfw.world.objects_at(gfw.layer.missile):
        if gobj.Collsion_AABB(b, Boss) and Boss.nodamage == False:
            sound_damage.play()
            dead = Boss.decrease_life(b.power)
            if dead:
                pattern_index += 1
                Boss.life = 1000
                Boss.nodamage = True
            b.remove()
            return


if __name__ == '__main__':
    gfw.run_main()
