import pygame
from pygame import display
from pygame.event import Event


class BaseScreen:
    def __init__(self, screen_width: int, screen_height: int):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.running = True

    def render(self, screen: display):
        # Render the screen
        raise NotImplementedError()

    def update(self):
        raise NotImplementedError()

    def handle_input(self, event: Event):
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False
