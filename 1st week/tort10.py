import turtle as t

t.shape('turtle')


def circle():
    for i in range(180):
        t.forward(2)
        t.left(2)


for i in range(6):
    circle()
    t.left(60)
