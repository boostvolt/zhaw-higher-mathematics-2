import numpy as np
import matplotlib.pyplot as plt


# Funktion für das Anfangswertproblem
def f(t, y):
    return 9 / (2 + 2 * t)


# Exakte Lösungsfunktion
def exact_solution(t):
    return 1 - 1 / (2 * t) + 5


# Klassisches Runge-Kutta-Verfahren
def Name_S12_Aufg1(f, a, b, n, y0):
    h = (b - a) / n
    x = [a]
    y = [y0]

    for i in range(1, n + 1):
        xi = a + i * h
        k1 = f(x[i - 1], y[i - 1])
        k2 = f(x[i - 1] + 0.5 * h, y[i - 1] + 0.5 * h * k1)
        k3 = f(x[i - 1] + 0.5 * h, y[i - 1] + 0.5 * h * k2)
        k4 = f(x[i - 1] + h, y[i - 1] + h * k3)

        yi = y[i - 1] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

        x.append(xi)
        y.append(yi)

    return x, y


# Parameter für das Anfangswertproblem
a = 1
b = 6
n = int((b - a) / 0.01)
y0 = 5

# Numerische Lösung berechnen
x_numerical, y_numerical = Name_S12_Aufg1(f, a, b, n, y0)

# Exakte Lösung berechnen
x_exact = np.linspace(a, b, 1000)
y_exact = exact_solution(x_exact)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(x_numerical, y_numerical, label='Numerische Lösung', color='blue')
plt.plot(x_exact, y_exact, label='Exakte Lösung', color='red', linestyle='--')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Numerische und Exakte Lösung des Anfangswertproblems')
plt.legend()
plt.grid(True)
plt.show()
