import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, TITLE
from core.input_handler import InputHandler
from core.renderer import Renderer
from core.clock import Clock
from entities.player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.screen  = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)

        self.clock   = Clock(FPS)
        self.input   = InputHandler()
        self.renderer = Renderer(self.screen)

        self.all_sprites  = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()

        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.all_sprites.add(self.player)

    def run(self):
        running = True
        while running:
            self.clock.tick()
            running = self.input.process_events()
            keys = self.input.get_keys()

            self.player.handle_input(keys, self.bullet_group, self.all_sprites)
            self.all_sprites.update()

            self.renderer.clear()
            self.renderer.draw_group(self.all_sprites)
            self.renderer.flip()

        pygame.quit()
