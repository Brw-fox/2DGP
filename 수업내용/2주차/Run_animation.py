# 2020_09_14_(2)

from pico2d import *

open_canvas()

gra = load_image('grass.png')
ch = load_image('animation_sheet.png')


x = 0
frame_index = 0
action = 1

while x < 800:
    clear_canvas()
    gra.draw(400, 30)
    ch.clip_draw(frame_index * 100, action * 100, 100, 100, x, 85)
    update_canvas()

    get_events()
    # for e in evts:
    # print(e)

    x += 2
    # frame_index += 1
    # if frame_index >= 8:frame_index = 0 -> if를 써서 분기를 하고있음. CPU에서 분기는 좋지않음.
    frame_index = (frame_index + 1) % 8

    if x % 100 == 0:
        action = (action + 1) % 4

    delay(0.02)

delay(1)

clear_canvas_now()

delay(1)

close_canvas()
