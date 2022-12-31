import pygame
from pygame.event import Event

import defs


class Player:
    def __init__(self, x: int, y: int, sprite_image: str):
        self.x = x
        self.y = y
        self.target_x = x
        self.target_y = y
        self.sprite = pygame.image.load(sprite_image).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (defs.screen_width / 15, defs.screen_width / 15))
        self.rect = self.sprite.get_rect(topleft=(self.x, self.y))
        self.velocity = 3
        self.lerp_factor = 0.05

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.target_y -= self.velocity
        if keys[pygame.K_s]:
            self.target_y += self.velocity
        if keys[pygame.K_a]:
            self.target_x -= self.velocity
        if keys[pygame.K_d]:
            self.target_x += self.velocity

        # movement smoothening

        self.x = self.x + (self.target_x - self.x) * self.lerp_factor
        self.y = self.y + (self.target_y - self.y) * self.lerp_factor
        self.rect.topleft = (self.x, self.y)
