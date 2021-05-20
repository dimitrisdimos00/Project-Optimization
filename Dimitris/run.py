import numpy as np
from DesignVariable import designVec
from Population import population
from Operations import operations



pop1 = population(100, -10, 10, -10, 10, 0.0001)
op = operations(pop1)
print("---------------------POPULATION 1: ---------------------")
op.print()

for i in range(1000):
    new_pop = op.calculateNewPopulation(op.mates, 0.05, 0.95)
    op = operations(new_pop)
    txt = "---------------------POPULATION {pop_no:d}: ---------------------".format(pop_no = i + 2)
    print(txt)
    op.print()


