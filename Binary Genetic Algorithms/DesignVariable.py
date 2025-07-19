import numpy as np
import random

class designVec:
    def __init__(self, min, max, dx):
        self.q = int(np.ceil( np.log2( (max - min) / dx + 1 ) ))
        self.value_bin = self.generateBinary(self.q, min, max)
        self.value_dec = self.convertToDecimal(self.q, min, max, self.value_bin)
        self.min_value = min
        self.max_value = max
        self.dx = dx

    def setValue(self, bin_value, min, max, dx):
        self.q = int(np.ceil( np.log2( (max - min) / dx + 1 ) ))
        self.value_bin = bin_value
        self.value_dec = self.convertToDecimal(self.q, min, max, self.value_bin)
        self.min_value = min
        self.max_value = max
        self.dx = dx
    
    def generateBinary(self, q, min, max):
        
        bin_array = np.zeros(q, dtype='int') 

        for i in range(0, q):
            bin_array[i] = random.randint(0, 1)

        dec = self.convertToDecimal(q, min, max, bin_array)

        return bin_array


    def convertToDecimal(self, q, min, max, value_bin):
    
        sum = 0
        i = 0
        for k in range(q - 1, -1, -1):
            sum += 2 ** i * value_bin[k]
            i += 1
        x = min + (max - min) / (2 ** q - 1) * sum
        
        return x


    def printDesignVector(self):
        print("decimal value: ", self.value_dec)
        print("binary value: ", self.value_bin)
            

