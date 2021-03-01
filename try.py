import pygame, sys
from random import randint
from pygame.locals import *

pygame.init()

FPS = 30
screen_size = (400, 750)
screen = pygame.display.set_mode((screen_size[0], screen_size[1]))
c_grey = (100, 100, 110, 255)
c_grey_a = (100, 100, 100, 70)
c_green = (0, 100, 0, 255)
c_sky = (170, 170, 200, 255)
c_blue = (100, 100, 200, 255)
c_white = (200, 200, 200, 255)
c_grey_land = (100, 100, 100, 255)
c_black = (0, 0, 0, 255)
c_red = (200, 30, 50, 255)
screen.fill(c_white)


def circle_gradient(position, color, surf, radius):
    for i in range(radius):
        light_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        pygame.draw.circle(light_surface, color, position, i)
        surf.blit(light_surface, (0, 0))


def draw_car(direction, coordx, coordy, c_main):
    coef = coordy / screen_size[1]
    car_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    circle_gradient((coordx, coordy), (255, 255, 255, 2), car_surface, int(50 * coef))
    pygame.draw.ellipse(car_surface, c_black, (coordx + 85 * coef, coordy + 10 * coef, 30 * coef, 10 * coef), 0)
    pygame.draw.rect(car_surface, c_main, (coordx, coordy, 100 * coef, 30 * coef), 0)
    pygame.draw.rect(car_surface, c_main, (coordx + 25 * coef, coordy - 25 * coef, 60 * coef, 30 * coef), 0)
    pygame.draw.rect(car_surface, c_white, (coordx + 30 * coef, coordy - 20 * coef, 20 * coef, 18 * coef), 0)
    pygame.draw.rect(car_surface, c_white, (coordx + 60 * coef, coordy - 20 * coef, 20 * coef, 18 * coef), 0)
    pygame.draw.circle(car_surface, c_black, (coordx + 20 * coef, coordy + 30 * coef), 15 * coef)
    pygame.draw.circle(car_surface, c_black, (coordx + 80 * coef, coordy + 30 * coef), 15 * coef)
    pygame.draw.ellipse(car_surface, c_grey_a, (coordx + 110 * coef, coordy - 10 * coef, 40 * coef, 20 * coef))
    pygame.draw.ellipse(car_surface, c_grey_a, (coordx + 130 * coef, coordy - 35 * coef, 50 * coef, 25 * coef))
    pygame.draw.rect(car_surface, (255, 255, 0), (coordx, coordy, 10 * coef, 7 * coef), 0)
    screen.blit(pygame.transform.flip(car_surface, bool(direction), 0), (0, 0))


def rand_color(main_color):
    res = [main_color[0] + randint(-30, 30), main_color[1] + randint(-30, 30), main_color[2] + randint(-30, 30),
           main_color[3]]
    for i in range(len(res)):
        if res[i] < 0:
            res[i] = 0
        if res[i] > 255:
            res[i] = 255
    return res


def draw_background(num_of_trees, main_color_house, main_color_clouds, surf):
    surf_size = surf.get_size()
    back = pygame.Surface(surf.get_size(), pygame.SRCALPHA)
    for i in range(num_of_trees):
        if bool(randint(0, 1)):
            x = randint(0, surf_size[0])
            y = randint(0, surf_size[1] // 4)
            pygame.draw.rect(back, rand_color(main_color_house),
                             (x, y, randint(surf_size[0] // 7, surf_size[0] // 4),
                              surf_size[1] - randint(0, 30)))
        else:
            x_size = randint(surf_size[0] // 5, surf_size[0] // 2)
            y_size = x_size // 2
            x = randint(-x_size // 2, surf_size[0] - x_size // 2)
            y = randint(-y_size // 2, surf_size[1] // 4)
            pygame.draw.ellipse(back, rand_color(main_color_clouds), (x, y, x_size, y_size))
        surf.blit(back, (0, 0))


def draw_cars(number_of_cars, main_color):
    for i in range(number_of_cars):
        draw_car(randint(0, 1), randint(0, screen_size[0]),
                 screen_size[1] * 2 // 3 + screen_size[1] * 3 // 8 // number_of_cars * i, rand_color(main_color))


screen.fill((0, 0, 0))
pygame.draw.rect(screen, c_green, (0, 2 * screen_size[1] // 3 + 3, screen_size[0], screen_size[1] // 3), 0)
pygame.draw.ellipse(screen, c_grey_land, (-10, screen_size[1] - 100, screen_size[0] * 3 // 2, screen_size[1] // 2))
pygame.draw.rect(screen, c_sky, (0, screen_size[1] // 6, screen_size[0], screen_size[1] // 2), 0)


sky = pygame.Surface((screen_size[0], screen_size[1] // 2), pygame.SRCALPHA)
dark = pygame.Surface((screen_size[0], screen_size[1] // 6))
subscreen1 = pygame.Surface((screen_size[0] * 2 // 3, screen_size[1] // 3))
subscreen2 = pygame.Surface((screen_size[0] * 2 // 3, screen_size[1] // 3))
sky.fill((0, 0, 0, 0))
dark.fill(c_black)
subscreen1.fill(c_blue)
subscreen2.fill(c_blue)

draw_background(5, c_blue, c_blue, sky)
draw_background(7, c_black, c_black, dark)
draw_background(3, c_grey, c_grey_land, subscreen1)
draw_background(3, c_grey, c_grey_land, subscreen2)

pygame.draw.rect(subscreen1, c_white, (0, 0, screen_size[0] * 2 // 3, screen_size[1] // 3), 5)
pygame.draw.rect(subscreen2, c_white, (0, 0, screen_size[0] * 2 // 3, screen_size[1] // 3), 5)


screen.blit(dark, (0, 0))
screen.blit(subscreen1, (0, screen_size[1] // 3))
screen.blit(subscreen2, (screen_size[0] // 3, screen_size[1] // 3 - 20))
screen.blit(sky, (0, screen_size[1] // 6))
draw_cars(10, c_red)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
