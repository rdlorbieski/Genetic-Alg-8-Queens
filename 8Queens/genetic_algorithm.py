import random

class GeneticAlgorithm:
    """
    A class representing a genetic algorithm for solving the 8-queens problem.
    """

    def __init__(self, population_size):
        """
        Initializes a new instance of the GeneticAlgorithm class.

        Parameters:
        - population_size (int): The size of the population.
        """
        self.population_size = population_size
        self.population = [self.generate_individual() for _ in range(population_size)]

    def generate_individual(self):
        """
        Generates a random individual for the initial population.

        Returns:
        - list[int]: A list representing the individual.
        """
        return [random.randint(0, 7) for _ in range(8)]

    def fitness(self, individual):
        """
        Calculates the fitness of a given individual based on the number of non-conflicting queens.

        Parameters:
        - individual (list[int]): The individual to evaluate.

        Returns:
        - int: The fitness value of the individual.
        """
        conflicts = 0
        for i in range(8):
            for j in range(i+1, 8):
                if individual[i] == individual[j] or abs(individual[i] - individual[j]) == j - i:
                    conflicts += 1
        return 8 - conflicts

    def select_parents(self):
        """
        Selects the two fittest parents from the population.

        Returns:
        - list[list[int]]: The two selected parents.
        """
        parents = sorted(self.population, key=self.fitness, reverse=True)[:2]
        return parents

    def crossover(self, parent1, parent2):
        """
        Performs a crossover operation between two parents.

        Parameters:
        - parent1 (list[int]): The first parent.
        - parent2 (list[int]): The second parent.

        Returns:
        - tuple[list[int], list[int]]: The two offspring.
        """
        crossover_point = random.randint(1, 6)
        offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
        offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
        return offspring1, offspring2

    def mutation(self, individual):
        """
        Mutates a given individual with a 20% probability.

        Parameters:
        - individual (list[int]): The individual to mutate.

        Returns:
        - list[int]: The mutated individual.
        """
        if random.random() < 0.2:
            position = random.randint(0, 7)
            individual[position] = random.randint(0, 7)
        return individual

    def new_generation(self):
        """
        Generates a new population by selecting parents, performing crossover, and mutation.
        """
        parents = self.select_parents()
        offspring = []
        for i in range(0, self.population_size, 2):
            child1, child2 = self.crossover(*parents)
            child1 = self.mutation(child1)
            child2 = self.mutation(child2)
            offspring += [child1, child2]
        self.population = offspring

    def genocide(self, survival_percentage=0):
        """
        Kills off a portion of the population and replaces them with new random individuals.

        Parameters:
        - survival_percentage (float): The percentage of the population to keep.
        """
        number_survivors = int(self.population_size * survival_percentage)
        survivors = sorted(self.population, key=self.fitness, reverse=True)[:number_survivors]
        self.population = survivors + [self.generate_individual() for _ in
                                       range(self.population_size - number_survivors)]

    def run(self, generations):
        """
        Executes the genetic algorithm for a specified number of generations.

        Parameters:
        - generations (int): The number of generations to run the algorithm for.
        """
        for generation in range(generations):
            print(f"Generation {generation}: Best individual: {max(self.population, key=self.fitness)} with fitness: {self.fitness(max(self.population, key=self.fitness))}")
            self.new_generation()

    def best_individual(self):
        """
        Returns the best individual from the population.

        Returns:
        - list[int]: The best individual.
        """
        return max(self.population, key=self.fitness)


if __name__ == "__main__":
    ga = GeneticAlgorithm(100)
    ga.run(1000)
