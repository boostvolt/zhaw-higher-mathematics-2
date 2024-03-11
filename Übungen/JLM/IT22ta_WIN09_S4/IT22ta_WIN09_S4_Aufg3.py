import matplotlib.pyplot as plt
import numpy as np

# Aufgabe 3 a)

x = np.array([1981, 1984, 1989, 1993, 1997, 2000, 2001, 2003, 2004, 2010])
y = np.array([0.5, 8.2, 15, 22.9, 36.6, 51, 56.3, 61.8, 65, 76.7])
n_int = len(x)

z = np.polyfit(x, y, n_int)
x_axis = np.arange(1975, 2020, 0.1)


plt.plot(x_axis, np.polyval(z, x_axis))
plt.plot(x, y, marker="o", linewidth=0)
plt.ylim(-100, 250)
plt.xlim(1975, 2020)
plt.xlabel("Jahr")
plt.ylabel("Haushalte mit Computer [%]")
plt.title("Lagrange")
plt.legend(["f1(x)"])
plt.grid()
plt.show()

# Das Polynom geht nicht exakt durch alle Datenpunkte


# Aufgabe 3 b)

x = np.array([1981, 1984, 1989, 1993, 1997, 2000, 2001, 2003, 2004, 2010])
y = np.array([0.5, 8.2, 15, 22.9, 36.6, 51, 56.3, 61.8, 65, 76.7])
n_int = len(x)

z = np.polyfit(x - x.mean(), y, n_int)
x_axis = np.arange(1975, 2020, 0.1)


plt.plot(x_axis, np.polyval(z, x_axis - x.mean()))
plt.plot(x, y, marker="o", linewidth=0)
plt.ylim(-100, 250)
plt.xlabel("Jahr")
plt.ylabel("Haushalte mit Computer [%]")
plt.title("Lagrange")
plt.legend(["f1(x)"])
plt.grid()
plt.show()

# Punkte sind nun exakt auf dem Polynom.

# Aufgabe 3 c)

# Schätzwert für 2020: -infinity
# Dieser Wert ist nicht realistisch, da allgemein ein negativer Prozentsatz nicht erreichbar ist.

# Aufgabe 3 d)

def lagrange_int(x, y, x_int):
    y_int = []

    for xi in x_int:
        p = 0
        n = len(x)

        for i in range(0, n):
            l_n = 1
            for j in range(0, n):
                if j != i:
                    l_n *= (xi - x[j]) / (x[i] - x[j])
            p += y[i] * l_n
        y_int.append(p)
    return y_int


x = np.array([1981, 1984, 1989, 1993, 1997, 2000, 2001, 2003, 2004, 2010])
y = np.array([0.5, 8.2, 15, 22.9, 36.6, 51, 56.3, 61.8, 65, 76.7])


x_int = np.arange(1975, 2020, 0.1)
y_int = lagrange_int(x,y,x_int)



z = np.polyfit(x_int - x_int.mean(), y_int, 9)

plt.plot(x_int, y_int)
plt.plot(x_int, np.polyval(z, x_int - x.mean()))
plt.ylim(-100, 250)
plt.xlabel("Jahr")
plt.ylabel("Haushalte mit Computer [%]")
plt.title("Lagrange")
plt.legend(["Funktion aus Aufgabe 2", "Funktion aus Aufgabe 3b"])
plt.grid()
plt.show()

# In Aufgabe 2 haben wir nicht mit dem Mittelwert gerechnet