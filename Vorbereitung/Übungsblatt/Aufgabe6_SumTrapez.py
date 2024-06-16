import numpy as np
import scipy.integrate

"""INPUT"""
f = lambda x: 2 * np.exp(-(((x / 10) - 2) ** 4))  # funktion
a, b = 0.0, 40  #

n = 4  # interation schritte für höhe
# oder Schrittweite: setze eins von beiden und andere auf 0
h = 0  # 0.0618
err = 1e-3
"""INPUT"""


def sum_trapez(f, a, b, n, h):
    x = np.linspace(a, b, n + 1)
    # h = (b - a) / n
    tf = h * ((f(a) + f(b)) * 0.5 + np.sum(f(x[1:-1])))
    tmp = ""
    for x_in in x[1:-1]:
        tmp = "%s+ f(%s)" % (tmp, x_in)

    print(f" tf = {h} * (f({a}) + f({b})) * 0.5", tmp)
    return tf


if n <= 0:
    n = np.ceil((b - a) / h).astype("int")

if h == 0:
    h = (b - a) / n

tf = sum_trapez(f, a, b, n, h)

exact = scipy.integrate.quad(f, a, b)[0]

print("exakte lösung: ", exact)
print(
    "sum Trapez:", tf, "  error: ", abs(tf - exact), "erfüllt: ", abs(tf - exact) < err
)
