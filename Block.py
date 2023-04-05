import pygame
from Word import Word


class Block:
    block_history = []
    old_blocks_peremiters = []
    block_stack_height = [600, 600, 600]

    def __init__(self, image, place, word):
        self.surface = pygame.image.load(image).convert_alpha()
        self.perimeter = self.surface.get_rect(center=place)
        self.image = image
        self.word = Word(word, self.perimeter.center)
        self.txt = word
        self.__speed = 5
        Block.block_history.append(self)

    def get_down(self, limit):
        if self.perimeter.midbottom[1] < limit:
            self.perimeter.y += self.__speed
            self.word.perimeter.y += self.__speed

    def go_left(self):
        if self.perimeter.x == 200:
            will_collide = self.__check_for_collision(0)
            if not will_collide:
                self.perimeter.x = 0
        elif self.perimeter.x == 400:
            will_collide = self.__check_for_collision(1)
            if not will_collide:
                self.perimeter.x = 200
        self.word.perimeter.center = self.perimeter.center

    def go_right(self):
        if self.perimeter.x == 200:
            will_collide = self.__check_for_collision(2)
            if not will_collide:
                self.perimeter.x = 400
        elif self.perimeter.x == 0:
            will_collide = self.__check_for_collision(1)
            if not will_collide:
                self.perimeter.x = 200
        self.word.perimeter.center = self.perimeter.center

    def __check_for_collision(self, x):
        if self.perimeter.bottomleft[1] >= Block.block_stack_height[x]:
            return True

    @property
    def is_untouched(self):
        return self.perimeter.collidelist(Block.old_blocks_peremiters) == -1

    @property
    def is_at_bottom(self):
        return self.perimeter.midbottom[1] >= 600
