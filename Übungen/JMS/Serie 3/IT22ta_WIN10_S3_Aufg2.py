from sympy import Matrix, symbols, sympify, plot_implicit, Eq


x, y = symbols("x y")
f1 = x**2 / 186**2 - y**2 / (300**2 - 186**2) - 1
f2 = (y - 500) ** 2 / 279**2 - (x - 300) ** 2 / (500**2 - 279**2) - 1

p1 = plot_implicit(Eq(f1, 0), (x, -2000, 2000), (y, -2000, 2000), show=False)
p2 = plot_implicit(Eq(f2, 0), (x, -2000, 2000), (y, -2000, 2000), show=False)

p1.extend(p2)
p1.show()

########################################################################################


def newton_method(functions, initial_guess, tolerance, debug=False):
    functions = [sympify(f) for f in functions]  # Convert strings to SymPy expressions
    variables = symbols(" ".join(initial_guess.keys()))
    jacobian_matrix = Matrix(functions).jacobian(variables)
    current_guess = initial_guess.copy()

    while True:
        delta = -jacobian_matrix.inv().subs(current_guess) * Matrix(functions).subs(
            current_guess
        )

        for j, var in enumerate(variables):
            current_guess[str(var)] = (current_guess[str(var)] + delta[j]).evalf()

        f_norm = Matrix(functions).subs(current_guess).norm()

        if debug:
            print(f"x = {current_guess}, ||f(x)|| = {f_norm.evalf()}")

        if f_norm < tolerance:
            break

    return current_guess


# Define functions
functions = [
    "x**2/186**2 - y**2/(300**2 - 186**2) - 1",
    "(y - 500)**2/279**2 - (x - 300)**2/(500**2 - 279**2) - 1",
]

# Define initial guess
initial_guesses = [
    {"x": -200, "y": 50},
    {"x": 250, "y": 200},
    {"x": 750, "y": 900},
    {"x": -1250, "y": 1600},
]

for initial_guess in initial_guesses:
    print(newton_method(functions, initial_guess, 10**-5, True))
    print()
