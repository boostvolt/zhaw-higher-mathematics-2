import matplotlib.pyplot as plt
import numpy as np

'''INPUT'''
# Zu lösende Differentialgleichung
a = 0
b = 190

# h = ((b - a) * 1.0) / n
h = 0.1
n = int((b - a) / h)
y0 = np.array([0., 0.])


def f(t, y):
    # hier muss die matrix aufgebaut werden wie sie auf eine dgl 1 umgestellt wurde.
    # y[1] = z2
    # [ h', dgl ]
    return np.array([y[1], (100 - 80 * y[0] - (1 / (4 * 10 ** -4)) * y[1])])


'''INPUT'''


def richtungsfeld(f, xmin, xmax, ymin, ymax, hx, hy):
    x = np.arange(xmin, xmax + hx, hx)
    y = np.arange(ymin, ymax + hy, hy)
    x, y = np.meshgrid(x, y)

    vx = np.ones_like(x)
    vy = f(x, y)
    v = np.sqrt(vx ** 2 + vy ** 2)
    vx = vx / v
    vy = vy / v
    plt.grid()
    plt.quiver(x, y, vx, vy, width=0.003, angles='xy')


def euler(f, x, h, y0):
    y = np.zeros((y0.size, n + 1))
    y[:, 0] = y0

    for k in range(x.shape[0] - 1):
        k1 = f(x[k], y[:, k])
        y[:, k + 1] = y[:, k] + h * k1

    return y


def mittelpunkt(f, x, h, y0):
    y = np.zeros((y0.size, n + 1))
    y[:, 0] = y0

    for k in range(x.shape[0] - 1):
        k1 = f(x[k], y[:, k])
        k2 = f(x[k] + h * 0.5, y[:, k] + 0.5 * h * k1)
        y[:, k + 1] = y[:, k] + h * k2

    return y


def mod_euler(f, x, h, y0):
    y = np.zeros((y0.size, n + 1))
    y[:, 0] = y0

    for k in range(x.shape[0] - 1):
        k1 = f(x[k], y[:, k])
        k2 = f(x[k] + h, y[:, k] + h * k1)
        y[:, k + 1] = y[:, k] + h * (k1 + k2) * 0.5

    return y


x = np.arange(a, b + h, step=h, dtype=np.float64)

# y_euler = euler(f, x, h, y0)
# y_modeuler = mod_euler(f, x, h, y0)
y_mittelpunkt = mittelpunkt(f, x, h, y0)

# Graphen zeichnen
# plt.plot(x, y_euler, label='Euler')
# plt.plot(x, y_modeuler, label='Modifiziertes Euler')
plt.plot(x, y_mittelpunkt, label='Mittelpunkt')
plt.legend()

# Richtungsfeld zeichnen
# hx = (b - a) / n
# hy = hx
# richtungsfeld(f, a, b, 1.5, 2.5, hx, hy)

plt.show()
