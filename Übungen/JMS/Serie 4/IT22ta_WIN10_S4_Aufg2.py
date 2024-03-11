import numpy as np

def lagrange_int(x, y, x_int):
    n = x.size
    y_int = 0
    
    for i in range(n):
        L = 1

        for j in range(n):
            if i != j:
                L *= (x_int - x[j]) / (x[i] - x[j])

        y_int += (L * y[i])

    return y_int


x = np.array([0, 2500, 5000, 10000])
y = np.array([1013, 747, 540, 226])

print(lagrange_int(x, y, 3750))