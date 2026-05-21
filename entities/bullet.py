import pygame
from entities.base_entity import BaseEntity
from settings import BULLET_RADIUS, BULLET_LIFETIME, YELLOW


class Bullet(BaseEntity):
    def __init__(self, x, y, vel):
        super().__init__(x, y)
        self.lifetime = BULLET_LIFETIME

        size = BULLET_RADIUS * 2
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (BULLET_RADIUS, BULLET_RADIUS), BULLET_RADIUS)
        self.rect = self.image.get_rect(center=(int(x), int(y)))

        self.vel = vel

    def update(self):
        super().update()
        self.lifetime -= 1
        if self.lifetime <= 0:
            self.kill()

        # wrap around screen edges
        sw, sh = pygame.display.get_surface().get_size()
        self.pos.x %= sw
        self.pos.y %= sh
        self.rect.center = (int(self.pos.x), int(self.pos.y))
