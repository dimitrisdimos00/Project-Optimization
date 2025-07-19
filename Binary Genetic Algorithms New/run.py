import numpy
import matplotlib.pyplot as pyplot
import Population

# Rastrigin search domain: -5.12 <= x, y <= 5.12

def rastrigin(x, y):
    return 20 + x ** 2 - 10 * numpy.cos(2 * numpy.pi * x) + y ** 2 - 10 * numpy.cos(2 * numpy.pi * y)

# Ackley search domain: -5 <= x, y <= 5

def ackley(x, y):
    return -20 * numpy.exp( -0.2 * numpy.sqrt( 0.5 * (x ** 2 + y ** 2))) - numpy.exp( 0.5 * (numpy.cos(2 * numpy.pi * x) + numpy.cos(2 * numpy.pi * y))) + numpy.exp(1) + 20

# Sphere search domain: -inf <= xi <= +inf

def sphere(x, y):
    return x ** 2 + y ** 2

# --- Configuration ---

objective_function = rastrigin
function_name = "Rastrigin"
domain = (-5.12, 5.12)

# objective_function = ackley
# function_name = "Ackley"
# domain = (-5, 5)

# objective_function = sphere
# function_name = "Sphere"
# domain = (1, 1)

population = Population.Population(size=300, central_point=(0,0), 
    radius=300, function=objective_function)

iterations = 0
while(not population.converges(limit=0.005) 
    and max(population.fitness_values) < 0.9999):

    population.print_status()
    population.recreate(crossover_probability=0.95, mutation_probability=0.15)
    iterations += 1

population.print_status()
print(iterations, "iterations")

# Extract the final population's coordinates and their fitness values
x_coords = [ind[0] for ind in population.population]
y_coords = [ind[1] for ind in population.population]
z_coords = [objective_function(x, y) for x, y in population.population]

# Create the 3D plot
figure = pyplot.figure(figsize=(12, 8)).add_subplot(projection='3d')

# Plot the surface of the Rastrigin function
a = numpy.linspace(domain[0], domain[1], num=50)
b = numpy.linspace(domain[0], domain[1], num=50)

X, Y = numpy.meshgrid(a, b)
Z = objective_function(X, Y)

figure.plot_surface(X, Y, Z, rstride=5, cstride=5, 
    cmap='viridis', edgecolor='none', alpha=0.6)

# Plot the final population as a scatter plot on the surface
figure.scatter(x_coords, y_coords, z_coords, color='red', 
    s=20, depthshade=True, label='Final Population')

figure.set_title(f"Final Population on {function_name} Function Surface")

pyplot.show()

