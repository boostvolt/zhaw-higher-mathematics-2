import matplotlib.pyplot as plt
import numpy as np


def IT22ta_WIN10_S11_Aufg3(f, a, b, n, y0):
    h = (b - a) / n
    t = np.zeros(n + 1)
    y_euler = np.zeros(n + 1)
    t[0] = a
    y_euler[0] = y0
    y_exakt = np.zeros(n + 1)

    fy = lambda x: np.sqrt(((2 * x**3) / 3) + 4)

    for i in range(0, n + 1):
        t[i] = a + i * h
        y_exakt[i] = fy(t[i])

    t = np.zeros(n + 1)
    t[0] = a

    for i in range(0, n):
        t[i + 1] = t[i] + h
        y_euler[i + 1] = y_euler[i] + h * f(t[i], y_euler[i])
    print("Euler")
    print(np.column_stack((t, y_euler, np.abs(y_exakt - y_euler))))
    return [t, y_euler]


f = lambda x, y: 0.1 * y + np.sin(2 * x)
a = 0
b = 6
n = 30
y0 = 0

[x, y_euler] = IT22ta_WIN10_S11_Aufg3(f, a, b, n, y0)


plt.plot(x, y_euler)
plt.show()
