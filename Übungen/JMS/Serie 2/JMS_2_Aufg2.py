import sympy as sp

x, y, z = sp.symbols("x y z")


def aufgabe1():
    f1 = 5 * x * y
    f2 = x**2 * y**2 + x + 2 * y

    A = sp.Matrix([f1, f2])
    Df = A.jacobian([x, y])
    print(Df)
    Df0 = Df.subs([(x, 1), (y, 2)])
    print(Df0)


def aufgabe2():
    f1 = sp.ln(x**2 + y**2) + z**2
    f2 = sp.exp(y**2 + z**2) + x**2
    f3 = (1/(z**2 + x**2)) + y**2

    A = sp.Matrix([f1, f2, f3])
    Df = A.jacobian([x, y, z])

    Df0 = Df.subs([(x, 1), (y, 2), (z, 3)])
    print(Df0)


aufgabe1()
aufgabe2()
