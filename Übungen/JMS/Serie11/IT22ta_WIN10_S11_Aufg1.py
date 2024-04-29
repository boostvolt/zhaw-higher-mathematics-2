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


IT22ta_WIN10_S11_Aufg1(f, xmin, xmax, ymin, ymax, hx, hy)

f = lambda x, y: x**2 / y
a = 0
b = 1.4
n = 2
y0 = 2


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

    t = np.zeros(n + 1)
    t[0] = a
    y_mittelpunkt = np.zeros(n + 1)
    y_mittelpunkt[0] = y0
    x_half = np.zeros(n + 1)
    y_half = np.zeros(n + 1)

    for i in range(0, n):
        x_half[i] = t[i] + (h / 2)
        y_half[i] = y_mittelpunkt[i] + (h / 2) * f(t[i], y_mittelpunkt[i])
        t[i + 1] = t[i] + h
        y_mittelpunkt[i + 1] = y_mittelpunkt[i] + h * f(x_half[i], y_half[i])

    print("Mittelpunkt")
    print(
        np.column_stack(
            (t, y_mittelpunkt, x_half, y_half, np.abs(y_exakt - y_mittelpunkt))
        )
    )

    t = np.zeros(n + 1)
    t[0] = a
    y_modeuler = np.zeros(n + 1)
    y_modeuler[0] = y0
    y_e = np.zeros(n + 1)

    for i in range(0, n):
        t[i + 1] = t[i] + h
        y_e[i + 1] = y_modeuler[i] + h * f(t[i], y_modeuler[i])
        k1 = f(t[i], y_modeuler[i])
        k2 = f(t[i + 1], y_e[i + 1])
        t[i + 1] = t[i] + h
        y_modeuler[i + 1] = y_modeuler[i] + h * ((k1 + k2) / 2)

    print("Modifiziert")
    print(np.column_stack((t, y_modeuler, np.abs(y_exakt - y_modeuler))))

    return [t, y_euler, y_mittelpunkt, y_modeuler]


[x, y_euler, y_mittelpunkt, y_modeuler] = IT22ta_WIN10_S11_Aufg3(f, a, b, n, y0)

IT22ta_WIN10_S11_Aufg1(f, -2, 2, -0.5, 3, 0.25, 0.25)

plt.plot(x, y_euler)
plt.plot(x, y_mittelpunkt, linestyle="--")
plt.plot(x, y_modeuler, linestyle="dotted")
plt.show()

# print("result")
# print(x, y_euler, y_mittelpunkt)
