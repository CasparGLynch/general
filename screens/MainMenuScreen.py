from pygame import Surface, display
from pygame.event import Event

from screens.BaseScreen import BaseScreen


class MainMenuScreen(BaseScreen):

    def __init__(self, screen_width: int, screen_height: int):
        super().__init__(screen_width=screen_width, screen_height=screen_height)

    def render(self, screen: display):
        # Render the main menu screen
        screen.fill(color=(0, 100, 0))

    def update(self):
        pass

    def handle_input(self, event: Event):
        super().handle_input(event=event)
