import matplotlib.pyplot as plt
import numpy as np


def IT22ta_WIN10_S8_Aufg3a(x, y):
    res = 0
    for i in range(0, len(x) - 1):
        yi = y[i]
        yi_plus_1 = y[i + 1]
        xi_plus_1 = x[i + 1]
        xi = x[i]

        res = res + ((yi + yi_plus_1) / 2) * (xi_plus_1 - xi)

    return res


m_a = 300000
m_e = 80000
t_e = 190
v_rel = 2600
g = 9.81

u = (m_a - m_e) / t_e

a = lambda t: v_rel * (u / (m_a - u * t)) - g

delta_t = 0.1
t = np.arange(0, t_e + delta_t, delta_t)

v_int = np.zeros(t.size)
h_int = np.zeros(t.size)

for i in range(0, t.size):
    v_int[i] = IT22ta_WIN10_S8_Aufg3a(t[0 : i + 1], a(t[0 : i + 1]))
    h_int[i] = IT22ta_WIN10_S8_Aufg3a(t[0 : i + 1], v_int[0 : i + 1])

v = lambda t: v_rel * np.log(m_a / (m_a - u * t)) - g * t
h = (
    lambda t: (-v_rel * (m_a - u * t) / u) * np.log(m_a / (m_a - u * t))
    + v_rel * t
    - 0.5 * g * t**2
)

plt.plot(t, v_int)
plt.plot(t, v(t), linestyle="--")

plt.grid()
plt.show()

plt.plot(t, h_int)
plt.plot(t, h(t), linestyle="--")
plt.grid()
plt.show()
