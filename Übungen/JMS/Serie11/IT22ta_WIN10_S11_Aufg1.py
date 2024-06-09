import matplotlib.pyplot as plt
import numpy as np

f = lambda t, y: t**2 + 0.1 * y
xmin = -2
xmax = 2
hx = 0.25
ymin = -3
ymax = 3
hy = 0.25


def IT22ta_WIN10_S11_Aufg1(f, xmin, xmax, ymin, ymax, hx, hy):
    [x, y] = np.meshgrid(np.arange(xmin, xmax, hx), np.arange(ymin, ymax, hy))
    plt.quiver(
        x, y, np.ones((int((xmax - xmin) / hx), int((ymax - ymin) / hy))), f(x, y)
    )


if __name__ == "__main__":
    IT22ta_WIN10_S11_Aufg1(f, xmin, xmax, ymin, ymax, hx, hy)
    plt.show()
