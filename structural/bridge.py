class DrawingOne:
    def draw_circle(self, x, y, radius):
        print('One is drawing a circle ({}, {}) with radius of {}'.format(x, y, radius))


class DrawingTwo:
    def draw_circle(self, x, y, radius):
        print('Two is drawing a circle ({}, {}) with radius of {}'.format(x, y, radius))


class Bridge:
    def __init__(self, x, y, radius, drawing_object) -> None:
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_object = drawing_object

    def draw(self):
        self._drawing_object.draw_circle(self._x, self._y, self._radius)


bridge = Bridge(1, 2, 3, DrawingOne())
bridge.draw()
