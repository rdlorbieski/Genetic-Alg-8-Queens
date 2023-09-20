
# 8-Queens Genetic Algorithm Visualization

## Overview

This program uses a genetic algorithm to solve the classic 8-Queens problem. The 8-Queens puzzle involves placing eight queens on an 8x8 chessboard so that no two queens threaten each other. The genetic algorithm iteratively refines a population of solutions to approach an optimal solution to the problem.

To enhance the understanding of the algorithm's workings, the program visualizes the placement of queens on a chessboard for the best solution in the current generation, updating the visualization as the algorithm progresses.

## Features

- Genetic algorithm implementation for the 8-Queens problem.
- Dynamic visualization of the best solution in each generation using pygame.
- Interactive display, allowing users to exit the visualization upon finding a solution or at any point they wish.

## Requirements

- Python 3.x
- `pygame` library

To install the required library, run:
```
pip install pygame
```

## Usage

1. Clone the repository or download the source code.
2. Navigate to the directory containing the program files.
3. Run the main script with:
```
python main.py
```
4. Watch the visualization as the genetic algorithm iteratively improves the solutions.
5. Once a solution is found or if you wish to exit at any point, press 'Esc' or close the pygame window.

## Files

- `genetic_algorithm.py`: Contains the implementation of the genetic algorithm for the 8-Queens problem.
- `visualization.py`: Provides functionality to visualize the chessboard and the placement of queens using pygame.


## Demonstration of Results
![Logo](https://rodolfo.lorbieski.eti.br/img/portfolio/projetos/8queens.png)
