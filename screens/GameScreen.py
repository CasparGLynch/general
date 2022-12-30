# Pygame
from pygame import Surface
from pygame.event import Event

# Screens
from screens.BaseScreen import BaseScreen


class GameScreen(BaseScreen):

    def __init__(self, screen_width: int, screen_height: int, level: int):
        super().__init__(screen_width=screen_width, screen_height=screen_height)
        self.level = level

    def render(self, screen: Surface):
        screen.fill(color=(0, 0, 100))

    def handle_input(self, event: Event):
        super().handle_input(event=event)
