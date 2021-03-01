import pygame
from random import randint
import time

pygame.init()
FPS = 60
screen = pygame.display.set_mode((1200, 800))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

condition = [False, False]
times = [0, 0]
score = [0]
balls = []
speed = []


def fill_balls_and_speeds(num):
    for i in range(num):
        balls.append([randint(100, 1100), randint(100, 700), randint(10, 100), randint(0, 5), randint(0, 100)])
        if balls[i][4] < 70:
            speed.append([randint(-5, 5), randint(-5, 5)])
        else:
            speed.append([randint(-10, 10), randint(-10, 10)])
            balls[i][2] = int(balls[i][2] * 1.5)


def draw_shit(ball):
    for b in ball:
        if b[4] < 70:
            pygame.draw.circle(screen, COLORS[b[3]], (b[0], b[1]), b[2])
        else:
            pygame.draw.rect(screen, COLORS[b[3]], (b[0], b[1], b[2], b[2]))


def move_balls(ball, sped):
    for i in range(len(ball)):
        ball[i][0] += sped[i][0]
        ball[i][1] += sped[i][1]
        if ball[i][4] < 70:
            if ball[i][0] > 1200 - ball[i][2]:
                sped[i][0] = (-1) * sped[i][0]
            if ball[i][0] < 0 + ball[i][2]:
                sped[i][0] = (-1) * sped[i][0]
            if ball[i][1] > 800 - ball[i][2]:
                sped[i][1] = (-1) * sped[i][1]
            if ball[i][1] < 0 + ball[i][2]:
                sped[i][1] = (-1) * sped[i][1]
        else:
            if ball[i][0] > 1200 - ball[i][2]:
                sped[i][0] = randint(-10, 0)
                sped[i][1] = randint(-10, 10)
            if ball[i][0] < 0:
                sped[i][0] = randint(0, 10)
                sped[i][1] = randint(-10, 10)
            if ball[i][1] > 800 - ball[i][2]:
                sped[i][1] = randint(-10, 0)
                sped[i][0] = randint(-10, 10)
            if ball[i][1] < 0:
                sped[i][1] = randint(0, 10)
                sped[i][0] = randint(-10, 10)


def click(eve, ball, sped):
    if condition[0]:
        for i in range(len(ball)):
            if ((eve.pos[0] - ball[i][0])**2 + (eve.pos[1] - ball[i][1])**2) < ball[i][2] * ball[i][2] \
                    and ball[i][4] < 70:
                score[0] += 100 - ball[i][2]
                ball[i][0] = randint(100, 1100)
                ball[i][1] = randint(100, 700)
                ball[i][2] = randint(10, 100)
                ball[i][3] = randint(0, 5)
                ball[i][4] = randint(0, 100)
                sped[i][0] = randint(-5, 5)
                sped[i][0] = randint(-5, 5)
            elif 0 < eve.pos[0] - ball[i][0] < ball[i][2] and 0 < eve.pos[1] - ball[i][1] < ball[i][2]:
                score[0] += 2 * (150 - ball[i][2])
                ball[i][0] = randint(100, 1100)
                ball[i][1] = randint(100, 700)
                ball[i][2] = randint(10, 100)
                ball[i][3] = randint(0, 5)
                ball[i][4] = randint(0, 100)
                sped[i][0] = randint(-10, 10)
                sped[i][0] = randint(-10, 10)
        else:
            print("missed")
            score[0] -= 1
    else:
        condition[0] = True
        times[0] = time.time()


def prints():
    f1 = pygame.font.Font(None, 50)
    if condition[0]:
        texcoordt1 = f1.render(str(score[0]), True, (180, 0, 0))
        screen.blit(texcoordt1, (30, 70))
        texcoordt2 = f1.render(str(round((time.time() - times[0]), 2)), True, (180, 0, 0))
        screen.blit(texcoordt2, (30, 30))
    elif not condition[0] and not condition[1]:
        text = f1.render('Wussup nigga! Press any mouse button and try get 100 points',
                         True, (180, 0, 0))
        screen.blit(text, (90, 300))
    elif not condition[0] and condition[1]:
        text2 = f1.render('Man! You got 100 points in ' + str(times[1]) + 'sec, why so slow? ' +
                          'Try again?', True, (180, 0, 0))
        screen.blit(text2, (90, 300))
        

fill_balls_and_speeds(5)
print(balls)

pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event, balls, speed)

    if score[0] >= 100:
        condition[1] = True
        condition[0] = False
        times[1] = round(time.time() - times[0], 2)
        score[0] = 0

    if condition[0]:
        move_balls(balls, speed)
        draw_shit(balls)
    prints()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
