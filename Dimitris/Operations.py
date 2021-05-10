import numpy as np
import random

def f(x):
    return x**2

class operations:
    def __init__(self, population):
        self.population = population
        self.n = population.pop_size

        self.fitness_values = self.evaluate()
        self.sum_of_fvalues = self.calculateSumOfFvals()
        self.averageOfFvals = self.sum_of_fvalues * (1 / self.population.getPopulationSize())

        self.probabilities_of_selection = self.findProbabilitiesOfSelection()
        self.cummulative_probabilities = self.findCummulativeProbabilities()

        self.mates = self.findMates()

        
    
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
        
    def findMates(self):
        selectedMates = []
        for j in range(self.n):
            r = random.uniform(0,1)
         
            length = len(self.cummulative_probabilities)
            for i in range(1, length):
                if r > self.cummulative_probabilities[i - 1] and r <= self.cummulative_probabilities[i]:
                    selectedMates.append(i + 1)
        return selectedMates

    def print(self):
        self.population.printPopulation()
        print("\n Fitness Values: ")
        print(self.fitness_values)

        print("\n Probability of selection: ")
        print(self.probabilities_of_selection)

        
        print("\n Cummulative probabilities: ")
        print(self.cummulative_probabilities)

        print("\n Average of fitness values: ")
        print(self.averageOfFvals)

        print("\n Selected Mates: ")
        print(self.mates)

        # allDesVec = self.population.all_design_vectors
        # print("\n Selected Mates Real Values: ")
        # for m in self.mates:
        #     print(allDesVec[m].printDesignVector())
