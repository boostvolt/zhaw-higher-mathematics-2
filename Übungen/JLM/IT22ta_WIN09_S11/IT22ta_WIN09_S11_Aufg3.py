import matplotlib.pyplot as plt
import numpy as np
from IT22ta_WIN09_S11_Aufg1 import richtungsfeld

f = lambda x, y: x**2 / y
a = 0
b = 1.4
n = 2
y0 = 2


def IT22ta_WIN10_S11_Aufg3(f, a, b, n, y0):
    h = (b - a) / n
    t = np.zeros(n + 1)
    y_euler = np.zeros(n + 1)
    y_mittelpunkt = np.zeros(n + 1)
    y_modeuler = np.zeros(n + 1)

    t[0] = a
    y_euler[0] = y0
    y_mittelpunkt[0] = y0
    y_modeuler[0] = y0

    for i in range(0, n):
        t[i + 1] = t[i] + h

        # Euler method
        y_euler[i + 1] = y_euler[i] + h * f(t[i], y_euler[i])

        # Midpoint method
        k1 = f(t[i], y_mittelpunkt[i])
        k2 = f(t[i] + h / 2, y_mittelpunkt[i] + (h / 2) * k1)
        y_mittelpunkt[i + 1] = y_mittelpunkt[i] + h * k2

        # Modified Euler method
        k1 = f(t[i], y_modeuler[i])
        k2 = f(t[i] + h, y_modeuler[i] + h * k1)
        y_modeuler[i + 1] = y_modeuler[i] + (h / 2) * (k1 + k2)

    return t, y_euler, y_mittelpunkt, y_modeuler


[x, y_euler, y_mittelpunkt, y_modeuler] = IT22ta_WIN10_S11_Aufg3(f, a, b, n, y0)
richtungsfeld(f, -2, 2, -0.5, 3, 0.25, 0.25)
plt.plot(x, y_euler, label="Euler")
plt.plot(x, y_mittelpunkt, linestyle="--", label="Midpoint")
plt.plot(x, y_modeuler, linestyle="dotted", label="Modified Euler")

plt.legend()
plt.show()
