import sympy as sp

x_0 = sp.Matrix([1.1, 0.9])

d1, d2 = sp.symbols("d1 d2")
x1, x2 = sp.symbols("x1 x2")

Df = sp.Matrix([[-18, -4*x2],[-4*x2, -4*x1 + 12*x2 ** 2]])
f = sp.Matrix([20 - 18 * x1 - 2 * x2 ** 2,-4 * x2 * (x1 - x2 ** 2)])


# Iteration 1
print("Iteration 1")
Df0 = Df.subs([(x1, x_0[0]), (x2, x_0[1])])
f0 = f.subs([(x1, x_0[0]), (x2, x_0[1])])
print(f"Df0: {Df0}")
print(f"f0: {f0}")


# Calculate our delta (x1, x2)
solutions = sp.solve(Df0 @ sp.Matrix([d1, d2]) + f0, [d1, d2])
delta1= solutions[d1]
delta2= solutions[d2]
print(f"Delta1: {delta1:.3f} and Delta2: {delta2:.3f}")

# Calculate our x1
d0 = sp.Matrix([delta1, delta2])
x_1 = x_0 + d0
print(f"x_1: {x_1}")

# Define the function f(x1)
fx1 = f.subs([(x1, x_1[0]), (x2, x_1[1])])
print(f"fx1: {fx1}")

# Calculate the 2 norm of f(x1)
norm_fx1 = sp.sqrt(sum(comp**2 for comp in fx1))
print(f"norm_fx1: {norm_fx1:.3f}")

# Calculate the 2 norm of x1 - x0
norm_x1_x0 = sp.sqrt(sum(comp**2 for comp in (x_1 - x_0)))
print(f"norm_x1_x0: {norm_x1_x0:.3f}")

# Iteration 2
print("\nIteration 2")
Df1 = Df.subs([(x1, x_1[0]), (x2, x_1[1])])
f1 = f.subs([(x1, x_1[0]), (x2, x_1[1])])
print(f"Df1: {Df1}")
print(f"f1: {f1}")


solutions = sp.solve(Df1 @ sp.Matrix([d1, d2]) + f1, [d1, d2])
delta1= solutions[d1]
delta2= solutions[d2]
print(f"Delta1: {delta1:.3f} and Delta2: {delta2:.3f}")

d1 = sp.Matrix([delta1, delta2])
x_2 = x_1 + d1
print(f"x_2: {x_2}")

# Define the function f(x2)
fx2 = f.subs([(x1, x_2[0]), (x2, x_2[1])])
print(f"fx2: {fx2}")

# Calculate the 2 norm of f(x2)
norm_fx2 = sp.sqrt(sum(comp**2 for comp in fx2))
print(f"norm_fx2: {norm_fx2:.3f}")

# Calculate the 2 norm of x2 - x1
norm_x2_x1 = sp.sqrt(sum(comp**2 for comp in (x_2 - x_1)))
print(f"norm_x2_x1: {norm_x2_x1:.3f}")