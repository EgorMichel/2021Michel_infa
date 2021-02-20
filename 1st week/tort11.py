import turtle as t

t.shape('turtle')

t.speed(0)


def circle(r):
    for i in range(180):
        t.forward(2 * r * 0.01745)
        t.left(2)


t.left(90)
for i in range(10):
    circle(20 + 5 * i)
    t.left(180)
    circle(20 + 5 * i)
    t.left(180)
