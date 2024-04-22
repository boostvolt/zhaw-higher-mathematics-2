import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Definiere die Funktion
x = sp.symbols('x')     # Symbol x
g = 9.81                # Erdbeschleunigung
ma = 300000             # Masse der Rakete
te = 190                # Brenndauer
me = 80000              # Masse der Rakete ohne Treibstoff
mu = (ma - me) / te     # Masse des Treibstoffs pro Sekunde
f_v = 2600 * mu / (ma - mu * x) - g     # Funktion f(x)
# Funktion umstellen, um Höhe f_h zu berechnen:
f_h = 2600 * mu / (ma - mu * x) - g     # TODO: Funktion anpassen.
a = 0                   # Startwert
b = 190                 # Endwert
n = 190                 # Anzahl der x-Werte
h = (b - a) / n         # Schrittweite

exact_result = 10 # TODO: Ersetzen: sp.integrate.quad(lambda v: 2600 * mu / (ma - mu * v) - g, a, b)
x_vals = np.linspace(a, b, n)  # x-Werte
v_vals = [f_v.subs(x, val) for val in x_vals]  # Funktionswerte für alle x-Werte
h_vals = [f_h.subs(x, val) for val in x_vals]  # Funktionswerte für alle x-Werte

# Ableitung printen und benennen
print("v(x) =", f_v)
print("h(x) =", f_h)
# Plotten der Funktion f(x), f'(x) und f''(x)
plt.plot(x_vals, v_vals)
plt.plot(x_vals, h_vals)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['v(x)', "h(x)"])
plt.title("Geschwindigkeit und Höhe der Rakete über der Zeit")
plt.show()


def sum_trapezregel(a, b, h, exact_result, f, n):
    sum = 0

    for i in range(1, n):
        sum += f(a + i * h)

    Tf = h * ((f(a) + f(b)) / 2 + sum)
    abs_error = np.abs(Tf - exact_result[0])

    print(f"Summierte Trapezregel: {Tf}")
    print(f"Absoluter Fehler Trapezregel: {abs_error}")

# TODO: Trapezregel anwenden.
#sum_trapezregel(a, b, h, exact_result, f, n)