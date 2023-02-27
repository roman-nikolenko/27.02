import random

import pygame as pg
import pygame

W, H = 500, 500
SIZE = (W, H)
FPS = 60
clock = pg.time.Clock()
img = pygame.image.load('img.png')

pg.init()
win = pygame.display.set_mode(SIZE)

class Image:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = random.choice([-1, -0.5, -0.25, 0.25, 0.5, 1])
        self.dy = random.choice([-1, -0.5, -0.25, 0.25, 0.5, 1])

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x > W or self.x < 0:
            self.dx = -self.dx + (random.randint(-1, 1))
        if self.y > W or self.y < 0:
            self.dy = -self.dy + (random.randint(-1, 1))

    def show(self):
        win.blit(img, (self.x, self.y))


objects = []
for i in range(100):
    objects.append(Image(W, H))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    for image in objects:
        image.move()

    win.fill((225, 225, 225))
    for image in objects:
        image.show()
    pygame.display.update()
    clock.tick(FPS)
