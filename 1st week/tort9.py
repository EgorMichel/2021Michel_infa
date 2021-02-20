import turtle as t
import math as m

t.shape('turtle')


def nangle(n, r):
    angle = ((n - 2) * 180) / n
    a = 2 * m.sin(2 * m.pi / n) * r
    t.left(180 - angle / 2)
    for p in range(n):
        t.forward(a)
        t.left(180 - angle)


for i in range(3, 11):
    nangle(i, 20 * i)
    ang = ((i - 2) * 180) / i
    t.right(180 - ang / 2)
    t.penup()
    t.forward(40)
    t.pendown()

