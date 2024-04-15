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

p = np.array(
    [13000, 12900, 12700, 12000, 11650, 10600, 9900, 5500, 5300, 4750, 4500, 3300]
)

y = p * 4 * np.pi * (x**2)


def IT22ta_WIN10_S8_Aufg3a(x, y):
    res = 0
    for i in range(0, len(x) - 1):
        yi = y[i]
        yi_plus_1 = y[i + 1]
        xi_plus_1 = x[i + 1]
        xi = x[i]

        res = res + ((yi + yi_plus_1) / 2) * (xi_plus_1 - xi)

    return res


tef_neq = IT22ta_WIN10_S8_Aufg3a(x, y)
referenz = 5.976 * 10**24

print("Erdmasse: ", tef_neq)
print("Absoluter Fehler: ", np.abs(referenz - tef_neq))
print("Realtiver Fehler: ", np.abs((referenz - tef_neq) / referenz))
