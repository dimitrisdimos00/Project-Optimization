from DesignVariable import designVec
import numpy as np
import random

class population:
    def __init__(self, population_size, minValue, maxValue, dx):
       
        self.minValue = minValue
        self.maxValue = maxValue

        self.pop_size = population_size
        self.all_design_vectors = []
        for i in range(population_size):
            dv1 = designVec(minValue, maxValue, dx)       
            # dv2 = designVec(self.str_length, dec_value)
            # vector2d = (dv1, dv2)
            self.all_design_vectors.append(dv1)
    
    def getPopulationSize(self):
        return self.pop_size
    def getAllDesignVectors(self):
        return self.all_design_vectors


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

