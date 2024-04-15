from sympy import *

# Define the function
x = symbols('x')  # Symbol x
f = cos(x**2)  # Function
a = 0  # Lower bound
b = pi  # Upper bound
m = 5  # Number of fragments
acc = 4 # Accuracy


# Romberg extrapolation
def rombergFunction(f, a, b, m):
    h = b - a
    R = [[0 for i in range(m)] for j in range(m)]
    R[0][0] = (h / 2 * (f.subs(x, a) + f.subs(x, b))).evalf()
    for i in range(1, m):
        h = h / 2
        sum = 0
        for k in range(1, 2 ** i, 2):
            sum += f.subs(x, a + k * h)
        R[i][0] = (R[i - 1][0] / 2 + sum * h).evalf()
        for j in range(1, i + 1):
            R[i][j] = (R[i][j - 1] + (R[i][j - 1] - R[i - 1][j - 1]) / (4 ** j - 1)).evalf()
    return R

# Print matrix in a readable way and round to 4 decimal places
for row in rombergFunction(f, a, b, m):
    print([round(elem, acc) for elem in row])