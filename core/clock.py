import pygame


class Clock:
    def __init__(self, fps):
        self._clock = pygame.time.Clock()
        self.fps = fps

    def tick(self):
        return self._clock.tick(self.fps)

    def get_fps(self):
        return self._clock.get_fps()
