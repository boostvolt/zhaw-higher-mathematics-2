import numpy as np
import matplotlib.pyplot as plt

'''INPUT'''


def f(x, y):
    return x / y


def y_exact(x):
    return np.sqrt(x ** 2 - 3)


h = 3
y0 = 1
# anfangspunkt y(2) = 1, y(5) berechnen
x = np.arange(2, 5.1, step=h, dtype=np.float64)
'''INPUT'''


def interpolate_runge_kutta_custom(f, x, h, y0):
    a = np.array([
        [0, 0, 0],
        [1 / 3, 0, 0],
        [0, 2 / 3, 0]
        # ,[0.75, 0.5, 0.75, 0]
    ], dtype=np.float64)
    b = np.array([1 / 4, 0, 3 / 4], dtype=np.float64)
    c = np.array([0, 1 / 3, 2 / 3], dtype=np.float64)
    s = a.shape[0]
    y = np.full(x.shape[0], 0, dtype=np.float64)
    y[0] = y0

    for i in range(x.shape[0] - 1):
        k = np.full(s, 0, dtype=np.float64)

        for n in range(s):
            k[n] = f(x[i] + (c[n] * h),
                     y[i] + h * np.sum([a[n][m] * k[m] for m in range(n)]))

            tmp = ('0' if n == 0 else '')
            for m in range(n):
                tmp = '{} {} * {}'.format(tmp, a[n][m], k[m])

            print(f'k{n + 1} = f({x[i]} + {(c[n] * h)}, {y[i]} + {h}*{tmp}) = {k[n]}')
        y[i + 1] = y[i] + h * np.sum([b[n] * k[n] for n in range(s)])

    return y


y_c = interpolate_runge_kutta_custom(f, x, h, y0)
print(y_c)
plt.figure(0)
plt.title('Runge-Kutta vs Runge-Kutta-custom vs Exact')
plt.plot(x, y_c, label='Runge-Kutta custom')
plt.plot(x, y_exact(x), label='Exact')
plt.legend()
plt.show()
