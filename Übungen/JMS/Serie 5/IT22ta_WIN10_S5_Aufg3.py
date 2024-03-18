import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

x = np.array([1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010])
y = np.array([75.995, 91.972, 105.711, 123.203, 131.669, 150.697, 179.323, 203.212, 226.505, 249.633, 281.422, 308.745])

##############################

def taskB():
    cs = CubicSpline(x,y)
    y_new = cs(x)

    plt.figure(figsize=(8, 4))
    plt.plot(x, y, 'o', label='Datenpunkte')
    plt.plot(x, y_new, '-', label='Kubische Spline-Interpolation')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Kubische Spline-Interpolation')
    plt.show()

taskB()

######################
def taskB():
    print("")