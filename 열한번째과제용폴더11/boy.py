from pico2d import *
import game_framework

RD, LD, RU, LU, TIMER, AD = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_a): AD
}

table = {
    "SLEEP": {"HIT": "WAKE"},
    "WAKE": {"TIMER10": "SLEEP"}
}

class IDLE:
    @staticmethod
    def enter(self, event):
        print('ENTER IDLE')
        self.timer = 1000
        self.dir = 0

    @staticmethod
    def exit(self):
        print('EXIT IDLE')

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0:
            self.add_event(TIMER)

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

class RUN:
    def enter(self, event):
        print('ENTER RUN')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    def exit(self):
        print('EXIT RUN')
        self.face_dir = self.dir

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800)

    def draw(self):
        print('DRAW RUN')
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)

class SLEEP:
    def enter(self, event):
        print('ENTER SLEEP')
        self.frame = 0

    def exit(self):
        pass

    def do(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        print('DRAW SLEEP')
        if self.face_dir == -1:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100, -3.141592 / 2, '', self.x + 25, self.y - 25, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100, 3.141592 / 2, '', self.x - 25, self.y - 25, 100, 100)

class AUTO_RUN:
    def enter(self, event):
        print('ENTER AUTO_RUN')
        self.frame = 0
        self.dir = self.face_dir

    def exit(self):
        print('EXIT AUTO_RUN')
        self.face_dir = self.dir

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x == 0 or self.x == 800:
            self.dir *= -1

    def draw(self):
        print('DRAW AUTO_RUN')
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y + 40, 200, 200)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y + 40, 200, 200)


next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, AD: AUTO_RUN},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, AD: AUTO_RUN},
    SLEEP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, AD: AUTO_RUN},
    AUTO_RUN: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, AD: IDLE}
}

class Boy:

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.timer = 100

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

