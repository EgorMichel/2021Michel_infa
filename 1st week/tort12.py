import turtle as t

t.shape('turtle')

t.speed(0)


def arc(r):
    for i in range(90):
        t.forward(2 * r * 0.01745)
        t.right(2)


t.left(90)


for i in range(3):
    arc(50)
    arc(10)


arc(50)