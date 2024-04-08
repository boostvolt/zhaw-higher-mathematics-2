import numpy as np

x = np.array(
    [
        0,
        800000,
        1200000,
        1400000,
        2000000,
        3000000,
        3400000,
        3600000,
        4000000,
        5000000,
        5500000,
        6370000,
    ]
)
ro = np.array(
    [13000, 12900, 12700, 12000, 11650, 10600, 9900, 5500, 5300, 4750, 4500, 3300]
)


def IT22ta_WIN09_S8_Aufg3a(x, y):
    Tf_neq = 0
    for i in range(len(x) - 1):
        Tf_neq += ((y[i] + y[i + 1]) / 2) * (x[i + 1] - x[i])
    return Tf_neq


y = ro * 4 * np.pi * (x**2)
m_ref = 5.976 * 10**24
m = IT22ta_WIN09_S8_Aufg3a(x, y)
print(m)
abs_error = np.abs(m - m_ref)
print(abs_error)
rel_error = abs_error / m_ref
print(rel_error)
