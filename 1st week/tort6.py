import turtle as t

t.shape('turtle')

n = int(input())

for i in range(n):
    t.forward(100)
    t.stamp()
    t.backward(100)
    t.left(360 / n)

input()