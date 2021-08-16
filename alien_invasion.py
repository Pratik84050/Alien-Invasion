import sys
import pygame

class AlienInvasion:
    """Overall class ti manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resoures."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

def run_game(self):
    """Start the main loop for the game."""
    while True:
        # Watch for keyword and mouse events.
        for event in pygame.events.get():
            if event.type == pygame.QUIT:
                sys.exit()


        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == 'main':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()