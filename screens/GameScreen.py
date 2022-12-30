import pygame

from screens.BaseScreen import BaseScreen


class GameScreen(BaseScreen):

    def __init__(self, screen_width, screen_height, level):
        super().__init__(screen_width=screen_width, screen_height=screen_height)
        self.level = level

    def render(self, screen):
        screen.fill((100, 10, 0))

    def handle_input(self, event):
        super().handle_input(event)
