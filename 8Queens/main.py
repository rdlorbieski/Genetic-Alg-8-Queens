from genetic_algorithm import GeneticAlgorithm
from visualization import Visualization
import pygame
import time

def main():
    """
    The main function to run the genetic algorithm for the 8-queens problem and visualize its progress using pygame.
    """
    ga = GeneticAlgorithm(200)
    viz = Visualization()
    for generation in range(1000):
        print(f"Generation {generation}: Best individual: {ga.best_individual()} with fitness: {ga.fitness(ga.best_individual())}")
        ga.new_generation()
        if ga.fitness(ga.best_individual()) == 8:  # Check if the solution has already been found
            print("Solution found!")
            break
        else:
            viz.draw_queen_icon(ga.best_individual())
            time.sleep(0.05)
            if generation % 20 == 0:
                ga.genocide()

    print("GA Completed. Press 'Esc' to exit.")

    # Loop to keep the visualization window open
    while True:
        viz.draw_queen_icon(ga.best_individual())
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    viz.close()
                    return
            elif event.type == pygame.QUIT:
                viz.close()
                return

if __name__ == "__main__":
    main()
