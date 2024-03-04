from sympy import Matrix, symbols, sympify, plot_implicit, Eq

def get_minimum_k(functions, initial_guess):
    variables = symbols(' '.join(initial_guess.keys()))
    jacobian_matrix = Matrix(functions).jacobian(variables)
    delta = -jacobian_matrix.inv().subs(initial_guess) * Matrix(functions).subs(initial_guess)
    for i in range(10):
        if(initial_guess + delta)

def newton_method(functions, initial_guess, tolerance, debug=False):
    functions = [sympify(f) for f in functions]  # Convert strings to SymPy expressions
    variables = symbols(' '.join(initial_guess.keys()))
    jacobian_matrix = Matrix(functions).jacobian(variables)
    current_guess = initial_guess.copy()



    while True:
        delta = -jacobian_matrix.inv().subs(current_guess) * Matrix(functions).subs(current_guess)

        for j, var in enumerate(variables):
            current_guess[str(var)] = (current_guess[str(var)] + delta[j]).evalf() * 0.5

        f_norm = Matrix(functions).subs(current_guess).norm()

        if debug:
            print(f"x = {current_guess}, ||f(x)|| = {f_norm.evalf()}")

        if f_norm < tolerance:
            break

    print()
    return current_guess


functions = [
    "x1 + x2 - x3**2 - 13",
    "log(x2/4) + exp(0.5 * x3) - 1",
    "(x2 - 3)**2 - x3**3 + 7"
]