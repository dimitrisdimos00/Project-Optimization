from Population import population
from Operations import operations


# creating a new population with size: 100, minValue: -10, maxValue:10 in x
# minValue: -10, maxValue:10 in y, and precision of 0.0001
pop1 = population(200, -100, 100, -100, 100, 0.00001)
pop1.printPopulation()
op = operations(pop1)
print("---------------------POPULATION 1: ---------------------")
op.print()
i = 0
# check the standard deviation as a convergence criterion
convergence = op.check_convergence_for_all(0.01)
max_iterations = 400
while i < max_iterations and convergence == False:
    new_pop = op.calculateNewPopulation(op.mates, 0.05, 0.95)
    op = operations(new_pop)
    txt = "---------------------POPULATION {pop_no:d}: ---------------------".format(pop_no = i + 2)
    print(txt)
    op.print()
    i += 1
    convergence = op.check_convergence_for_all(0.01)
new_pop.printPopulation()

