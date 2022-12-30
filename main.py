import pygame

from screens.BaseScreen import BaseScreen
from screens.GameScreen import GameScreen
from screens.MainMenuScreen import MainMenuScreen

# Initialize Pygame and create a window
pygame.init()


class Game:
    # Set the initial screen to the main menu screen
    def __init__(self, screen_width, screen_height):
        self.pyscreen = pygame.display.set_mode((screen_width, screen_height))
        self.current_screen = MainMenuScreen(screen_width, screen_height)

    # Main game loop

    def run(self):
        while self.current_screen.running:
            for event in pygame.event.get():
                self.current_screen.handle_input(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # Switch to a new game screen when the SPACE key is pressed
                        if isinstance(self.current_screen, MainMenuScreen):
                            screen_width = self.current_screen.screen_width
                            screen_height = self.current_screen.screen_height
                            self.current_screen = GameScreen(
                                screen_width=screen_width,
                                screen_height=screen_height,
                                level=0
                            )
                        elif isinstance(self.current_screen, GameScreen):
                            screen_width = self.current_screen.screen_width
                            screen_height = self.current_screen.screen_height
                            self.current_screen = MainMenuScreen(
                                screen_width=screen_width,
                                screen_height=screen_height,
                            )
            # Update and render the current screen
            self.current_screen.render(self.pyscreen)
            pygame.display.flip()


if __name__ == '__main__':
    game = Game(1600, 800)
    game.run()
