import pygame
import time
from pygame.event import Event
from pygame.time import Clock

import defs


class Player:
    def __init__(self, x: int, y: int, sprite_image: str, clock: float):
        self.x = x
        self.y = y
        self.target_x = x
        self.target_y = y
        self.sprite = pygame.image.load(sprite_image).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (defs.screen_width / 15, defs.screen_width / 15))
        self.rect = self.sprite.get_rect(topleft=(self.x, self.y))
        self.velocity = 1.25
        self.lerp_factor = 0.05
        self.moving_left = False
        self.clock = clock
        self.images = ['images/player.png', 'images/player_move.png']

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
        new_x = self.x + (self.target_x - self.x) * self.lerp_factor
        new_y = self.y + (self.target_y - self.y) * self.lerp_factor

        # image changer for when Lardon is in movement
        if (abs(new_x) > abs(self.x) + 0.5) | (abs(new_x) < abs(self.x) - 0.5):
            if time.time() - self.clock > 0.16:
                image = self.images.pop()
                self.sprite = pygame.image.load(image).convert_alpha()
                self.sprite = pygame.transform.scale(self.sprite, (defs.screen_width / 15, defs.screen_width / 15))
                self.images.insert(0, image)
                self.moving_left = False
                self.clock = time.time()
        # flip sides
        if (new_x < self.x) and not self.moving_left:
            self.sprite = pygame.transform.flip(self.sprite, True, False)
            self.moving_left = True
        elif (new_x >= self.x) and self.moving_left:
            self.sprite = pygame.transform.flip(self.sprite, True, False)
            self.moving_left = False

        self.x = new_x
        self.y = new_y

        self.rect.topleft = (self.x, self.y)
