import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 600))

rect(screen, (66, 103, 237), (0, 0, 1000, 600))  # Заливка цвета воды  Первый слой

polygon(screen, (219, 218, 204), ((0, 400), (0, 0), (1000, 0), (1000, 375), (0, 400)), 0)  # Облака

polygon(screen, (227, 215, 109), ((0, 400), (0, 125), (600, 115), (1000, 135), (1000, 375), (0, 400)), 0)  # Небо

polygon(screen, (38, 207, 23), ((0, 400), (0, 250), (375, 230), (1000, 240), (1000, 375), (0, 400)), 0)  # Трава

polygon(screen, (74, 73, 66), ((10, 258), (30, 250), (35, 230), (40, 200), (120, 175), (300, 120), (400, 50), (550, 110)
                               , (560, 130), (570, 200), (610, 250), (680, 200), (750, 128), (770, 100), (890, 200),
                               (1000, 260), (10, 258))
        , 0)  # Задние горы

polygon(screen, (115, 32, 112), ((0, 410), (0, 260), (20, 260), (50, 280), (65, 310), (160, 200), (200, 240), (290, 190)
                                 , (300, 200), (490, 280), (750, 380), (940, 180), (1000, 420), (0, 410))
        , 0)  # Передние горы


circle(screen, (255, 247, 15), (700, 70), 60, 0)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
