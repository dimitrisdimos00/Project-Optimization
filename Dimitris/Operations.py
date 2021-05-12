import numpy as np
import random

def f(x):
    return x**2

class operations:
    def __init__(self, population):
        self.population = population
        self.designVectors = self.population.all_design_vectors
        self.n = population.pop_size

        self.fitness_values = self.evaluate()
        self.sum_of_fvalues = self.calculateSumOfFvals()
        self.averageOfFvals = self.sum_of_fvalues * (1 / self.population.getPopulationSize())

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


    def singlePointMutation(self, bin_value, max_mutation_prob):
        pm = random.uniform(0, max_mutation_prob)
        prob_mutation_sucess = random.uniform(0, 1)

        if prob_mutation_sucess <= pm:
            q = bin_value.size
            site = random.randint(0, q)
            if bin_value[site] == 1:
                bin_value[site] = 0
            else:
                bin_value[site] = 1
        return bin_value

    def crossover(self, bin_value1, bin_value2):
        q = bin_value1.size
        site = random.randint(0, q - 1)
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

    def calculateNewPopulation(self, mates): 
        # mates is a list
        length = len(mates)
        new__design_vectors = [None] * length
        for i in range(0, length, 2):
            parent1 = mates[i]
            parent2 = mates[i + 1]
            offspring1, offspring2 = self.crossover(parent1.value_bin, parent2.value_bin)
            
            new_population[i] = offspring1
            new_population[i + 1] = offspring2
        
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

        # allDesVec = self.population.all_design_vectors
        # print("\n Selected Mates Real Values: ")
        # for m in self.mates:
        #     print(allDesVec[m].printDesignVector())
