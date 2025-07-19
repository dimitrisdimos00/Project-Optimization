from DesignVariable import designVec
import numpy as np
import random

# a class that stores a population of 2d design vectors and the population size
class population:
    def __init__(self, population_size, min_value_d1, max_value_d1, min_value_d2, max_value_d2, dx):
        all_des_vec = [None] * population_size # creating empty list
 
        self.max_value_d1 = max_value_d1
        self.min_value_d1 = min_value_d1
        self.max_value_d2 = max_value_d2
        self.min_value_d2 = min_value_d2

        self.dx = dx

        for i in range(population_size):
            dv1 = designVec(min_value_d1, max_value_d1, dx)
            dv2 = designVec(min_value_d2, max_value_d2, dx)
            vector2d = (dv1, dv2)
            all_des_vec[i] = vector2d
        self.all_design_vectors = all_des_vec
        self.pop_size = population_size

    def setAllDesignVectors(self, dvlist):
        self.all_design_vectors = dvlist
        self.pop_size = len(dvlist)


    def printPopulation(self):
        counter = 1
        for vector2d in self.all_design_vectors:
            print("\n")
            print("no.", counter)
            # dv.printDesignVector()
            counter += 1
            print("x:")
            vector2d[0].printDesignVector()
            print("y:")
            vector2d[1].printDesignVector()