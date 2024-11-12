from pico2d import *
import game_world
import game_framework

class Ball:
    image = None

    def __init__(self, x=400, y=300, velocity=1):  # velocity를 공의 초기 속도로 설정
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        # 공이 일정 속도로 이동
        self.x += self.velocity * 300 * game_framework.frame_time  # 공의 이동 속도 조정

        # 화면 밖으로 나가면 제거
        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10


    def handle_collision(self, group, other):
        if group == 'boy:ball':
            game_world.remove_object(self)
        elif group == 'ball : zombie':
            game_world.remove_object(self)
