from pico2d import *
import game_world
import game_framework

# Bird Fly Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
FLY_SPEED_KMPH = 54.0  # Km / Hour
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

# Bird Action Speed
TIME_PER_ACTION = 0.5 # 액션 당 걸리는 시간
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION # 초당 액션 수
FRAMES_PER_ACTION = 14

class Bird:
    def __init__(self, x = 400 , y = 500):
        self.image = load_image('bird_animation.png')
        self.x, self.y = x, y
        self.frame = 0
        self.dir = 1
        self.flip = ''

    def draw(self):
        self.image.clip_composite_draw(int(self.frame % 5) * 183, (2 - (int(self.frame) // 5)) * 168, 180, 168, 0, self.flip, self.x, self.y, 70, 35)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.dir * FLY_SPEED_PPS * game_framework.frame_time
        if self.x > 1600:
            self.dir = -1
            self.flip = 'h'
        elif self.x < 0:
            self.dir = 1
            self.flip = ''
