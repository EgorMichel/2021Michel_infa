import turtle as t

t.shape('turtle')

t.speed(0)


def arc(r):
    for i in range(90):
        t.forward(2 * r * 0.01745)
        t.right(2)


def circle(r):
    t.penup()
    t.forward(r)
    t.right(90)
    t.pendown()
    arc(r)
    arc(r)
    t.penup()
    t.left(90)
    t.backward(r)
    t.pendown()


#face
t.begin_fill()
arc(100)
arc(100)
t.color("yellow")
t.end_fill()
t.color("black")

#right eye
t.begin_fill()
t.right(60)
t.penup()
t.forward(60)
t.pendown()
circle(15)
t.penup()
t.backward(60)
t.color("blue")
t.end_fill()
t.color("black")

#left eye
t.begin_fill()
t.right(60)
t.forward(60)
t.pendown()
circle(15)
t.penup()
t.backward(60)
t.color("blue")
t.end_fill()
t.color("black")

#nose
t.width(8)
t.left(30)
t.forward(80)
t.pendown()
t.forward(30)

#smile
t.color("red")
t.penup()
t.forward(10)
t.left(90)
t.forward(70)
t.right(90)
t.pendown()
arc(70)


input()
