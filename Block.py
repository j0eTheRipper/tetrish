import pygame
from Word import Word
from random import randint
block_images = ('src/block.png', 'src/block1.png', 'src/block2.png')
LEFT = 0
MIDDLE = 200
RIGHT = 400


class Block:
    block_history = []
    dead_blocks = []
    block_stack_height = [600, 600, 600]

    def __init__(self, place, word):
        self.image = self.__choose_block_image()
        self.surface = pygame.image.load(self.image).convert_alpha()
        self.perimeter = self.surface.get_rect(center=place)
        self.txt = next(word)
        self.word = Word(self.txt, self.perimeter.center)
        self.__speed = 5
        Block.block_history.append(self)

    def get_down(self, limit):
        if self.perimeter.midbottom[1] < limit:
            self.perimeter.y += self.__speed
            self.word.perimeter.y += self.__speed

    def go_left(self):
        if self.perimeter.x == 200:
            self.__move(LEFT)
        elif self.perimeter.x == 400:
            self.__move(MIDDLE)
        self.word.perimeter.center = self.perimeter.center

    def go_right(self):
        if self.perimeter.x == 200:
            self.__move(RIGHT)
        elif self.perimeter.x == 0:
            self.__move(MIDDLE)
        self.word.perimeter.center = self.perimeter.center

    def kill_block(self):
        place = self.perimeter.x // 200
        Block.dead_blocks.append(self.perimeter)
        Block.block_stack_height[place] = self.perimeter.y

    def __move(self, place):
        index = place // 200
        will_collide = self.__check_for_collision(index)
        if not will_collide:
            self.perimeter.x = place

    def __check_for_collision(self, x):
        if self.perimeter.bottomleft[1] >= Block.block_stack_height[x]:
            return True

    @staticmethod
    def __choose_block_image():
        if len(Block.block_history) % 3 == 0:
            return block_images[randint(0, 2)]
        else:
            last_block = Block.block_history[-1]
            if last_block.image == block_images[0]:
                return block_images[1]
            elif last_block.image == block_images[1]:
                return block_images[2]
            elif last_block.image == block_images[2]:
                return block_images[0]

    @property
    def is_untouched(self):
        return self.perimeter.collidelist(Block.dead_blocks) == -1

    @property
    def is_at_bottom(self):
        return self.perimeter.midbottom[1] >= 600
