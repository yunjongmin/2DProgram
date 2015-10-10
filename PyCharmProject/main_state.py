import random
import json
import os

from pico2d import *

import game_framework



name = "MainState"

background = None
monster1 = None


class Background:
    def __init__(self):
        self.image = load_image('Resource/back_01.bmp')

    def draw(self):
        self.image.draw(240, 320)

class Monster1:
    def __init__(self):
        self.x, self.y = 520, 200
        self.frame = 0
        self.image = load_image('Resource/monster1.png')

    def update(self):
        #self.frame = (self.frame + 2) % 8
        #self.frame = 2
        if self.frame == 0:
            self.frame = 1
        elif self.frame == 1:
            self.frame = 7
        elif self.frame == 7:
            self.frame = 0
        delay(0.1)


    def draw(self):
        self.image.clip_draw(self.frame * 33, 0, 33, 33, self.x, self.y)



def enter():
    global background
    global monster1
    background = Background()
    monster1 = Monster1()
    pass


def exit():
    global background
    global monster1
    del(background)
    del(monster1)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
           game_framework.quit()
    pass


def update():
    monster1.update()
    pass


def draw():
    clear_canvas()
    background.draw()
    monster1.draw()
    update_canvas()
    pass





