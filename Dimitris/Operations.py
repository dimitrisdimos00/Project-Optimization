import numpy as np
import random
from DesignVariable import designVec
from Population import population
def f(x):
    return x**2

class operations:
    def __init__(self, pop_size, min, max, dx): 
        self.population = population(pop_size, min, max, dx)
        self.designVectors = self.population.all_design_vectors
        self.max = max
        self.min = min
        self.dx = dx
        
        self.n = pop_size

        self.fitness_values = self.evaluate()
        self.sum_of_fvalues = self.calculateSumOfFvals()
        self.averageOfFvals = self.sum_of_fvalues * (1 / self.n)

        self.probabilities_of_selection = self.findProbabilitiesOfSelection()
        self.cummulative_probabilities = self.findCummulativeProbabilities()

        self.mates, self.matesNo = self.findMates(self.designVectors, self.cummulative_probabilities)

    def setOperations(self, population):
        self.population = population
        self.designVectors = population.all_design_vectors
        self.max = self.designVectors[0].max_value
        self.min = self.designVectors[0].min_value
        self.dx = self.designVectors[0].dx
        self.n = self.population.pop_size

        self.fitness_values = self.evaluate()
        self.sum_of_fvalues = self.calculateSumOfFvals()
        self.averageOfFvals = self.sum_of_fvalues * (1 / self.n)

        self.probabilities_of_selection = self.findProbabilitiesOfSelection()
        self.cummulative_probabilities = self.findCummulativeProbabilities()

        self.mates, self.matesNo = self.findMates(self.designVectors, self.cummulative_probabilities)


    def evaluate(self):
        eval_value = []
        for dv in self.population.all_design_vectors:
            fitness_value = 1 / (1 + f(dv.value_dec)) # find the fitness value 
            eval_value.append(fitness_value)
        return eval_value
    
    def calculateSumOfFvals(self):
        sum = 0
        for fv in self.fitness_values:
            sum += fv
        return sum

    def findProbabilitiesOfSelection(self):
        pos = []
        for fv in self.fitness_values:
            p = fv / self.sum_of_fvalues
            pos.append(p)
        return pos

    def findCummulativeProbabilities(self):
        cumProb = []
        current_sum = self.probabilities_of_selection[0]
        cumProb.append(current_sum)

        length = len(self.probabilities_of_selection)
        for i in range(1, length):
            current_sum += self.probabilities_of_selection[i]
            cumProb.append(current_sum)
            
        return cumProb
        
    def findMates(self, designVectors, cumProb):
        n = len(designVectors)
        selectedMates = [None] * n
        selectedMatesIndex = [None] * n

        for j in range(n):
            r = random.uniform(0,1)
            selectedIndex = 0
            # find the index of the element to be selected
            for i in range(1, n):
                if r > cumProb[i - 1] and r <= cumProb[i]:
                    selectedIndex = i
            
            selectedMates[j] = designVectors[selectedIndex]
            selectedMatesIndex[j] = selectedIndex

        return selectedMates, selectedMatesIndex

    def singlePointMutation(self, bin_value, pm):
        
        prob_mutation_sucess = random.uniform(0, 1)
        site = -1
        if prob_mutation_sucess <= pm:
            q = bin_value.size
            site = random.randint(0, q - 1)
            if bin_value[site] == 1:
                bin_value[site] = 0
            else:
                bin_value[site] = 1
        return bin_value

    def crossover(self, bin_value1, bin_value2):
        q = bin_value1.size
        site = random.randint(0, q - 2)
        offspring1 = np.zeros(q, dtype='int')
        offspring2 = np.zeros(q, dtype='int')
        
        for i in range(q):
            if i <= site:
                offspring1[i] = bin_value1[i]
                offspring2[i] = bin_value2[i] 
            else:
                offspring1[i] = bin_value2[i]
                offspring2[i] = bin_value1[i]
        
        return offspring1, offspring2

    def calculateNewPopulation(self, mates, pm): 
        # mates is a list
        length = len(mates)
        new_design_vectors = [None] * length
        for i in range(0, length, 2):
            # select parents
            parent1 = mates[i]
            parent2 = mates[i + 1]
            
            # calculate crossover
            offspring1, offspring2 = self.crossover(parent1.value_bin, parent2.value_bin)

            # calculate mutations
            offspring1 = self.singlePointMutation(offspring1, pm)
            offspring2 = self.singlePointMutation(offspring2, pm)

            # set the new design vectors in a list
            dv1 = designVec(self.min, self.max, self.dx)
            dv1.setValue(offspring1, self.min, self.max, self.dx)
            dv2 = designVec(self.min, self.max, self.dx)
            dv2.setValue(offspring2, self.min, self.max, self.dx)
            new_design_vectors[i] = dv1
            new_design_vectors[i + 1] = dv2
        
        # create a new population from the new design vector list
        new_population = population(self.n, self.min, self.max, self.dx)
        new_population.setAllDesignVectors(new_design_vectors)
        return new_population


    def print(self):
        self.population.printPopulation()
        # print("\n Fitness Values: ")
        # print(self.fitness_values)

        print("\n Probability of selection: ")
        print(self.probabilities_of_selection)

        # print("\n Cummulative probabilities: ")
        # print(self.cummulative_probabilities)

        print("\n Average of fitness values: ")
        print(self.averageOfFvals)

        print("\n Selected Mates: ")
        n = len(self.mates)
        for i in range(n):
            print("no. ", self.matesNo[i])
            print(self.mates[i].printDesignVector())


