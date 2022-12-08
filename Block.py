import pygame

SPEED = 10


class Block:
    def __init__(self, image, place):
        self.surface = pygame.image.load(image).convert_alpha()
        self.perimeter = self.surface.get_rect(center=place)

    def rise(self, limit):
        if self.perimeter.midtop[1] > limit:
            self.perimeter.y -= SPEED

    def get_down(self, limit):
        if self.perimeter.midbottom[1] < limit:
            self.perimeter.y += SPEED

    def go_left(self, limit):
        if self.perimeter.midleft[0] > limit:
            self.perimeter.x -= SPEED

    def go_right(self, limit):
        if self.perimeter.midright[0] < limit:
            self.perimeter.x += SPEED
