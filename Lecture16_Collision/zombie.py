import random
import math
import game_framework
import game_world

from pico2d import *

# zombie Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10.0

animation_names = ['Walk']

class Zombie:
    images = None

    def load_images(self):
        if Zombie.images is None:
            Zombie.images = {}
            for name in animation_names:
                Zombie.images[name] = [load_image("./zombie/" + name + " (%d).png" % i) for i in range(1, 11)]

    def __init__(self, x=0, y=0, dir=1):
        self.x = x
        self.y = y
        self.dir = dir
        self.hit_count = 0  # 공에 맞은 횟수를 추적하기 위한 변수
        self.width = 200
        self.height = 200
        self.load_images()
        self.frame = random.randint(0, 9)

    def handle_collision(self, group, other):
        if group == 'ball : zombie':
            self.hit_count += 1
            if self.hit_count == 1:
                    # 첫 번째로 맞았을 때 크기를 절반으로 줄임
                self.width = 100
                self.height = 100
            elif self.hit_count == 2:
                    # 두 번째로 맞았을 때 게임 월드에서 제거
                game_world.remove_object(self)
        elif group == 'boy : zombie':
                # 소년과 충돌 시 게임 종료
             game_framework.quit()

    def draw(self):
        if self.dir < 0:
            Zombie.images['Walk'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, self.width, self.height)
        else:
            Zombie.images['Walk'][int(self.frame)].draw(self.x, self.y, self.width, self.height)


    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += RUN_SPEED_PPS * self.dir * game_framework.frame_time
        if self.x > 1600:
            self.dir = -1
        elif self.x < 800:
            self.dir = 1
        self.x = clamp(800, self.x, 1600)
        pass



    def handle_event(self, event):
        pass




