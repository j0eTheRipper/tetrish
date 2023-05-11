import pygame
from Block import Block
from Word import Word
from sys import exit
from generate_words import generate_word, generate_sentence


pygame.init()

MAX = 600
screen = pygame.display.set_mode((MAX, MAX))
clock = pygame.time.Clock()
background = pygame.image.load('src/background.png').convert()


def initiate_game(src):
    global sentences, correct_sentence, words, user_sentence
    sentences = generate_sentence(src)
    correct_sentence = next(sentences)
    words = generate_word(correct_sentence)
    user_sentence = ['', '', '']
    Block((300, 0), words)


BLOCK_HISTORY = Block.block_history

pygame.display.set_caption('Tetrish')


def main():
    start = 0
    while True:
        check_for_events()

        screen.blit(background, (0, 0))
        instructions = pygame.image.load('src/instructions.png').convert()
        if not start:
            screen.blit(instructions, (150, 100))
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                initiate_game('src/example.txt')
                start += 1
            elif pygame.key.get_pressed()[pygame.K_LEFT]:
                initiate_game('src/french.txt')
                start += 1
        else:
            render_blocks()
            play_game()

        pygame.display.update()
        clock.tick(30)


def check_for_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if BLOCK_HISTORY:
                block = BLOCK_HISTORY[-1]
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

    if pygame.key.get_pressed()[pygame.K_DOWN]:
        block.get_down(MAX)

    if not block.is_at_bottom and block.is_untouched:
        block.get_down(MAX)
    elif block.perimeter.midtop[1] <= 0:  # Block has no space to go.
        stop_screen = pygame.image.load('src/you_lost.png').convert()
        screen.blit(stop_screen, (150, 100))
    else:
        word, index = block.anchor_block()
        user_sentence[index] = word
        try:
            Block((300, 0), words)
        except StopIteration:
            if user_sentence == correct_sentence.split():
                Block.kill_last_row()
            try:
                correct_sentence = next(sentences)
            except StopIteration:
                win_screen = pygame.image.load('src/you_won.png').convert()
                screen.blit(win_screen, (150, 100))
            words = generate_word(correct_sentence)
            Block((300, 0), words)


if __name__ == '__main__':
    main()
