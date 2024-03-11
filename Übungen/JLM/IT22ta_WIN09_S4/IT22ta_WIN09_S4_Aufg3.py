import matplotlib.pyplot as plt
import numpy as np

# Aufgabe 3 a)

x_int = np.array([1981, 1984, 1989, 1993, 1997, 2000, 2001, 2003, 2004, 2010])
y_int = np.array([0.5, 8.2, 15, 22.9, 36.6, 51, 56.3, 61.8, 65, 76.7])

z = np.polyfit(x_int, y_int, 9)
x = np.arange(1975, 2020, 0.1)

plt.plot(x, np.polyval(z, x))
plt.plot(x_int, y_int, marker="o", linewidth=0)
plt.ylim(-100, 250)
plt.xlim(1975, 2020)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Polynomial")
plt.legend(["f1(x)"])
plt.grid()
plt.show()

# Das Polynom geht nicht exakt durch alle Datenpunkte


# Aufgabe 3 b)

x_int = np.array([1981, 1984, 1989, 1993, 1997, 2000, 2001, 2003, 2004, 2010])
y_int = np.array([0.5, 8.2, 15, 22.9, 36.6, 51, 56.3, 61.8, 65, 76.7])

z = np.polyfit(x_int - x_int.mean(), y_int, 9)
x = np.arange(1975, 2020, 0.1)

plt.plot(x, np.polyval(z, x - x_int.mean()))
plt.plot(x_int, y_int, marker="o", linewidth=0)
plt.ylim(-100, 250)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Polynomial")
plt.legend(["f1(x)"])
plt.grid()
plt.show()
