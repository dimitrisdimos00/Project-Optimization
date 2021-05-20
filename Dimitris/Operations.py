import numpy as np
import random
from DesignVariable import designVec
from Population import population
def f(x):
    return x**2

def ackley(x, y):
    return -20 * np.exp( -0.2 * np.sqrt( 0.5 * (x ** 2 + y ** 2))) - np.exp( 0.5 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))) + np.exp(1) + 20
    

class operations:
    def __init__(self, population): 
        self.population = population
        self.designVectors = population.all_design_vectors
        self.max_d1 = population.max_value_d1
        self.min_d1 = population.min_value_d1
        self.max_d2 = population.max_value_d2
        self.min_d2 = population.min_value_d2
        self.dx = population.dx
        
        self.n = population.pop_size

        self.fitness_values = self.evaluate()
        self.sum_of_fvalues = self.calculateSumOfFvals()
        self.averageOfFvals = self.sum_of_fvalues * (1 / self.n)

        self.probabilities_of_selection = self.findProbabilitiesOfSelection()
        self.cummulative_probabilities = self.findCummulativeProbabilities()

        self.mates, self.matesNo = self.findMates(self.designVectors, self.cummulative_probabilities)

    def evaluate(self):
        eval_value = []
        for vector2d in self.population.all_design_vectors:
            fitness_value = 1 / (1 + ackley(vector2d[0].value_dec, vector2d[1].value_dec)) # find the fitness value 
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

    # no need to change despite the dimensions of the design vectors
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
    
    # no need to change despite the dimensions of the design vectors
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

    def calculateNewPopulation(self, mates, pm, pc): 
        max_d1 = self.max_d1
        min_d1 = self.min_d1
        max_d2 = self.max_d2
        min_d2 = self.min_d2
        dx = self.dx

        # mates is a list of 2d vectors
        length = len(mates)

        # initialize the new 2d vectors' list
        new_design_vectors = [None] * length

        parent1_found = False
        parent2_found = False
        parent1_position = 0
        parent2_position = 0

        for k in range(len(mates)):
            prob_crossover_sucess = random.uniform(0, 1)
            
            if prob_crossover_sucess <= pc:
                if not parent1_found:
                    parent1 = mates[k]
                    parent1_position = k
                    parent1_found = True
                elif not parent2_found:
                    parent2 = mates[k]
                    parent2_position = k
                    parent2_found = True
            new_design_vectors[k] = mates[k]
                

            if parent1_found and parent2_found:
                p1valb0 = parent1[0].value_bin
                p1valb1 = parent1[1].value_bin
                bin_array1 = np.concatenate((parent1[0].value_bin, parent1[1].value_bin), axis = None)
                bin_array2 = np.concatenate((parent2[0].value_bin, parent2[1].value_bin), axis = None)

                offspring1, offspring2 = self.crossover(bin_array1, bin_array2)

                # divide the new binary arrays into two equally sized arrays
                bin_array_1_offspring_1, bin_array_2_offspring_1 = np.split(offspring1, 2)
                bin_array_1_offspring_2, bin_array_2_offspring_2 = np.split(offspring2, 2)
                
                # set the new design vectors in a list
                # offspring 1:
                dv1_offspring1 = designVec(min_d1, max_d1, dx)
                dv1_offspring1.setValue(bin_array_1_offspring_1, min_d1, max_d1, dx)

                dv2_offspring1 = designVec(min_d2, max_d2, dx)
                dv2_offspring1.setValue(bin_array_2_offspring_1, min_d2, max_d2, dx)

                # offspring 2:
                dv1_offspring2 = designVec(min_d1, max_d1, dx)
                dv1_offspring2.setValue(bin_array_1_offspring_2, min_d1, max_d1, dx)

                dv2_offspring2 = designVec(min_d2, max_d2, dx)
                dv2_offspring2.setValue(bin_array_2_offspring_2, min_d2, max_d2, dx)
            
                # create the new 2d vector for each offspring
                offspring2d_1 = (dv1_offspring1, dv2_offspring1)
                offspring2d_2 = (dv1_offspring2, dv2_offspring2)

                # pass the new offspring vector inside the new list
                new_design_vectors[parent1_position] = offspring2d_1
                new_design_vectors[parent2_position] = offspring2d_2
                
                parent1_found = False
                parent2_found = False
        
        # calculate the mutation for each vector
        for k in range(len(new_design_vectors)):
            vector2d = new_design_vectors[k]
            
            bin_value = np.concatenate((new_design_vectors[k][0].value_bin, new_design_vectors[k][1].value_bin), axis = None)
            bin_value = self.singlePointMutation(bin_value, pm)
            # split the result into 2 equal size arrays
            bin_value1, bin_value2 = np.split(bin_value, 2)

            # create 2 new design vectors with the new values
            dv1 = designVec(min_d1, max_d1, dx)
            dv1.setValue(bin_value1, min_d1, max_d1, dx)

            dv2 = designVec(min_d2, max_d2, dx)
            dv2.setValue(bin_value2, min_d2, max_d2, dx)

            # create a new 2d vector as a tuple
            vector2d = (dv1, dv2)
            new_design_vectors[k] = vector2d

        # create a new population from the new design vector list
        new_population = population(self.n, min_d1, max_d1, min_d2, max_d2, dx)
        new_population.setAllDesignVectors(new_design_vectors)
        return new_population

    def print(self):
        # self.population.printPopulation()
        # print("\n Fitness Values: ")
        # print(self.fitness_values)

        # print("\n Probability of selection: ")
        # print(self.probabilities_of_selection)

        # print("\n Cummulative probabilities: ")
        # print(self.cummulative_probabilities)

        print("\n Average of fitness values: ")
        print(self.averageOfFvals)

        # print("\n Selected Mates: ")
        # n = len(self.mates)
        # for i in range(n):
        #     print("no. ", self.matesNo[i])
        #     print(self.mates[i][0].printDesignVector())
        #     print(self.mates[i][1].printDesignVector())


