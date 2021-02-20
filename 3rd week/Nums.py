import turtle as t

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