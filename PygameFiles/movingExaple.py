from pickle import TRUE
import pygame, os, time, random, math, sys
pygame.init()

WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))

box = pygame.Rect(WIDTH//2-25, 0, 50, 50)
down = TRUE
up = False

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()

    pygame.draw.rect(screen, (255,255,255), box)
    if box.y >= HEIGHT-50:
        up = True
        down = False

    if box.y <= 0:
        up = False
        down = True
    
    if up:
        box.y -= 5
    
    if down:
        box.y += 5
    
    pygame.time.delay(50)
    pygame.display.update()