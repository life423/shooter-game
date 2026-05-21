import pygame
from settings import BLACK


class Renderer:
    def __init__(self, screen):
        self.screen = screen

    def clear(self):
        self.screen.fill(BLACK)

    def draw_group(self, group):
        group.draw(self.screen)

    def flip(self):
        pygame.display.flip()
