from sympy import Matrix, symbols, sympify

def newton_method(functions, initial_guess, tolerance, debug=False):
    functions = [sympify(f) for f in functions]  # Convert strings to SymPy expressions
    variables = symbols(" ".join(initial_guess.keys()))
    current_guess = initial_guess.copy()

    while True:
        jacobian_matrix = Matrix(functions).jacobian(variables)
        delta = -jacobian_matrix.inv().subs(current_guess) * Matrix(functions).subs(current_guess)
        k = 0
        condition_guess = current_guess.copy()
        for i in range(10, -1, -1):
            for j, var in enumerate(variables):
                condition_guess[str(var)] = (current_guess[str(var)] + (delta[j] / 2**i)).evalf()
            f_norm_condition = Matrix(functions).subs(condition_guess).norm()

            if f_norm_condition > Matrix(functions).subs(current_guess).norm():
                k = i + 1
                break

        for j, var in enumerate(variables):
            current_guess[str(var)] = (current_guess[str(var)] + (delta[j] / 2**k)).evalf()

        f_norm = Matrix(functions).subs(current_guess).norm()

        if debug:
            print(f"x = {current_guess}, ||f(x)|| = {f_norm.evalf()}")

        if f_norm < tolerance:
            break

    return current_guess

functions = [
    "x1 + x2**2 - x3**2 - 13",
    "log(x2/4) + exp(0.5 * x3) - 1",
    "(x2 - 3)**2 - x3**3 + 7",
]

x_0 = {"x1": 1.5, "x2": 3, "x3": 2.5}
newton_method(functions, x_0, 10**-5, True)