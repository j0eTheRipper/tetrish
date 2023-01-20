import pygame
from Block import Block
from sys import exit
from random import randint


pygame.init()

MAX = 600
screen = pygame.display.set_mode((MAX, MAX))
clock = pygame.time.Clock()
background = pygame.image.load('src/background.png').convert()
block_images = ('src/block.png', 'src/block1.png', 'src/block2.png')
new_block = block_images[randint(0, 2)]
Block(new_block, (300, 0))
blocks = Block.blocks


def main():
    while True:
        check_for_events()

        screen.blit(background, (0, 0))
        render_blocks()
        play_game()

        pygame.display.update()
        clock.tick(30)


def check_for_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


def render_blocks():
    for i in blocks:
        screen.blit(i.surface, i.perimeter)


def play_game():
    block = blocks[-1]
    previous_blocks = block.perimeter.collidelist(Block.block_rect)

    if block.perimeter.midbottom[1] < MAX and previous_blocks == -1:
        block.move(MAX)
    elif block.perimeter.midtop[1] <= 0:
        pygame.quit()
        exit()
    else:
        Block.block_rect.append(block.perimeter)
        Block.block_stack_height[block.perimeter.x // 200] = block.perimeter.y
        new_blk = choose_block(block)
        Block(new_blk, (300, 0))


def choose_block(block):
    if len(blocks) % 3 == 0:
        return block_images[randint(0, 2)]
    else:
        if block.image == block_images[0]:
            return block_images[1]
        elif block.image == block_images[1]:
            return block_images[2]
        elif block.image == block_images[2]:
            return block_images[0]


if __name__ == '__main__':
    main()
