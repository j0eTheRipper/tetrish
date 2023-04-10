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
Block(new_block, (300, 0), 'youssef')
BLOCK_HISTORY = Block.block_history

pygame.display.set_caption('Tetrish')


def main():
    while True:
        check_for_events()

        screen.blit(background, (0, 0))
        render_blocks()
        play_game()

        pygame.display.update()
        clock.tick(60)


def check_for_events():
    block = BLOCK_HISTORY[-1]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                block.go_right()
            elif event.key == pygame.K_LEFT:
                block.go_left()


def render_blocks():
    for i in BLOCK_HISTORY:
        screen.blit(i.surface, i.perimeter)
        screen.blit(i.word.surface, i.word.perimeter)


def play_game():
    block = BLOCK_HISTORY[-1]

    if not block.is_at_bottom and block.is_untouched:
        block.get_down(MAX)
    elif block.perimeter.midtop[1] <= 0:  # Block has no space to go.
        pygame.quit()
        exit()
    else:
        block.kill_block()
        create_block(block)


def create_block(block):
    new_blk = choose_block(block)
    Block(new_blk, (300, 0), 'youssef')


def choose_block(block):
    if len(BLOCK_HISTORY) % 3 == 0:
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
