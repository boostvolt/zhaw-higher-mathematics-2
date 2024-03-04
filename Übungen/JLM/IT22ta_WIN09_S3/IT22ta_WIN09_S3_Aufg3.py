# import sympy as sp

# x, y, z = sp.symbols("x y z")
# f1 = x + y**2 - z**2 -13
# f2 = sp.ln(y/4) + sp.exp(0.5*z -1) - 1
# f3 = (y - 3)**2 - z**3 + 7

# # ------------------------------------------------------------------------------------------------------------------------

# x0 = sp.Matrix([1.5, 3, 2.5])
# epsilon = 1e-5
# f = sp.Matrix([f1,f2,f3])
# Df = f.jacobian([x,y,z])

# # Newton-Raphson-Verfahren

# f0 = f.subs([(x,x0[0]),(y,x0[1]),(z,x0[2])])
# while(f0.norm(2) > epsilon):
#     Df0 = Df.subs([(x,x0[0]),(y,x0[1]),(z,x0[2])])
#     delta = Df0.LUsolve(-f0)
#     x0 = x0 + delta
#     f0 = f.subs([(x,x0[0]),(y,x0[1]),z,x0[2]])
# print(f"x0: {x0.evalf()}")

import numpy as np


def nonlinear_system(x):
    f1 = x[0] + x[1] ** 2 - x[2] ** 3 - 13
    f2 = np.log(x[1] / 4) + np.exp(0.5 * x[2] - 1) - 1
    f3 = (x[1] - 3) ** 2 - x[2] ** 3 + 7
    return np.array([f1, f2, f3])


def damped_newton_method(x0, tolerance=1e-5):
    x = x0
    iteration = 0
    max_iterations = 1000

    while (
        np.linalg.norm(nonlinear_system(x)) > tolerance and iteration < max_iterations
    ):
        jacobian_matrix = np.array(
            [
                [1, 1, -3 * x[1] ** 2],
                [0, 1 / (4 * x[1]), 0.5 * np.exp(0.5 * x[2] - 1)],
                [0, 2 * (x[1] - 3), -3 * x[2] ** 2],
            ]
        )
        step = np.linalg.solve(jacobian_matrix, -nonlinear_system(x))

        # Damping factor to ensure convergence
        damping_factor = 0.5
        step_size = 1.0
        while np.linalg.norm(nonlinear_system(x + step_size * step)) >= np.linalg.norm(
            nonlinear_system(x)
        ):
            step_size *= damping_factor

        x = x + step_size * step
        iteration += 1

        print(
            f"Iteration {iteration}: ||f(x)|| = {np.linalg.norm(nonlinear_system(x))}, Step Size: {step_size}"
        )

    if iteration == max_iterations:
        print("Maximum iterations reached. Consider adjusting parameters.")

    return x


# Startvektor
x0 = np.array([1.5, 3, 2.5])

# Lösung mit dem gedämpften Newton-Verfahren
solution = damped_newton_method(x0)

print("Lösung:", solution)
print("Funktionswerte:", nonlinear_system(solution))


# zweite Variante
import sympy as sp

x1, x2, x3 = sp.symbols("x1 x2 x3")
f1 = x1 + x2**2 - x3**2 -13
f2 = sp.log(x2/4) + sp.exp(0.5*x3-1) - 1
f3 = (x2 -3)**2 - x3**3 + 7

f = sp.Matrix([f1, f2, f3])
Df = f.jacobian([x1, x2, x3])

x_0 = sp.Matrix([1.5,3,2.5])
print(f)
print(Df)

k = 0

# Nach 3 Durchläufen irgend in einem endlos State
while((f.subs([(x1, x_0[0]), (x2, x_0[1]), (x3, x_0[2])])).norm(2) > 10**(-5)):
    delta = Df.inv().subs([(x1, x_0[0]), (x2, x_0[1]), (x3, x_0[2])]) @ -(f.subs([(x1, x_0[0]), (x2, x_0[1]), (x3, x_0[2])]))
    x_0 = x_0 + (delta / 2**k)
    k += 1 # keine Ahnung, was die korrekte Definition von k ist
    print(k)
    print(x_0.evalf())

# Wird nicht erreicht
print("done")