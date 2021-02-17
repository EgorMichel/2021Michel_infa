from random import randint
import turtle as t



number_of_turtles = 10
steps_of_time_number = 1000
t.speed(0)


def make_field(x):
    t.penup()
    t.forward(x/2)
    t.left(90)
    t.pendown()
    t.width(10)
    t.forward(x/2)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x/2)

make_field(400)
t.width(2)
pool = [t.Turtle(shape='circle') for i in range(number_of_turtles)]
coordinates = [[1., 1.]]
velocity = [[1., 1.]]
i = 0

for unit in pool:
    unit.penup()
    unit.speed(50)
    coordinates.append([randint(-200, 200), randint(-200, 200)])
    velocity.append([randint(-99, 99) / 33, randint(-99, 99) / 33])
    unit.goto(coordinates[i])
    i += 1
    unit.left(randint(0, 366))


for j in range(steps_of_time_number):
    for i in range(number_of_turtles):
        coordinates[i][0] += velocity[i][0]
        coordinates[i][1] += velocity[i][1]

        if coordinates[i][0]**2 > 40000:
            velocity[i][0] = -1 * velocity[i][0]
        if coordinates[i][1]**2 > 40000:
            velocity[i][1] = -1 * velocity[i][1]

        pool[i].goto(coordinates[i][0], coordinates[i][1])
