from mpl_toolkits import mplot3d
from Operations import operations

import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return x**2

op = operations(20, -10, 10, 0.001)
dvs = op.designVectors
x = [None] * len(dvs)
y = [None] * len(dvs)
i = 0
txt = "G{no:d}".format(no = 1)
for dv in dvs:
    x[i] = dv.value_dec
    y[i] = f(x[i])
    
    plt.text(x[i], y[i], txt, size =  'x-small')
    i += 1
    

plt.scatter(x, y, s = 4)


for j in range(2, 6):
    new_pop = op.calculateNewPopulation(op.mates, 0.2)
    op.setOperations(new_pop)

    dvs = op.designVectors
    x = [None] * len(dvs)
    y = [None] * len(dvs)
    i = 0
    txt = "G{no:d}".format(no = j)
    for dv in dvs:
        x[i] = dv.value_dec
        y[i] = f(x[i])
        plt.text(x[i], y[i], txt, size =  'x-small')
        i += 1
    plt.scatter(x, y, s = 4)
plt.show()               

# def f(x, y):
#     return -20 * np.exp( -0.2 * np.sqrt( 0.5 * (xline ** 2 + yline ** 2))) - np.exp( 0.5 * (np.cos(2 * np.pi * xline) + np.cos(2 * np.pi * yline)) + np.exp(1) + 20
    
# xline = np.linspace(0, 5, 100)
# yline = np.linspace(0, 5, 100)
# X, Y = np.meshgrid(xline, yline)
# Z = f(X, Y)
# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.contour3D(X, Y, Z, 50, cmap='binary')