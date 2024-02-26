import sympy as sp

x, y, z = sp.symbols("x y z")
f1 = 5*x*y
f2 = (x**2)*(y**2) + x + 2*y
def jacobi():
    f = sp.Matrix([f1, f2])
    X = sp.Matrix([x, y])
    Df = f.jacobian(X)
    Df0 = Df.subs([(x, 1), (y, 2)])
    print(Df0)

jacobi()


