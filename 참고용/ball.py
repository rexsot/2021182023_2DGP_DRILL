import random
from pico2d import *
import game_world

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600), 60, 0

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= self.fall_speed

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, other, group):
        if group == 'boy:ball':
            game_world.remove_object(self)

    def stop(self):
        self.fall_speed = 0


class BigBall(Ball):
    MIN_FALL_SPEED = 1 # 50 pps = 1.5 meter per sec
    MAX_FALL_SPEED = 5 # 200 pps = 6 meter per sec
    image = None
    def __init__(self):
        if BigBall.image == None:
            BigBall.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, 1600-1), 500
        self.fall_speed = random.randint(BigBall.MIN_FALL_SPEED, BigBall.MAX_FALL_SPEED)

def get_bb(self):
    return self.x - 20, self.y - 20, self.x + 20, self.y + 20
