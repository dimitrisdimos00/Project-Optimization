from Population import population
from Operations import operations

population_size = 100
x_min = -5
x_max = 5
y_min = -5
y_max = 5
Dx = 0.00001
max_iterations = 400
standard_deviation = 0.01
pc = 0.95
pm = 0.05



pop1 = population(population_size, x_min, x_max, y_min, y_max, Dx)
pop1.printPopulation()
op = operations(pop1)
print("---------------------POPULATION 1: ---------------------")
op.print()
i = 0
# check the standard deviation as a convergence criterion
convergence = op.check_convergence_for_all(standard_deviation)
while i < max_iterations and convergence == False:
    new_pop = op.calculateNewPopulation(op.mates, pm, pc)
    op = operations(new_pop)
    txt = "---------------------POPULATION {pop_no:d}: ---------------------".format(pop_no = i + 2)
    print(txt)
    op.print()
    i += 1
    convergence = op.check_convergence_for_all(standard_deviation)
new_pop.printPopulation()

