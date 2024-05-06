import numpy as np
import matplotlib.pyplot as plt
from IT22ta_WIN09_S12_Aufg1 import Name_S12_Aufg1

# Funktion für das Anfangswertproblem
def f(t, y):
    return 9 / (2 + 2 * t)

# Exakte Lösungsfunktion
def exact_solution(t):
    return 1 - 1 / (2 * t) + 5

# Neues Runge-Kutta-Verfahren
def new_runge_kutta(f, a, b, n, y0):
    h = (b - a) / n
    x = [a]
    y = [y0]

    for i in range(1, n + 1):
        xi = a + i * h
        k1 = f(x[i - 1], y[i - 1])
        k2 = f(x[i - 1] + 0.5 * h, y[i - 1] + 0.5 * h * k1)
        k3 = f(x[i - 1] + 2/3 * h, y[i - 1] + 2/3 * h * k2)
        k4 = f(x[i - 1] + h, y[i - 1] + h * (k1/6 + k2/3 + k3/2))

        yi = y[i - 1] + (h / 10) * (k1 + 2 * k2 + 3 * k3 + 4 * k4)

        x.append(xi)
        y.append(yi)

    return x, y

# Parameter für das Anfangswertproblem
a = 1
b = 6
n = int((b - a) / 0.01)
y0 = 5

# Numerische Lösung berechnen mit klassischem Runge-Kutta-Verfahren
x_numerical_classic, y_numerical_classic = Name_S12_Aufg1(f, a, b, n, y0)

# Numerische Lösung berechnen mit neuem Runge-Kutta-Verfahren
x_numerical_new, y_numerical_new = new_runge_kutta(f, a, b, n, y0)

# Exakte Lösung berechnen
x_exact = np.linspace(a, b, 1000)
y_exact = exact_solution(x_exact)

# Plot der Lösungen
plt.figure(figsize=(10, 6))
plt.plot(x_numerical_classic, y_numerical_classic, label='Klassisches RK-Verfahren', color='blue')
plt.plot(x_numerical_new, y_numerical_new, label='Neues RK-Verfahren', color='green')
plt.plot(x_exact, y_exact, label='Exakte Lösung', color='red', linestyle='--')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Numerische Lösungen des Anfangswertproblems')
plt.legend()
plt.grid(True)
plt.show()

# Berechnung und Plot des absoluten Fehlers
absolute_error_classic = np.abs(np.array(y_exact) - np.interp(x_exact, x_numerical_classic, y_numerical_classic))
absolute_error_new = np.abs(np.array(y_exact) - np.interp(x_exact, x_numerical_new, y_numerical_new))

plt.figure(figsize=(10, 6))
plt.plot(x_exact, absolute_error_classic, label='Absoluter Fehler (klassisches RK)', color='blue')
plt.plot(x_exact, absolute_error_new, label='Absoluter Fehler (neues RK)', color='green')
plt.xlabel('t')
plt.ylabel('Absoluter Fehler')
plt.title('Absoluter Fehler der numerischen Lösungen')
plt.legend()
plt.grid(True)
plt.show()
