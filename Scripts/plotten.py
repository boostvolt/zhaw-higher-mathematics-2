import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


# Funktionsdefinition:
def p(x):
    return 0.54055556 * x ** 4 - 0.03203704 * x ** 3 - 0.10069444 * x ** 2 + 0.03231481 * x - 0.00291667


coeff = np.array([-0.00291667, 0.03231481, -0.10069444, -0.03203704, 0.54055556])


def f(x):
    return 1 / (1.82083754 + 0.42108857 * x ** 2)


# Wertebereich definieren:
x = np.array([0, 1, 2, 3, 4, 5], dtype=np.float64)
y = np.array([0.54, 0.44, 0.28, 0.18, 0.12, 0.08], dtype=np.float64)

plt.scatter(x, y)
plt.grid()
plt.plot(x, np.polyval(coeff, x), zorder=0, label='a')
plt.plot(x, f(x), label='b')
plt.scatter(x, y, marker='x', color='r', zorder=1, label='measured')
plt.legend()
plt.show()
