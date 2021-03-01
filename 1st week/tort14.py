import turtle as t
import math as m

t.shape('turtle')

t.speed(0)


pi = 3.14159265


def star(n):
    r = 100
    a = 2 * r * m.sin(2 * pi / n)
    sina = (4 * r * r * m.sin(2 * pi / n)) / (4 * r * r + a * a / 4)
    print(sina)
    angle = m.asin(sina)

    for i in range(n):
        t.forward(100)
        t.left(180 - angle * 57.3)


star(5)

input()
