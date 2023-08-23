import pygame

class Visualization:
    """
    A class representing a visualization for the 8-queens problem using pygame.
    """

    def __init__(self):
        """
        Initializes a new instance of the Visualization class.
        """
        pygame.init()
        self.width = 400
        self.height = 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.icon = pygame.image.load('queen.png')

        pygame.display.set_caption('Eight Queens Problem')

    def draw_queen_icon(self, solution):
        """
        Draws the chessboard and places the queen icons based on the provided solution.

        Parameters:
        - solution (list[int]): A list representing the solution of the 8-queens problem.
        """
        self.screen.fill((255, 255, 255))  # White background

        cell_size = self.width // 8

        # Resizing the icon to fit within the cells
        icon_scaled = pygame.transform.scale(self.icon, (cell_size, cell_size))

        # Draw chessboard and queens
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    pygame.draw.rect(self.screen, (0, 0, 0), (col * cell_size, row * cell_size, cell_size, cell_size))

                # Drawing the queen icon in the place of the red circle
                if solution[col] == row:
                    self.screen.blit(icon_scaled, (col * cell_size, row * cell_size))

        pygame.display.flip()

    def close(self):
        """
        Closes the pygame window.
        """
        pygame.quit()
