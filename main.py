import pygame
from Block import Block
from sys import exit


pygame.init()
MAX = 600
screen = pygame.display.set_mode((MAX, MAX))
clock = pygame.time.Clock()
background = pygame.image.load('src/background.png').convert()
blocks = [Block('src/block.png', (300, 0))]
block = blocks[-1]
print(block.perimeter.collidelist([i.perimeter for i in blocks[:-1]]))


while True:
    block = blocks[-1]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background, (0, 0))
    for i in blocks:
        screen.blit(i.surface, i.perimeter)

    collidelist = block.perimeter.collidelist([i.perimeter for i in blocks[:-1]])
    if block.perimeter.midbottom[1] <= MAX and collidelist == -1:
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            block.get_down(MAX)
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            block.go_left(0)
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            block.go_right(MAX)
    elif block.perimeter.midtop <= 0:
        pygame.quit()
        exit()
    else:
        blocks.append(Block('src/block.png', (300, 0)))

    pygame.display.update()
    clock.tick(60)
