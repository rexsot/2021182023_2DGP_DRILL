from pico2d import *
import math

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
r = 235



def moverec():
    global x
    global y
    while(x < 780):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 2
        delay(0.01)
    while(y < 560):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y += 2
        delay(0.01)
    while(x > 20):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 2
        delay(0.01)
    while(y > 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y -= 2
        delay(0.01)
    while(x < 400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 2
        delay(0.01)

# 원점 좌표 (400 ,325) 

def movecir():
    global x
    global y
    r = 235
    c = 90 #각도 (270 -> 360(0) -> 270
    while(c < 360):
        x = 400 - r * math.cos(c / 360 * 2 * math.pi)
        y = 325 - r * math.sin(c / 360 * 2 * math.pi)
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        c += 0.1
        
    c = 0
    
    while(c < 90):
        x = 400 - r * math.cos(c / 360 * 2 * math.pi)
        y = 325 - r * math.sin(c / 360 * 2 * math.pi)
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        c += 0.1
    
    
while(1):
    moverec()
    movecir()

close_canvas()
