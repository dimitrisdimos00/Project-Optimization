import numpy as np
import random
import matplotlib.pyplot as plt

cp = (5,5)
r = 25
size = 1000
curr_size = 0
x_array = [None] * size
y_array = [None] * size
while(size > curr_size):
    x = np.random.randint(cp[0] - r, cp[0] + r)
    y = np.random.randint(cp[1] - r, cp[1] + r)
    d = np.sqrt((cp[0] - x)**2 + (cp[1] - y)**2)
    if(d<=r):
        x_array[curr_size] = x
        y_array[curr_size] = y
        curr_size +=1

plt.scatter(x_array, y_array)
plt.show()