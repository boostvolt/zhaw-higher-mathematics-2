import numpy as np
import matplotlib.pyplot as plt


def task_a(x, y):
    polynom = np.polyfit(x, y, x.size - 1)
    plt.figure()
    x_value = np.arange(1975, 2020, 0.1)
    plt.plot(x_value, np.polyval(polynom, x_value))
    plt.plot(x, y, marker = "o", linewidth = 0)
    plt.title("Aufgabe 3a")
    plt.xlabel("X")
    plt.ylim(-100, 250)
    plt.ylabel("Y")
    plt.grid()
    plt.show()
    


x = np.array([1981, 1984, 1989, 1993, 1997, 2000, 2001, 2003, 2004, 2010])
y = np.array([0.5, 8.2, 15, 22.9, 36.6, 51, 56.3, 61.8, 65, 76.7])

task_a(x, y)
# Das Polynom geht nicht ganz genau durch alle Punkte aber beinahe perfekt

############################

def task_b(x, y):
    polynom = np.polyfit(x - x.mean(), y, x.size - 1)
    plt.figure()
    x_value = np.arange(1975, 2020, 0.1)
    plt.plot(x_value, np.polyval(polynom, x_value - x.mean()))
    plt.plot(x, y, marker = "o", linewidth = 0)
    plt.title("Aufgabe 3b")
    plt.xlabel("X")
    plt.ylim(-100, 250)
    plt.ylabel("Y")
    plt.grid()
    plt.show()
    


x = np.array([1981, 1984, 1989, 1993, 1997, 2000, 2001, 2003, 2004, 2010])
y = np.array([0.5, 8.2, 15, 22.9, 36.6, 51, 56.3, 61.8, 65, 76.7])    

task_b(x, y)
#Das Polynom geht genau durch alle Punkte

############################

def task_c(x, y, x_int):
    polynom = np.polyfit(x - x.mean(), y, x.size - 1)
    return np.polyval(polynom, x_int)


print(task_c(x, y, 2020))
# Nein es ist nicht realistisch. Zahlen ausserhalb des Intervals sind nicht repräsentativ durch das Polynom.

############################

def lagrange_int(x, y, x_int):
    y_int = np.zeros(x_int.size)

    for i in range(x_int.size):
        L = np.ones(x.size)

        for j in range(x.size):
            for h in range(x.size):
                if j != h:
                    L[h] *= (x_int[i] - x[j]) / (x[h] - x[j])

        for k in range(x.size):
            y_int[i] += L[k] * y[k]

    return y_int
    

def task_d(x, y):
    polynom = np.polyfit(x - x.mean(), y, x.size - 1)
    plt.figure()
    x_value = np.arange(1975, 2020, 0.1)
    plt.plot(x_value, lagrange_int(x, y, np.array(x_value, dtype=np.float64)))
    plt.plot(x_value, np.polyval(polynom, x_value - x.mean()))
    plt.plot(x, y, marker = "o", linewidth = 0)
    plt.title("Aufgabe 3d")
    plt.xlabel("X")
    plt.ylim(-100, 250)
    plt.ylabel("Y")
    plt.grid()
    plt.show()

task_d(x, y)