import random
from pico2d import *
import game_framework
import game_world
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy, zombies, balls

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    zombies = [Zombie(random.randint(100, 1500), 60, random.choice([-1, 1])) for _ in range(10)]
    game_world.add_objects(zombies, 1)

    global balls
    balls = [Ball(random.randint(100, 1600 - 100), 60, 0) for _ in range(30)]
    game_world.add_objects(balls, 1)

    balls = []
    game_world.add_collision_pair('boy : zombie', boy, None)
    for zombie in zombies:
        game_world.add_collision_pair('ball : zombie', None, zombie)

def finish():
    game_world.clear()

def update():
    game_world.update()
    for ball in balls:
        if game_world.collide(boy, ball):
            print('COLLISION boy:ball')

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass
