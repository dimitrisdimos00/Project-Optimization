import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import newPopulation

# rastrigin search domain: -5.12 <= x, y <= 5.12
def rastrigin(x, y):
    return 20 + x**2 - 10*np.cos(2*np.pi*x) + y**2 - 10*np.cos(2*np.pi*y)
# ackley search domain: -5 <= x, y <= 5
def ackley(x, y):
    return -20 * np.exp( -0.2 * np.sqrt( 0.5 * (x ** 2 + y ** 2))) - np.exp( 0.5 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))) + np.exp(1) + 20
# sphere search domain: -inf <= xi <= +inf
def sphere(x, y):
    return x**2 + y**2

cp = (0,0)
r = 4
size = 300
p = newPopulation.population(size, cp, r, rastrigin)
iterations = 0
while(not p.converges(0.005) and max(p.fitness_values) < 0.9999):
    p.print()
    p.recreate(0.95, 0.15)
    iterations+= 1
p.print()
print(iterations, "iterations")

# values = [None] * p.size
# x_array = [None] * p.size
# y_array = [None] * p.size

# for j in range(4):
#     for i in range(p.size):
#         x_array[i] = p.population[i][0]
#         y_array[i] = p.population[i][1]
#         values[i] = rastrigin(x_array[i], y_array[i])

# ax = plt.figure().add_subplot(projection='3d')
#     # ax.scatter(x_array, y_array, values)
# a = np.linspace(-5.12, 5.12, num=50)
# b = np.linspace(-5.12, 5.12, num=50)
# X, Y = np.meshgrid(a, b)
# Z = sphere(X, Y)
# ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1, color="red")
    # p.recreate(0.9)
# plt.show()