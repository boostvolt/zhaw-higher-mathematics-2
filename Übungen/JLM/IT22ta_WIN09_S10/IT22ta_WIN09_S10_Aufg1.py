from sympy import *
from IT22ta_WIN09_S9_Aufg3 import rombergFunction

# Define the function
x = symbols('x')  # Symbol x
m = 4  # Number of fragments
acc = 4 # Accuracy

# Definition 1a)
f = 97000 / (-5 * x ** 2 - 570000)  # Function
a = 100  # Lower bound
b = 0  # Upper bound

# Romberg extrapolation
print("----Aufgabe 1a)-----")
for row in rombergFunction(f, a, b, m):
    print([round(elem, acc) for elem in row])
print("--------------------")

# Definition 1b)
f = 97000 * x / (-5 * x ** 2 - 570000)  # Function
a = 100  # Lower bound
b = 0  # Upper bound

# Romberg extrapolation
print("----Aufgabe 1b)-----")
for row in rombergFunction(f, a, b, m):
    print([round(elem, acc) for elem in row])
print("--------------------")