import pygame
import math
from entities.base_entity import BaseEntity
from entities.bullet import Bullet
from settings import (
    PLAYER_SPEED, ROTATE_SPEED, FRICTION,
    PLAYER_SIZE, BULLET_SPEED, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT,
)


def _build_surface(size):
    """Draw a triangle pointing up (angle 0 = up)."""
    surf = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
    tip    = (size,          0)
    left   = (0,             size * 2)
    right  = (size * 2,      size * 2)
    pygame.draw.polygon(surf, WHITE, [tip, left, right])
    return surf


class Player(BaseEntity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.angle = 0          # degrees; 0 = pointing up
        self._base_surf = _build_surface(PLAYER_SIZE)
        self.image = self._base_surf
        self.rect  = self.image.get_rect(center=(int(x), int(y)))
        self._shoot_cooldown = 0

    def _facing_vec(self):
        rad = math.radians(self.angle)
        return pygame.math.Vector2(math.sin(rad), -math.cos(rad))

    def handle_input(self, keys, bullet_group, all_sprites):
        if keys[pygame.K_a]:
            self.angle -= ROTATE_SPEED
        if keys[pygame.K_d]:
            self.angle += ROTATE_SPEED
        if keys[pygame.K_w]:
            self.vel += self._facing_vec() * PLAYER_SPEED

        self._shoot_cooldown = max(0, self._shoot_cooldown - 1)
        if keys[pygame.K_SPACE] and self._shoot_cooldown == 0:
            self._fire(bullet_group, all_sprites)
            self._shoot_cooldown = 15

    def _fire(self, bullet_group, all_sprites):
        fv = self._facing_vec()
        tip = self.pos + fv * PLAYER_SIZE
        bvel = self.vel + fv * BULLET_SPEED
        b = Bullet(tip.x, tip.y, bvel)
        bullet_group.add(b)
        all_sprites.add(b)

    def update(self):
        self.vel *= FRICTION
        super().update()

        # screen wrap
        self.pos.x %= SCREEN_WIDTH
        self.pos.y %= SCREEN_HEIGHT
        self.rect.center = (int(self.pos.x), int(self.pos.y))

        # rotate sprite to match angle
        self.image = pygame.transform.rotate(self._base_surf, -self.angle)
        self.rect  = self.image.get_rect(center=self.rect.center)
