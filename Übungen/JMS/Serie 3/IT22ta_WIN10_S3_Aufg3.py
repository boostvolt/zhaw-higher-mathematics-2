import numpy as np
import sympy as sy


def newton_damped(f, x0, eps=10**-5):
    x, y, z = sy.symbols("x y z")

    Df = sy.lambdify([([x], [y], [z])], f.jacobian([x, y, z]))
    fl = sy.lambdify([([x], [y], [z])], f)
    x = [x0]
    k = 0

    while np.linalg.norm(fl(x[k]), 2) >= eps:
        d = np.linalg.solve(Df(x[k]), -fl(x[k]))
        i = 0

        while np.linalg.norm(fl(x[k] + d / (2**i)), 2) >= np.linalg.norm(fl(x[k]), 2):
            i += 1

        x.append(x[k] + d / (2**i))
        k += 1

    return x


x, y, z = sy.symbols("x y z")
f = sy.Matrix(
    [
        x + y**2 - z**2 - 13,
        sy.log(y / 4) + sy.exp(0.5 * z - 1) - 1,
        (y - 3) ** 2 - z**3 + 7,
    ]
)
x0 = np.array([[1.5], [3], [2.5]])

xn = newton_damped(f, x0)

for k, xi in enumerate(xn[1:], start=1):
    print(f"{k} x = {xi}")
