from sympy import *
import matplotlib.pyplot as plt
import numpy as np

# Definiere die Funktion
x = symbols('x')  # Symbol x
f = exp(-x ** 2)  # Funktion
n = 100  # Anzahl der x-Werte
x_vals = np.linspace(-3, 3, n)  # x-Werte
y_vals = [f.subs(x, val) for val in x_vals]  # Funktionswerte für alle x-Werte

# Ableitungen berechnen
f_prime = diff(f, x)
f_prime2 = diff(f_prime, x)

# Integral berechnen
f_int = integrate(f, x)
f_int2 = integrate(f_int, x)

# Ableitung printen und benennen
print("f(x) =", f)
print("f'(x) =", f_prime)
print("f''(x) =", f_prime2)
print("F(x) =", f_int)
print("F2(x) =", f_int2)

# Plotten der Funktion f(x), f'(x) und f''(x)
plt.plot(x_vals, y_vals)
plt.plot(x_vals, [f_prime.subs(x, val) for val in x_vals])
plt.plot(x_vals, [f_prime2.subs(x, val) for val in x_vals])
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['f(x)', "f'(x)", "f''(x)"])
plt.title("f(x) = " + str(f))
plt.show()
