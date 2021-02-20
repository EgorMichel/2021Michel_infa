from PIL import Image
import pygame
from pygame.draw import *

FPS = 30

f = open("Exhibition\\" + str(input("Number of picture you want to see(from 0 to 20): ")) + "_2.png", "rb")
img = Image.open(f)
xy = img.size
obj = img.load()

screen = pygame.display.set_mode((xy[0] // 2, xy[1] // 2))
print(xy)
print("Loading...")

for i in range(xy[0] // 2):
    for j in range(xy[1] // 2):
        a = []
        a.append(obj[2 * i, 2 * j])
        a.append(obj[2 * i - 1, 2 * j])
        a.append(obj[2 * i, 2 * j - 1])
        a.append(obj[2 * i - 1, 2 * j - 1])
        A = [0, 0, 0]
        for t in range(len(a)):
            for k in range(len(A)):
                A[k] += a[t][k]
        for k in range(len(A)):
            A[k] /= 4

        rect(screen, A, (i, j, 1, 1))

print("Drawing finished")
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
