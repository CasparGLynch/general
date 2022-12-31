# Pygame
import pygame
from pygame import display
from pygame.event import Event

from objects.Player import Player
# Screens
from screens.BaseScreen import BaseScreen


class GameScreen(BaseScreen):

    def __init__(self, screen_width: int, screen_height: int, level: int, clock: float):
        super().__init__(screen_width=screen_width, screen_height=screen_height)
        self.level = level
        self.clock = clock
        self.player = Player(0, 0, "images/player.png", clock)

        self.background_image = pygame.image.load("images/background.png")
        self.background_image = pygame.transform.scale(self.background_image, (1920, 1080))

    def render(self, screen: display):
        screen.fill(color=(0, 0, 100))
        screen.blit(self.background_image, (0, 0))
        screen.blit(self.player.sprite, self.player.rect)

    def update(self):
        self.player.move()

    def handle_input(self, event: Event):
        super().handle_input(event=event)
