import numpy as np
from DesignVariable import designVec
from Population import population
from Operations import operations



op = operations(7, -5, 10, 0.01)
print("---------------------POPULATION 1: ---------------------")
op.print()

for i in range(5):
    new_pop = op.calculateNewPopulation(op.mates, 0.2)
    op.setOperations(new_pop)
    txt = "---------------------POPULATION {pop_no:d}: ---------------------".format(pop_no = i + 2)
    print(txt)
    op.print()
# op.setOperations(new_pop)
# op.print()

