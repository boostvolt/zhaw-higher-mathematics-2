import matplotlib.pyplot as plt
import numpy as np
from IT22ta_WIN10_S5_Aufg2 import IT22ta_WIN10_S5_Aufg2
from scipy.interpolate import CubicSpline

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
        226.505,
        249.633,
        281.422,
        308.745,
    ]
)

xx = np.arange(1900, 2011, 1)
yy = IT22ta_WIN10_S5_Aufg2(x, y, xx)
plt.plot(xx, yy)
plt.plot(x, y, marker="o", linewidth=0)
plt.xlabel("Jahr")
plt.ylabel("Bevölkerungsanzahl der USA [in Mio.]")
plt.title("Aufgabe 3a - Bevölkerungsanzahl der USA")
plt.legend(["3a"])
plt.grid()
plt.show()

##############################


def taskB():
    cs = CubicSpline(x, y)
    y_new = cs(x)

    plt.figure(figsize=(8, 4))
    plt.plot(x, y, "o", label="Datenpunkte")
    plt.plot(x, y_new, "-", label="Kubische Spline-Interpolation")
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Kubische Spline-Interpolation")
    plt.show()


taskB()


######################
# Die Zeitreihe wird auf das Jahr 0 geändert, um numerische Stabilität bei der Berechnung von Polynomen zu verbessern, insbesondere bei hohen Graden.
def taskC():
    xnew = x - 1900
    coeffs = np.polyfit(xnew, y, 11)
    xvalues = np.linspace(xnew[0], xnew[-1], 500)
    plt.figure(figsize=(8, 4))
    plt.plot(xnew, y, "o", label="Datenpunkte")
    plt.plot(xvalues, np.polyval(coeffs, xvalues), "-", label="Polynom 11. Grades")
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Kubische Spline-Interpolation")
    plt.show()


taskC()
