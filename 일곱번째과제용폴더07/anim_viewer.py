from pico2d import *
open_canvas()
grass = load_image('grass.png')
sonic = load_image('sonic.png')
x = 0
frame = 0
# 10 540 40 50 x 80

while (x < 800):
    clear_canvas()
    grass.draw(400, 30)
    if (frame == 0):
        sonic.clip_draw(frame * 50, 410, 40, 50, x-20, 80)
        x -= 17 # 스프라이트 간격 조정
    else:
        sonic.clip_draw(frame * 50, 410, 40, 50, x, 80)
    #짜를 x/y범위, 한번에 짜를 사진의 크기 x/y, 그릴 위치 x/y
    update_canvas()
    frame = (frame + 1) % 14
    x += 10
    delay(0.05)
    get_events()

close_canvas()
