import pyglet
import pickle
from game.objects import Wall

start = None

window = pyglet.window.Window(resizable=True)
map = []
line = pyglet.shapes.Line(0, 0, 0, 0, 1, (0, 255, 0))


@window.event
def on_draw():
    window.clear()
    line.draw()
    for wall in map:
        wall.draw()


@window.event
def on_mouse_press(x, y, button, modifiers):
    global start
    if start is None:
        start = (x, y)
    else:
        map.append(Wall(start[0], start[1], x, y))
        start = None
        line.x = 0
        line.y = 0
        line.x2 = 0
        line.y2 = 0


@window.event
def on_mouse_motion(x, y, dx, dy):
    if start is not None:
        line.x = start[0]
        line.y = start[1]
        line.x2 = x + dx
        line.y2 = y + dy
        # print(x, y, dx, dy)


pyglet.app.run()

with open("map", "wb") as f:
    pickle.dump(map, f)
    f.close()
