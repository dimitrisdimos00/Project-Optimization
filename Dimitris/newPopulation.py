import numpy as np
import random

class population:
    def __init__(self, size, central_point, radius):
    #, dx):
        self.size = size
        #self.dx = dx
        x_min = central_point[0] - radius
        x_max = central_point[0] + radius
        y_min = central_point[1] - radius
        y_max = central_point[1] + radius
        self.population = []
        current_size = 0
        while (current_size < size):
            x = random.uniform(x_min, x_max)
            y = random.uniform(y_min, y_max)
            d = np.sqrt((central_point[0] - x)**2 + (central_point[1] - y)**2)
            if (d <= radius):
                self.population.append((x, y))
                current_size +=1
        
    def crossover(g1, g2, alpha):
        gamma = random.uniform(-alpha, 1 + alpha)
        return round((gamma * g1 + (1 - gamma) * g2), 4)
    
    def recreate(self, function, crossover_probability):
        n = self.size
        
        fitness_values = [None] * n
        for i in range(n):
            fitness_values[i] = (1 / (1 + function(self.population[i][0], self.population[i][1])))
        
        selection_probability = [None] * n
        value_sum = sum(fitness_values)
        for i in range(n):
            selection_probability[i] = fitness_values[i] / value_sum
        
        cummulative_probability = [None] * n
        prob_sum = selection_probability[0]
        for i in range(0, n):
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
                    offspring1 = self.crossover(mates[parent1_index], mates[parent2_index], 0.5)
                    offspring2 = self.crossover(mates[parent1_index], mates[parent2_index], 0.5)
                    new_population[parent1_index] = offspring1
                    new_population[parent2_index] = offspring2
                    parent1 = parent2 = False      

    # def setPopulation(self, x_array, y_array):
    #     self.x_array = x_array
    #     self.y_array = y_array
    #     self.size = len(x_array)

    def print(self):
        for i in range(0, self.size):
            print("\n")
            print("no.", i + 1)
            print("x:", self.x_array[i])
            print("y:", self.y_array[i])