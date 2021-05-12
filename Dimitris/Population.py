from DesignVariable import designVec
import numpy as np
import random

# a class that stores a population of design vectors and the population size
class population:
    def __init__(self):
        pass

    def getAllDesignVectors(self):
        return self.all_design_vectors
    def getPopulationSize(self):
        return self.pop_size
    def setAllDesignVectors(self, dvlist):
        self.all_design_vectors = dvlist
        self.pop_size = len(dvlist)

    def initializePopulation(self, population_size, min_value, max_value, dx):
        all_des_vec = [None] * population_size
        for i in range(population_size):
            dv1 = designVec(min_value, max_value, dx)
            # dv2 = designVec(self.str_length, dec_value)
            # vector2d = (dv1, dv2)
            all_des_vec[i] = dv1
        self.all_design_vectors = all_des_vec
        self.pop_size = population_size

    def printPopulation(self):
        counter = 1
        for dv in self.all_design_vectors:
            print("\n")
            print("no.", counter)
            dv.printDesignVector()
            counter += 1
            # print("dv1:")
            # vector2d[0].printDesignVector()
            # print("dv2:")
            # vector2d[1].printDesignVector()

