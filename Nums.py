import turtle as t

# rules = (('d', 'f', 10, 'r', 90, 'f', 20, 'r', 90, 'f', 10, 'r', 90, 'f', 20, 'r', 90, 'u', 'f', 20),
#          ('u', 'r', 90, 'f', 10, 'd', 'l', 135, 'f', 14.142, 'r', 135, 'f', 20, 'u', 'b', 20, 'l', 90, 'f', 10),
#          ('d', 'f', 10, 'r', 90, 'f', 10, 'r', 45, 'f', 14.142, 'l', 135, 'f', 10, 'u', 'l', 90, 'f', 20, 'r', 90, 'f', 10),
#          ('d', 'f', 10, 'r', 135, 'f', 14.142, 'l', 135, 'f', 10, 'r', 135, 'f', 14.142, 'u', 'b', 14.142, 'l', 45, 'b', 10, 'l', 90, 'f', 10),
#          ('d', 'r', 90, 'f', 10, 'l', 90, 'f', 10, 'r', 90, 'f', 10, 'b', 20, 'u', 'l', 90, 'f', 10),
#          (), (),
#          ('d', 'f', 10, 'r', 135, 'f', 14.142, 'l', 45, 'f', 10,  'u', 'b', 20, 'l', 90, 'f', 20))

file = open("Rules.txt", 'r')
rules = file.readlines()


def draw_number(n):
    for i in range(len(rules[n])):
        if rules[n][i] == 'u':
            t.penup()
        if rules[n][i] == 'd':
            t.pendown()
        if rules[n][i] == 'f':
            t.forward(float(rules[n][i + 1:i + 5]) * 2)
            i += 4
        if rules[n][i] == 'b':
            t.back(float(rules[n][i + 1:i + 5]) * 2)
            i += 4
        if rules[n][i] == 'l':
            t.left(float(rules[n][i + 1:i + 5]))
            i += 4
        if rules[n][i] == 'r':
            t.right(float(rules[n][i + 1:i + 5]))
            i += 4


draw_number(1)
draw_number(4)
draw_number(1)
draw_number(7)
draw_number(0)
draw_number(0)