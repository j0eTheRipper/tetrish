import pygame


class Block:
    blocks = []
    block_rect = []
    block_stack_height = [600, 600, 600]

    def __init__(self, image, place):
        self.surface = pygame.image.load(image).convert_alpha()
        self.perimeter = self.surface.get_rect(center=place)
        self.image = image
        self.__speed = 10
        Block.blocks.append(self)

    def get_down(self, limit):
        if self.perimeter.midbottom[1] < limit:
            self.perimeter.y += self.__speed

    def go_left(self):
        if self.perimeter.x == 200:
            will_collide = self.__check_for_collision(0)
            if not will_collide:
                self.perimeter.x = 0
        elif self.perimeter.x == 400:
            will_collide = self.__check_for_collision(1)
            if not will_collide:
                self.perimeter.x = 200

    def go_right(self):
        if self.perimeter.x == 200:
            will_collide = self.__check_for_collision(2)
            if not will_collide:
                self.perimeter.x = 400
        elif self.perimeter.x == 0:
            will_collide = self.__check_for_collision(1)
            if not will_collide:
                self.perimeter.x = 200

    def move(self, max_limit):
        self.get_down(max_limit)
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.go_left()
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.go_right()

    def __check_for_collision(self, x):
        if self.perimeter.bottomleft[1] >= Block.block_stack_height[x]:
            return True
