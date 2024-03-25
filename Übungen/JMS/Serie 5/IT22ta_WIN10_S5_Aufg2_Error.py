import numpy as np
from matplotlib import pyplot as plt

x = np.array([4, 6, 8, 10])
y = np.array([6, 3, 9, 0])
xx = np.arange(4, 10.1, 0.1)


def spline(x, y, xx):
    if x.size != y.size:
        return "x and y must have the same size"

    a = np.copy(y)
    h = np.zeros(x.size)
    h[:-1] = x[1:] - x[:-1]
    c = np.zeros_like(x)
    A = np.zeros((x.size - 2, x.size))
    A = np.diag(2 * (h[:-1] + h[1:])) + np.diag(h[1:-1], 1) + np.diag(h[1:-1], -1)
    z = np.zeros(x.size - 2)
    # print(y[2:].shape)
    # print(y[1:-1].shape)
    # print(h[1:-1].shape)
    # print(h)
    z[0:] = 3 * (((y[2:] - y[1:-1]) / h[1:-1]) - ((y[1:-1] - y[:-2]) / h[:-2]))
    print(A)
    print(A.shape)
    print(z.shape)
    c[1:-1] = np.linalg.solve(A, z)

    b = ((y[1:] - y[:-1]) / h) - (c[1:] + 2 * c[:-1]) * (h / 3)

    d = (c[1:] - c[:-1]) / (h * 3)

    yy = np.zeros(xx.shape)
    for i in range(x.size - 1):
        idx = np.nonzero((xx >= x[i]) & (xx <= x[i + 1]))
        for j in idx[0]:
            dx = xx[j] - x[i]
            yy[j] = a[i] + (b[i] * dx) + (c[i] * (dx**2)) + (d[i] * (dx**3))

    return yy


if __name__ == "__main__":
    yy = spline(x, y, xx)
    plt.scatter(x, y)
    plt.plot(xx, yy)
    plt.grid()
    plt.show()
