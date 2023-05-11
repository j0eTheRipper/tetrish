from random import randint


def generate_word(sentence):
    sentence = sentence.split()
    while sentence:
        word = sentence.pop(randint(0, len(sentence) - 1))
        yield word


def generate_sentence(source):
    with open(source) as file:
        for sentence in file:
            yield sentence.strip("\n")

