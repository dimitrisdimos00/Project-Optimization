from warnings import simplefilter
import numpy as np
import random
from DesignVariable import designVec
from Population import population

# rastrigin search domain: -5.12 <= x, y <= 5.12
def rastrigin(x, y):
    return 20 + x**2 - 10*np.cos(2*np.pi*x) + y**2 - 10*np.cos(2*np.pi*y)
# ackley search domain: -5 <= x, y <= 5
def ackley(x, y):
    return -20 * np.exp( -0.2 * np.sqrt( 0.5 * (x ** 2 + y ** 2))) - np.exp( 0.5 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))) + np.exp(1) + 20
# sphere search domain: -inf <= xi <= +inf
def sphere(x, y):
    return x**2 + y**2
    
# a class that performs all the necessary operations for the genetic algorithm
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

        self.fitness_values = self.evaluate(self.designVectors)
        self.sum_of_fvalues = sum(self.fitness_values)
        self.averageOfFvals = self.sum_of_fvalues * (1 / self.n)

        self.probabilities_of_selection = self.findProbabilitiesOfSelection(self.fitness_values, self.sum_of_fvalues)
        self.cummulative_probabilities = self.findCummulativeProbabilities(self.probabilities_of_selection)

        self.mates, self.matesNo = self.findMates(self.designVectors, self.cummulative_probabilities)


    def evaluate(self, vectors):
        eval_value = []
        for vector2d in vectors:
            # find the fitness value F(x) = 1 / (1 + f(x))
            fitness_value = 1 / (1 + ackley(vector2d[0].value_dec, vector2d[1].value_dec)) 
            eval_value.append(fitness_value)
        return eval_value
    
    def findProbabilitiesOfSelection(self, fitness_values, sum):
        pos = []
        for fv in fitness_values:
            p = fv / sum
            pos.append(p)
        return pos

    def findCummulativeProbabilities(self, probabilities):
        cumProb = []
        current_sum = probabilities[0]
        cumProb.append(current_sum)

        length = len(probabilities)
        for i in range(1, length):
            current_sum += probabilities[i]
            cumProb.append(current_sum)
            
        return cumProb
        
    def findMates(self, designVectors, cumProb):
        n = len(designVectors)
        selectedMates = [None] * n
        selectedMatesIndex = [None] * n

        for j in range(n):
            r = random.uniform(0,1)
            selectedIndex = 0
            # find the index of the element to be selected with roulette method
            for i in range(1, n):
                if r > cumProb[i - 1] and r <= cumProb[i]:
                    selectedIndex = i
            
            selectedMates[j] = designVectors[selectedIndex]
            selectedMatesIndex[j] = selectedIndex

        return selectedMates, selectedMatesIndex

    # calculate the mutation on the given binary string with probability of mutation pm
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
    
    # caclulate the crossover in the given binary strings
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

    # in this function the new population is calculated given the 
    # probability of mutation pm and the probability of crossover pc
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
            # if the probability of crossover is achieved, select parent1 and parent2
            # and save them as well as their positions    
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
                
            # below is a series of concatenations and splits for the crossover to 
            # be calculated, given that the two parents are found
            if parent1_found and parent2_found:
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
                
                # set the booleans back to false
                parent1_found = False
                parent2_found = False
        
        # calculate the mutation for each vector
        for k in range(len(new_design_vectors)):
            vector2d = new_design_vectors[k]
            
            bin_value = np.concatenate((vector2d[0].value_bin, vector2d[1].value_bin), axis = None)
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

            # pass the new vactor to the list of the new design vectors
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

    def check_convergence(self, values, limit):

        #Checking the convergence of a list of values in comparison to a limit.

        """

        :param values: list of values, corresponding to fitness, variables of position ,or a characteristic   

        :param sd: standard deviation

        :return: boolean whether the criterion is met or not, criterion : stander var. <= a set limit

        """

        flag = False

        n = len(values)

        mean = sum(values) / n

        diff = [i - mean for i in values]

        diff_2 = [x ** 2 for x in diff]

        my_sum = sum(diff_2)

        variance = my_sum / n

        sd = np.sqrt(variance)

        if (sd <= limit):

            flag = True

        return flag

    def check_convergence_for_all(self, limit):
        # values is a list of 2d vectors
        values = self.designVectors
        l1 = []
        l2 = []
        for i in range(len(values)):
            l1.append(values[i][0].value_dec)
            l2.append(values[i][1].value_dec)
        if self.check_convergence(l1, limit) and self.check_convergence(l2, limit):
            return True
        return False
        