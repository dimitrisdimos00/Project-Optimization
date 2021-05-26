import numpy as np
from DesignVariable import designVec
from Population import population
from Operations import operations


# creating a new population with size: 100, minValue: -10, maxValue:10 in x
# minValue: -10, maxValue:10 in y, and precision of 0.0001
pop1 = population(100, -100, 100, -100, 100, 0.0001)
# pop1.printPopulation()
op = operations(pop1)
print("---------------------POPULATION 1: ---------------------")
op.print()
i = 0
afv = op.averageOfFvals
max_iterations = 1000
while i < max_iterations and afv < 0.96:
    new_pop = op.calculateNewPopulation(op.mates, 0.05, 0.95)
    op = operations(new_pop)
    txt = "---------------------POPULATION {pop_no:d}: ---------------------".format(pop_no = i + 2)
    print(txt)
    op.print()
    i += 1
    afv = op.averageOfFvals
# new_pop.printPopulation()

