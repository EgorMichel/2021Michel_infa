import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 700))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
balls = []
score = 0


def fillBalls(num):
    for i in range(num):
        balls.append([randint(20, 100), randint(100, 1100), randint(100, 600), randint(-5, 5), randint(-5, 5),
                      randint(0, 5)])


def drawballs(ball):
    for b in ball:
        pygame.draw.circle(screen, COLORS[b[5]], (b[1], b[2]), b[0])


def moveballs(ball):
    for i in range(len(ball)):
        ball[i][1] += ball[i][3]
        ball[i][2] += ball[i][4]
        if ball[i][1] + ball[i][0] > 1200:
            ball[i][3] = ball[i][3] * (-1)
        if ball[i][2] + ball[i][0] > 700:
            ball[i][4] = ball[i][4] * (-1)
        if ball[i][1] - ball[i][0] < 0:
            ball[i][3] = ball[i][3] * (-1)
        if ball[i][2] - ball[i][0] < 0:
            ball[i][4] = ball[i][4] * (-1)


def click(event_):
    for i in range(len(balls)):
        if (event_.pos[0] - balls[i][1])**2 + (event_.pos[1] - balls[i][2])**2 < balls[i][0]**2:
            balls[i] = ([randint(20, 100), randint(100, 1100), randint(100, 600), randint(-5, 5), randint(-5, 5),
                         randint(0, 5)])
            global score
            score += 1


def prints():
    global score
    f1 = pygame.font.Font(None, 50)
    texcoordt1 = f1.render(str(score), True, (180, 0, 0))
    screen.blit(texcoordt1, (30, 70))


pygame.display.update()
clock = pygame.time.Clock()
finished = False
fillBalls(3)
drawballs(balls)

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            click(event)

    prints()
    moveballs(balls)
    drawballs(balls)
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
