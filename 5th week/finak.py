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

# 0th is "am I playing", 1st is "did I win", 3d is "did i typed username"
condition = [False, False, False]
# current score
score = [0]
# list of balls (balls means all the figures)
balls = []
# list of speeds
speed = []
# Name that will appear in a leaderboard
username = ['']
file = open("Leaderboard.txt", 'r')
leaderboard = file.readlines()
leaderboard.append('Game session: ' + str(time.ctime(time.time())) + '\n')
# 0th - start time 1th - finish time, 2nd - best time
times = [0, 0, float(leaderboard[2])]


def fill_balls_and_speeds(num):
    '''
    :param num: number of balls
    fills list of balls randomly
    '''
    for i in range(num):
        balls.append([randint(100, 1100), randint(100, 700), randint(10, 100), randint(0, 5), randint(0, 100)])
        if balls[i][4] < 70:
            speed.append([randint(-5, 5), randint(-5, 5)])
        else:
            speed.append([randint(-10, 10), randint(-10, 10)])
            balls[i][2] = int(balls[i][2] * 1.5)


def draw_shit(ball):
    '''
    :param ball: list of balls
    draws a frame with balls
    '''
    for b in ball:
        if b[4] < 70:
            pygame.draw.circle(screen, COLORS[b[3]], (b[0], b[1]), b[2])
        else:
            pygame.draw.rect(screen, COLORS[b[3]], (b[0], b[1], b[2], b[2]))


def move_balls(ball, sped):
    '''
    :param ball: list of balls
    :param sped: list of speeds of balls
    moves balls on the screen
    '''
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
    '''
    :param eve: current event
    :param ball: list of balls
    :param sped: list of balls speed
    react to the current event
    '''
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
            score[0] -= 1
    elif not condition[0] and not condition[1] and not event.type == pygame.MOUSEBUTTONDOWN and not condition[2]:
        if eve.key == pygame.K_BACKSPACE:
            username[0] = username[0][:-1]
        elif eve.key == pygame.K_RETURN:
            condition[2] = True
            leaderboard.append(username[0] + ': \n')
        else:
            username[0] += eve.unicode
        print(username[0])
    else:
        condition[0] = True
        times[0] = time.time()


def prints():
    '''
    :return: makes all the prints required
    '''
    f1 = pygame.font.Font(None, 40)
    if condition[0]:
        texcoordt1 = f1.render(str(score[0]), True, (180, 0, 0))
        screen.blit(texcoordt1, (30, 70))
        texcoordt2 = f1.render(str(round((time.time() - times[0]), 2)), True, (180, 0, 0))
        screen.blit(texcoordt2, (30, 30))
    elif not condition[1] and not condition[0]:
        text = f1.render('Type ur name and press Enter to confirm. Then click to attempt to get 100 points',
                         True, (180, 0, 0))
        if not condition[2]:
            text2 = f1.render(username[0], True, (250, 250, 250))
        else:
            text2 = f1.render(username[0], True, (250, 250, 0))
        screen.blit(text, (90, 300))
        screen.blit(text2, (90, 400))
    elif not condition[0] and condition[1]:
        text2 = f1.render('You got 100 points in ' + str(times[1]) + 'sec, why so slow? Try again?', True, (180, 0, 0))
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
        elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            click(event, balls, speed)

    if score[0] >= 100:
        condition[1] = True
        condition[0] = False
        times[1] = round(time.time() - times[0], 3)
        leaderboard.append(str(times[1]) + '\n')
        if times[1] < times[2]:
            times[2] = times[1]
            leaderboard[2] = str(times[2]) + '\n'
            leaderboard[1] = username[0] + ':' + '\n'
        score[0] = 0

    if condition[0]:
        move_balls(balls, speed)
        draw_shit(balls)
    prints()
    pygame.display.update()
    screen.fill(BLACK)


file.close()
file = open("Leaderboard.txt", 'w')

for line in leaderboard:
    file.write(line)

file.write('-----------------' + '\n')
file.close()

pygame.quit()
