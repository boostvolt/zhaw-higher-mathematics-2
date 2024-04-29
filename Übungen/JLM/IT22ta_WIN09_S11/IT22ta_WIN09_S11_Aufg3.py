import numpy as np
import matplotlib.pyplot as plt
from IT22ta_WIN09_S11_Aufg1 import richtungsfeld


def f(x, y):
    return x ** 2 / y


def anfangswertproblem(f, a, b, n, y0):
    x = np.zeros(n + 1)
    y_euler = np.zeros(n + 1)
    y_mittelpunkt = np.zeros(n + 1)
    y_modeuler = np.zeros(n + 1)
    x[0] = a
    y_euler[0] = y0
    y_mittelpunkt[0] = y0
    y_modeuler[0] = y0
    for i in range(n):
        x[i + 1] = x[i] + h
        y_euler[i + 1] = y_euler[i] + h * f(x[i], y_euler[i])
        y_mittelpunkt[i + 1] = y_mittelpunkt[i] + h * f(x[i] + h / 2,
                                                        y_mittelpunkt[i] + h / 2 * f(x[i], y_mittelpunkt[i]))
        y_modeuler[i + 1] = y_modeuler[i] + h / 2 * (
                    f(x[i], y_modeuler[i]) + f(x[i + 1], y_modeuler[i] + h * f(x[i], y_modeuler[i])))
    return [x, y_euler, y_mittelpunkt, y_modeuler]


# Define the variables
a = 0
b = 1.4
h = 0.7
# convert to int
n = int((b - a) / h)
x = np.zeros(n + 1)
y = np.zeros(n + 1)
x[0] = a
y[0] = 2
ymin = 2
ymax = 3



# Calculate the solution with euler, midpoint and modified euler method
[x, y_euler, y_mittelpunkt, y_modeuler] = anfangswertproblem(f, a, b, n, y[0])

# Erzeuge das Punkteraster in der xy-Ebene
x = np.arange(a, b + h, h)
y_exact = np.sqrt((2 * x ** 3) / 3 + 4)



X, Y = np.meshgrid(x, y)

# Berechne die Steigung für jeden Punkt
Ydiff = f(X, Y)

# Normalisiere die Längen der Pfeile
magnitude = np.sqrt(1 + Ydiff ** 2)
U = 1 / magnitude
V = Ydiff / magnitude

# Berechne die Farben basierend auf der Steigung
color = np.arctan2(V, U)

# Plotte das Richtungsfeld
plt.figure(figsize=(20, 16))
plt.plot(x, y_exact)
plt.quiver(X, Y, U, V, color, cmap='RdYlGn_r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Richtungsfeld der Differentialgleichung')
plt.grid(True)
plt.show()

# Plot the exact solution
