from pico2d import *

open_canvas(1280, 1024)
back = load_image('TUK_GROUND.png') #640, 512
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


running = True

x = 640
y = 512

vec_x = 0
vec_y = 0
sel = 3
frame = 0


def handle_events():
    global running
    global x
    global y
    global vec_x
    global vec_y
    global sel
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN: # 키를 누를 때
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                vec_x += 1
            elif event.key == SDLK_LEFT:
                vec_x -= 1
            elif event.key == SDLK_UP:
                vec_y += 1
            elif event.key == SDLK_DOWN:
                vec_y -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                vec_x -= 1
            elif event.key == SDLK_LEFT:
                vec_x += 1
            elif event.key == SDLK_UP:
                vec_y -= 1
            elif event.key == SDLK_DOWN:
                vec_y += 1
    

while running:
    clear_canvas()
    back.draw(640, 512)
    
    character.clip_draw(frame * 100, sel * 100, 100, 100, x, y)
    # 좌이동 - 0
    # 우이동 - 100
    # 좌정지 - 200
    # 우정지 - 300
    update_canvas()

    handle_events()
    
    if (vec_x > 0):
        sel = 1
    elif (vec_x < 0):
        sel = 0
    elif (vec_x == 0):
        if (vec_y == 0):
            if (sel == 0):
                sel = 2
            elif (sel == 1):
                sel = 3
        elif (vec_y != 0):
            if (sel == 2):
                sel = 0
            elif(sel == 3):
                sel = 1


    if (0 < x + vec_x * 10 and x + vec_x * 10 < 1280):
        x += vec_x * 10
        
    if (0 < y + vec_y * 10 and y + vec_y * 10 < 1024):
        y += vec_y * 10
    
    frame = (frame + 1) % 8
    delay(0.03)

close_canvas()

