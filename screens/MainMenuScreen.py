import pygame

from screens.BaseScreen import BaseScreen
from screens.GameScreen import GameScreen


class MainMenuScreen(BaseScreen):

    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)

    def render(self, screen):
        # Render the main menu screen
        screen.fill((0, 100, 0))

    def handle_input(self, event):
        super().handle_input(event)
        # Handle input events for the main menu screen


