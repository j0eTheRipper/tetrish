import pygame


class Block:
    def __init__(self, image, place):
        self.surface = pygame.image.load(image).convert_alpha()
        self.perimeter = self.surface.get_rect(center=place)
        self.image = image
        self.__speed = 5

    def get_down(self, limit):
        if self.perimeter.midbottom[1] < limit:
            self.perimeter.y += self.__speed

    def go_left(self, limit):
        if self.perimeter.midleft[0] > limit:
            self.perimeter.x -= self.__speed

    def go_right(self, limit):
        if self.perimeter.midright[0] < limit:
            self.perimeter.x += self.__speed

    def move(self, max_limit):
        self.get_down(max_limit)
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.go_left(0)
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.go_right(max_limit)
