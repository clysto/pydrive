import math
import pyglet


class Wall:
    def __init__(self, x0, y0, x1, y1, batch=None):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.batch = batch

    def draw(self):
        line = pyglet.shapes.Line(
            self.x0, self.y0, self.x1, self.y1, 1, (255, 0, 0), batch=self.batch
        )
        line.draw()


class Car:
    def __init__(self):
        self.x = 50
        self.y = 50
        self.width = 20
        self.height = 10
        self.velocity = 50
        self.angle = 0
        self.left = False
        self.right = False

    def draw(self):
        rec = pyglet.shapes.Rectangle(self.x, self.y, self.width, self.height)
        rec.anchor_x = self.width / 2
        rec.anchor_y = self.height / 2
        rec.rotation = self.angle
        rec.draw()

    def turn_left(self):
        self.angle -= 3

    def turn_right(self):
        self.angle += 3

    def move_forward(self, dt):
        distance = dt * self.velocity
        if self.left:
            self.turn_left()
        elif self.right:
            self.turn_right()
        self.x += distance * math.cos(math.radians(self.angle))
        self.y += -distance * math.sin(math.radians(self.angle))
