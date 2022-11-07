import random
from pico2d import *

X_MAX = 1000
Y_MAX = 500

open_canvas(X_MAX, Y_MAX)

PIXEL_PER_METER = 1 # 1 pixel 1 cm
RUN_SPEED_KMPH = 50.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 10.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 1


class Bird:
    def __init__(self):
        self.x, self.y = random.randint(100, 900), 100
        self.frame = 0
        self.face_dir = 1
        self.image = load_image('bird_animation.png')

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME) % 15# 0-14
        self.x += self.face_dir * RUN_SPEED_PPS
        if self.x >= X_MAX or self.x <= 0:
            self.face_dir *= -1

# 100, 100 / 180, 160
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(int(self.frame) % 5 * 180, int(self.frame) // 5 * 170, 180, 160, self.x, self.y, 100, 100)
        else:
            self.image.clip_composite_draw(int(self.frame) % 5 * 180, int(self.frame) // 5 * 170, 180, 160, 0, 'h', self.x, self.y, 100, 100)

team = [Bird() for i in range(10)]

while(1):
    for bird in team:
        bird.update()
        bird.draw()

    delay(0.05)
    update_canvas()
    clear_canvas()

