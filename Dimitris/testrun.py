import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import newPopulation

def rastrigin(x, y):
    return 20 + x**2 - 10*np.cos(2*np.pi*x) + y**2 - 10*np.cos(2*np.pi*y)

cp = (0,0)
r = 4
size = 50
p = newPopulation.population(size, cp, r)

values = [None] * p.size
x_array = [None] * p.size
y_array = [None] * p.size

for i in range(p.size):
    x_array[i] = p.population[i][0]
    y_array[i] = p.population[i][1]
    values[i] = rastrigin(x_array[i], y_array[i])

ax = plt.figure().add_subplot(projection='3d')
ax.scatter(x_array, y_array, values)

# plt.scatter(p.x_array, p.y_array)
# plt.show()

# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')

# Grab some test data.
# X, Y, Z = axes3d.get_test_data(0.05)
a = np.linspace(-5.12, 5.12, num=50)
b = np.linspace(-5.12, 5.12, num=50)
X, Y = np.meshgrid(a, b)

# rastrigin
Z = 20 + X**2 - 10*np.cos(2*np.pi*X) + Y**2 - 10*np.cos(2*np.pi*Y)
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10, color="red")



p.recreate(rastrigin, 0.9)
for i in range(p.size):
    x_array[i] = p.population[i][0]
    y_array[i] = p.population[i][1]
    values[i] = rastrigin(x_array[i], y_array[i])

ax = plt.figure().add_subplot(projection='3d')
ax.scatter(x_array, y_array, values)

a = np.linspace(-5.12, 5.12, num=50)
b = np.linspace(-5.12, 5.12, num=50)
X, Y = np.meshgrid(a, b)
Z = 20 + X**2 - 10*np.cos(2*np.pi*X) + Y**2 - 10*np.cos(2*np.pi*Y)
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10, color="red")
plt.show()