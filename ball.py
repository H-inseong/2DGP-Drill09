from pico2d import load_image

import game_world


def fire_ball(self):
    ball = Ball(self.x, self.y, self.face_dir * 10)
    game_world.add_object(ball, 1)

class Ball:
    image = None

    def __init__(self, x, y, v):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.v = x, y, v

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.v

        if self.x < 25 or self.x > 800 - 25:
            game_world.remove_object(self)