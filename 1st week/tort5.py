import turtle as t

t.shape('turtle')

t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)

for i in range(10):
    t.penup()
    t.forward(10)
    t.left(90)
    t.pendown()
    t.forward(60 + i * 20)
    t.left(90)
    t.forward(70 + i * 20)
    t.left(90)
    t.forward(70 + i * 20)
    t.left(90)
    t.forward(70 + i * 20)
    t.left(90)
    t.forward(70 + i * 20)
