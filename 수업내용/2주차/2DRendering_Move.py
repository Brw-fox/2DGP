# 2020_09_14_(1)

from pico2d import *
# pico2d 에서 모든것(*)을 import해옴 -> 함수를 자기가만든것처럼 그냥사용가능
# import pico2d -> pico2d는 모듈객체 / 모듈전체를 가져옴

# lattice -> 모눈에 관련된 함수
open_canvas()

gra = load_image('grass.png')
ch = load_image('character.png')
# pico2d는 특성상, open_canvas()를 한뒤에 load_image()를 해야함.
# OS 관계없이, 모든 프로세스는 현재 디렉토리라는 개념이있음. OS모듈의 getcwd(getCurrentWorkingDirectory)함수로 위치를 알 수있음.
# os.chdir로 현재 디렉토리를 옮길수있음 경로입력시 \\('\'하나만쓰면 string escape로인식) 또는 / 사용
# shell 이아닌 실행프로그램으로 실행하면 자동으로 프로그램의 경로에서 실행.


# 캐릭터 화면에 100,100좌표마다 그리기
# for y in range(0, 600+1, 100):
#     for x in range(0, 800+1, 100):
#         ch.draw_now((x,y))


x = 0

while x < 800:
    clear_canvas()
    gra.draw(400, 30)
    ch.draw(x, 85)
    update_canvas() # 여태까지 back_buffer에 그린것을 front_buffer로 옮김

    #evts = get_events()  이벤트 처리를 위해 이벤트 큐에서 이벤트를 가져오는것. 이벤트 큐를 비워주어야 계속해서 이벤트가 큐에 쌓임.
    #for e in evts:
    #     print(e)
    get_events()
    x += 2
    delay(0.02)
    

delay(2)

clear_canvas_now()

delay(2)

close_canvas()
