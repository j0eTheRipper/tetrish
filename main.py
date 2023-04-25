import pygame
from Block import Block
from sys import exit
from generate_words import generate_word, generate_sentence


pygame.init()

MAX = 600
screen = pygame.display.set_mode((MAX, MAX))
clock = pygame.time.Clock()
background = pygame.image.load('src/background.png').convert()
sentences = generate_sentence()
correct_sentence = next(sentences)
words = generate_word(correct_sentence)
user_sentence = ['', '', '']
Block((300, 0), words)
BLOCK_HISTORY = Block.block_history

pygame.display.set_caption('Tetrish')


def main():
    while True:
        check_for_events()

        screen.blit(background, (0, 0))
        render_blocks()
        play_game()

        pygame.display.update()
        clock.tick(30)


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
    global correct_sentence
    global words

    if not block.is_at_bottom and block.is_untouched:
        block.get_down(MAX)
    elif block.perimeter.midtop[1] <= 0:  # Block has no space to go.
        pygame.quit()
        exit()
    else:
        word, index = block.anchor_block()
        user_sentence[index] = word
        try:
            Block((300, 0), words)
        except StopIteration:
            if user_sentence == correct_sentence.split():
                Block.kill_row()
            correct_sentence = next(sentences)
            words = generate_word(correct_sentence)
            Block((300, 0), words)


if __name__ == '__main__':
    main()
