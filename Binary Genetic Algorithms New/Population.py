import numpy as np
import random

class Population:

    def __init__(self, size, central_point, radius, function, mode="min"):
        self.size = size
        self.function = function
        self.mode = mode
        self.population = []
       
        x_min = central_point[0] - radius
        x_max = central_point[0] + radius
        y_min = central_point[1] - radius
        y_max = central_point[1] + radius

        current_size = 0
        while (current_size < size):
            x = random.uniform(x_min, x_max)
            y = random.uniform(y_min, y_max)
            d = np.sqrt((central_point[0] - x) ** 2 + (central_point[1] - y) ** 2)
            if (d <= radius):
                self.population.append((x, y))
                current_size +=1

        self.fitness_values = [None] * self.size
        self.average = 0
        self.evaluate()

    def evaluate(self) -> None:
        if(self.mode == "min"):
            # find the fitness value F(x) = 1 / (1 + f(x)) for minimum
            self.fitness_values = [1 / (1 + self.function(ind[0], ind[1])) for ind in self.population]
        else:
            # find the fitness value F(x) = f(x) for maximum
            self.fitness_values = [self.function(ind[0], ind[1]) for ind in self.population]
        
        self.average = sum(self.fitness_values) / self.size

    def recreate(self, crossover_probability, mutation_probability):
        
        def crossover(g1, g2, alpha=0.5):
            gamma = random.uniform(-alpha, 1 + alpha)
            return gamma * g1 + (1 - gamma) * g2

        n = self.size

        value_sum = sum(self.fitness_values)
        selection_probability = [sp / value_sum for sp in self.fitness_values]

        cummulative_probability = [None] * n
        prob_sum = selection_probability[0]
        for i in range(n):
            cummulative_probability[i] = prob_sum
            prob_sum += selection_probability[i]
        
        mates = [None] * n
        for j in range(n):
            # find the index of the element to be selected with roulette method
            index = 0
            r = random.uniform(0, 1)
            for i in range(1, n):
                if cummulative_probability[i - 1] < r and r <= cummulative_probability[i]:
                    index = i
            mates[j] = self.population[index]

        new_population = mates.copy()

        # crossovers
        parent1 = parent2 = False
        parent1_index = parent2_index = 0
        for i in range(n):
            if random.uniform(0, 1) <= crossover_probability:
                if not parent1:
                    parent1_index = i
                    parent1 = True
                elif not parent2:
                    parent2_index = i
                    parent2 = True
                else:
                    offspring1 = (crossover(mates[parent1_index][0], mates[parent2_index][0]), crossover(mates[parent1_index][1], mates[parent2_index][1]))
                    offspring2 = (crossover(mates[parent1_index][0], mates[parent2_index][0]), crossover(mates[parent1_index][1], mates[parent2_index][1]))
                    new_population[parent1_index] = offspring1
                    new_population[parent2_index] = offspring2
                    parent1 = parent2 = False
        
        # mutations
        for i in range(n):
            if random.uniform(0, 1) <= mutation_probability:
                m = (new_population[i][1], new_population[i][0])
                new_population[i] = m
        
        self.population = new_population
        self.evaluate()
    
    def converges(self, limit):

        def standard_deviation(values):
            n = len(values)
            mean = sum(values) / n
            diff = [i - mean for i in values]
            diff_2 = [x ** 2 for x in diff]
            my_sum = sum(diff_2)
            return np.sqrt(my_sum / n)
        
        x_array = self.population[:][0]
        y_array = self.population[:][1]

        if standard_deviation(x_array) <= limit and standard_deviation(y_array) <= limit:
            return True
        return False

    def print_status(self) -> None:
        """Prints the current status of the population."""
        fvmin = min(self.fitness_values)
        fvmax = max(self.fitness_values)
        indmax = self.fitness_values.index(fvmax)
        indmin = self.fitness_values.index(fvmin)
        best_x, best_y = self.population[indmax]
        
        # The best individual is always the one with the highest *fitness*
        # regardless of min/max mode.
        print(f"Avg Fitness: {self.average:.3f} | Best Individual: ({best_x:.3f}, {best_y:.3f}) | Best Fitness: {fvmax:.3f}")