import numpy as np
import matplotlib.pyplot as plt

'''INPUT'''
a = 0
b = 190

n = 10
# h = ((b - a) * 1.0) / n
h = 0.1
y0 = 0

# konstante
ma = 300_000
me = 80_000
q = (ma - me) / 190


def f(t, y):
    return 2600 * q / (ma - q * t) - 9.81 - (np.exp(-y / 8000) / (ma - q * t)) * (y ** 2)


'''INPUT'''


def interpolate_runge_kutta(f, x, h, y0):
    y = np.full(x.shape[0], 0, dtype=np.float64)
    y[0] = y0

    for i in range(x.shape[0] - 1):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + (h / 2.0), y[i] + (h / 2.0) * k1)
        k3 = f(x[i] + (h / 2.0), y[i] + (h / 2.0) * k2)
        k4 = f(x[i] + h, y[i] + h * k3)

        y[i + 1] = y[i] + h * (1 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

    return y


x = np.arange(a, b + h, step=h, dtype=np.float64)

y = interpolate_runge_kutta(f, x, h, y0)

print('x = ' + str(x))
print('y = ' + str(y))

plt.figure(0)
# plt.title('Runge-Kutta vs Runge-Kutta-custom vs Exact')
plt.plot(x, y, label='h\'\'')
# plt.plot(x, y_c, label='Runge-Kutta custom')
# plt.plot(x, y_exact(x), label='Exact')
plt.legend()
plt.grid()
plt.show()

# plt.figure(1)
# plt.plot(x, y*x, label='h\'')
# plt.legend()
# plt.grid()
# plt.show()
# plt.figure(2)
# plt.plot(x, y, label='h')
# plt.legend()
# plt.grid()
# plt.show()