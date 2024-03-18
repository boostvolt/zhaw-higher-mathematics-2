import matplotlib.pyplot as plt
import numpy as np
from IT22ta_WIN09_S5_Aufg2 import IT22ta_WIN09_S5_Aufg2
from scipy.interpolate import CubicSpline

# Aufgabe 3a

t = np.array([1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010])
p = np.array(
    [
        75.995,
        91.972,
        105.711,
        123.203,
        131.669,
        150.697,
        179.323,
        203.212,
        206.505,
        249.633,
        281.422,
        308.745,
    ]
)

xx = np.arange(1900, 2011, 1)
yy = IT22ta_WIN09_S5_Aufg2(t, p, xx)
plt.plot(xx, yy)
plt.plot(t, p, marker="o", linewidth=0)
plt.xlabel("Jahr")
plt.ylabel("Bevölkerungsanzahl der USA [in Mio.]")
plt.title("Aufgabe 3a - Bevölkerungsanzahl der USA")
plt.legend(["3a"])
plt.grid()
plt.show()

# Aufgabe 3b

x = np.array([1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010])
y = np.array(
    [
        75.995,
        91.972,
        105.711,
        123.203,
        131.669,
        150.697,
        179.323,
        203.212,
        206.505,
        249.633,
        281.422,
        308.745,
    ]
)
poly = CubicSpline(x, y)

x_int = np.arange(1900, 2020, 0.1)
y_int = poly(x_int)

plt.plot(x_int, y_int)
plt.plot(x, y, marker="o", linewidth=0)
plt.legend(["3b"])
plt.xlabel("Jahr")
plt.ylabel("Bevölkerungszahl der USA [in Mio.]")
plt.title("Aufgabe 3b - CubicSpline")
plt.grid()
plt.show()


# Aufgabe 3c

x_shifted = x - 1900
coefficients = np.polyfit(x_shifted, y, 11)
y_poly = np.polyval(coefficients, x_shifted)

plt.plot(x, y_poly)
plt.plot(x, y, marker="o", linewidth=0)
plt.xlabel("Jahr")
plt.ylabel("Bevölkerungszahl der USA [in Mio.]")
plt.title("Aufgabe 3c - Polynom 11. Grades")
plt.legend(["3c"])
plt.grid()
plt.show()

# Das Resultat in Aufgabe 3c ist identisch mit Aufgabe 3a. Die Plots sind exakt deckungsgleich.
# Die Aufgabe 3b hat keine Kanten und liegt exakter auf den Stützpunkten.
