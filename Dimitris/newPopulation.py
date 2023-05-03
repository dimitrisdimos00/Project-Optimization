import numpy as np

class population:
    def __init__(self, size, central_point, radius):
    #, dx):
        self.size = size
        self.x_array = [None] * size
        self.y_array = [None] * size
        #self.dx = dx
        current_size = 0
        x_min = central_point[0] - radius
        x_max = central_point[0] + radius
        y_min = central_point[1] - radius
        y_max = central_point[1] + radius
        while (current_size <= size):
            x = np.random.randint(x_min, x_max)
            y = np.random.randint(y_min, y_max)
            distance = np.sqrt((central_point[0] - x)**2 + (central_point[1] - y)**2)
            if (distance <= radius):
                self.x_array[current_size] = x
                self.y_array[current_size] = y
                current_size +=1

    def setPopulation(self, x_array, y_array):
        self.x_array = x_array
        self.y_array = y_array
        self.size = len(x_array)

    def print(self):
        for i in range(0, self.size):
            print("\n")
            print("no.", i + 1)
            print("x:", self.x_array[i])
            print("y:", self.y_array[i])