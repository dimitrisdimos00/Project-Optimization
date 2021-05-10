import numpy as np
import random

class designVec:
    def __init__(self, minValue, maxValue, dx):
        self.min = minValue
        self.max = maxValue
        
        self.q = int(np.ceil( np.log2( (maxValue - minValue) / dx + 1 ) ))

        # self.case = self.findCase(self.min, self.max)
        self.value_bin = self.generateBinary(self.q, self.min, self.max)
        self.value_dec = self.convertToDecimal(self.q, self.min, self.max, self.value_bin)
        

    def findCase(self, min, max):
        case = 1
        if min < 0 and max > 0:
            if max > abs(min):
                case = 1 
            elif max < abs(min):
                case = 2 
            else:
                # equal
                case = 3 
        elif min < 0 and max <= 0:
            # case = 4 => both min and max are negative
            case = 4 
        else:
            # case = 5 => both min and max are positive
            case = 5 
        return case


    def generateBinary(self, q, min, max):
        
        bin_array = np.zeros(q, dtype='int') 

        for i in range(0, q):
            bin_array[i] = random.randint(0, 1)

        dec = self.convertToDecimal(q, min, max, bin_array)

        # compute the sign according to the case of min and max parameters
        # sign = 0 # plus
        # if case == 1:
        #     if dec <= abs(min):
        #         sign = random.randint(0, 1)
        #     else:
        #         sign = 0
        # elif case == 2:
        #     if dec <= abs(max):
        #         sign = random.randint(0, 1)
        #     else:
        #         sign = 1
        # elif case == 3:
        #     sign = random.randint(0, 1)
        # elif case == 4:
        #     sign = 1
        # else:
        #     sign = 0
        
        # bin_array[0] = sign

        return bin_array

    # ignores the first bit(sign)
    def convertToDecimal(self, q, min, max, value_bin):
        
        sum = 0
        i = 0
        for k in range(q - 1, -1, -1):
            sum += 2 ** i * value_bin[k]
            i += 1
        x = min + (max - min) / (2 ** q - 1) * sum
        
        # sign = value_bin[0]
        # if sign == 1:
        #     x = x * (-1)
        
        return x

    def calculateCrossover(self, dv1, dv2):
        q = dv1.q
        site = random.randint(0, q - 1)



    def printDesignVector(self):
        print("decimal value: ", self.value_dec)
            

