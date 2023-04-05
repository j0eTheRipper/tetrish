from pygame.font import SysFont
WHITE = (255, 255, 255)


class Word:
    def __init__(self, text, place):
        font = SysFont('Arial', 20)
        self.surface = font.render(text, True, WHITE)
        self.perimeter = self.surface.get_rect(center=place)
        self.text = text
