import numpy as np
from DesignVariable import designVec
from Population import population
from Operations import operations

# pop = population(10, 10, -50, 50)
# pop.initializePopulation()
# sim = operations(pop)

# sim.print()

# dv = designVec(0.1, 6, 10)

# # for i in range(1):
#     # print(dv.value_bin)
# print(dv.q)
# dv.printDesignVector()

pop = population(10, -5, 10, 0.1)
op = operations(pop)
op.print()

# dv = designVec(-5, 10, 0.1)
# print(dv.value_dec)