import time

import pygame

import defs
from screens.GameScreen import GameScreen
from screens.MainMenuScreen import MainMenuScreen

# Initialize Pygame and create a window
pygame.init()
pygame.key.set_repeat(1, 40)


class Game:
    # Set the initial screen to the main menu screen
    def __init__(self, screen_width, screen_height):
        self.pyscreen = pygame.display.set_mode((screen_width, screen_height))
        self.current_screen = MainMenuScreen(screen_width, screen_height)
        self.clock = time.time()

    # Main game loop

    def run(self):
        while self.current_screen.running:
            for event in pygame.event.get():
                self.current_screen.handle_input(event=event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # Switch to a new game screen when the SPACE key is pressed
                        if isinstance(self.current_screen, MainMenuScreen):
                            screen_width = self.current_screen.screen_width
                            screen_height = self.current_screen.screen_height
                            self.current_screen = GameScreen(
                                screen_width=screen_width,
                                screen_height=screen_height,
                                level=0,
                                clock=self.clock
                            )
                            self.pyscreen.fill(color=(0, 0, 100))

            # Update and render the current screen
            self.current_screen.update(screen=self.pyscreen)

            self.current_screen.render(screen=self.pyscreen)
            pygame.display.flip()


if __name__ == '__main__':
    game = Game(screen_width=defs.screen_width, screen_height=defs.screen_width)
    game.run()
