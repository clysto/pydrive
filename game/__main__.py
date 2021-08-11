import pickle
import pyglet
from game.objects import Car

window = pyglet.window.Window(resizable=True)

car = Car()
map = None
with open("maps/map1", "rb") as f:
    map = pickle.load(f)
    f.close()


@window.event
def on_draw():
    window.clear()
    car.draw()
    for wall in map:
        wall.draw()


@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.LEFT:
        car.left = True
    if symbol == pyglet.window.key.RIGHT:
        car.right = True


@window.event
def on_key_release(symbol, modifiers):
    if symbol == pyglet.window.key.LEFT:
        car.left = False
    if symbol == pyglet.window.key.RIGHT:
        car.right = False


def update(dt):
    car.move_forward(dt)


pyglet.clock.schedule_interval(update, 1 / 30.0)
pyglet.app.run()
