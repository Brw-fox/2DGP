# 이벤트 드리븐 방식 get_event -> 이벤트큐에있는 이벤트들을 가져옴
#pico2d는 pysdl라이브러리에서 가져오는것. 이벤트는 pysdl을 찾아보는게 좋다.
from pico2d import *

def handle_evnets():
    global running, dx, x, y
    evts = get_events()
    for e in evts:
        if e.type == SDL_Quit:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
            elif e.key == SDLK_LEFT:
                dx -= 1
            elif e.key == SDLK_RIGHT:
                dx += 1
            print('keydown', dx)
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_LEFT:
                dx += 1
            elif e.key == SDLK_RIGHT:
                dx -= 1
            print('keyup', dx)
        elif e.type == SDL_MOUSEMOTION:
            x, y = e.x, get_canvas_height() - 1 - e.y
            #e.x , e.y는 윈도우 API의 좌표계를 따른다. 마우스를 따라가게하려면 캔버스의 높이를구해서 빼주어야함.
#파이썬의 함수특성, evts변수에 wirte하고있음 -> 지역변수가 됨  running도 마찬가지. 이 지역내에서만 쓰이는 함수가 되어버림.
#해결법 -> global로 선언해주어야함 즉 esc를 눌러도 running이 false가 되지않음.
open_canvas()

gra = load_image('grass.png')
ch = load_image('run_animation.png')

running = True
x,y = 400,85 #파이썬의 튜플
dx = 0
fidx = 0
while x < 800:
    clear_canvas()
    gra.draw(400,30)
    ch.clip_draw(fidx*100,0,100,100,x,y)
    update_canvas()

    handle_evnets()

    x += dx
    fidx = (fidx + 1) % 8
    delay(0.01)

    if running == False:
        break

close_canvas()

