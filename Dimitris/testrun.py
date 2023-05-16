import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import newPopulation

def rastrigin(x, y):
    return 20 + x**2 - 10*np.cos(2*np.pi*x) + y**2 - 10*np.cos(2*np.pi*y)
# sphere search domain: -inf <= xi <= +inf
def sphere(x, y):
    return x**2 + y**2
cp = (0,0)
r = 20
size = 50
p = newPopulation.population(size, cp, r, rastrigin)
for i in range(200):
    p.print()
    p.recreate(0.95)

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