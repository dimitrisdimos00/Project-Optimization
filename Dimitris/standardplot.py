from mpl_toolkits import mplot3d


import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return -20 * np.exp( -0.2 * np.sqrt( 0.5 * (xline ** 2 + yline ** 2))) - np.exp( 0.5 * (np.cos(2 * np.pi * xline) + np.cos(2 * np.pi * yline)) + np.exp(1) + 20
    
# x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
# plt.plot(x, np.sin(x))       # Plot the sine of each x point
# plt.show()                   # Display the plot


xline = np.linspace(0, 5, 100)
yline = np.linspace(0, 5, 100)
X, Y = np.meshgrid(xline, yline)
Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')