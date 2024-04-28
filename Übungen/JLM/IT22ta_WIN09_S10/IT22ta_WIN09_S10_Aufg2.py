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
f_a = 2600 * mu / (ma - mu * x) - g     # Funktion f(x)
f_v = -9.81 * x - 2600. * sp.log(259.091 - x) + 14450     # Funktion f'(x)
f_h = (17050 - 4.905 * x) * x + (673637. - 2600 *x) * sp.log(259.091 - x) - 3742000     # Funktion f''(x)
a = 0                   # Startwert
b = 190                 # Endwert
n = 190                 # Anzahl der x-Werte
h = (b - a) / n         # Schrittweite

exact_result_v = 10
exact_result_h = 10
x_vals = np.linspace(a, b, n)  # x-Werte
a_vals = [f_a.subs(x, val) for val in x_vals]  # Funktionswerte a für alle x-Werte
v_vals = [f_v.subs(x, val) for val in x_vals]  # Funktionswerte v für alle x-Werte
h_vals = [f_h.subs(x, val) for val in x_vals]  # Funktionswerte h für alle x-Werte

# Plotten der Funktionen
plt.plot(x_vals, a_vals)
plt.plot(x_vals, v_vals)
plt.plot(x_vals, h_vals)

plt.xlabel('x')
plt.ylabel('y')
plt.legend(['a(x)', "v(x)", "h(x"])
plt.title("Geschwindigkeit und Höhe der Rakete über der Zeit")
plt.show()


def IT22ta_WIN09_S8_Aufg3a(x, y):
    Tf_neq = 0
    for i in range(len(x) - 1):
        Tf_neq += ((y[i] + y[i + 1]) / 2) * (x[i + 1] - x[i])
    return Tf_neq

# v(t) berechnen
print(IT22ta_WIN09_S8_Aufg3a(x_vals, a_vals))

# h(t) berechnen
#print(IT22ta_WIN09_S8_Aufg3a(x_vals, h_vals))