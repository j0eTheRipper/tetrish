from random import randint


def generate_word(sentence):
    sentence = sentence.split()
    while sentence:
        word = sentence.pop(randint(0, len(sentence) - 1))
        yield word


def generate_sentence():
    with open('src/example.txt') as file:
        for sentence in file:
            yield sentence

