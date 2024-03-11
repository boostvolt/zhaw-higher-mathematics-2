from sympy import Matrix, symbols, sympify


def newton_method(functions, initial_guess, iterations, debug=False):
    functions = [sympify(f) for f in functions]  # Convert strings to SymPy expressions
    variables = symbols(" ".join(initial_guess.keys()))
    jacobian_matrix = Matrix(functions).jacobian(variables)
    current_guess = initial_guess.copy()

    for i in range(iterations):
        substitutions = [(var, current_guess[str(var)]) for var in variables]
        delta = -jacobian_matrix.inv().subs(substitutions) * Matrix(functions).subs(
            substitutions
        )

        previous_guess = current_guess.copy()
        current_guess = {
            str(var): current_guess[str(var)] + delta[j]
            for j, var in enumerate(variables)
        }

        f_norm = Matrix([f.subs(substitutions) for f in functions]).norm()
        x_norm = Matrix(
            [current_guess[str(var)] - previous_guess[str(var)] for var in variables]
        ).norm()

        if debug:
            print(
                f"Iteration {i+1}: x = {current_guess}, ||f(x^(k))|| = {f_norm}, ||x(k) - x(k-1)|| = {x_norm}"
            )

    return current_guess


# Define functions
functions = ["20 - 18 * x1 - 2 * x2**2", "-4 * x2 * (x1 - x2**2)"]

# Define initial guess
initial_guess = {"x1": 1.1, "x2": 0.9}

# Run Newton's method
solution = newton_method(functions, initial_guess, 2, True)
