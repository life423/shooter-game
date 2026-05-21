import pygame


class InputHandler:
    def get_keys(self):
        return pygame.key.get_pressed()

    def process_events(self):
        """Returns False if the user quit."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return False
        return True
