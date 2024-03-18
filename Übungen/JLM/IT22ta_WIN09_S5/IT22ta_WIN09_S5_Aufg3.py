import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

# Aufgabe 3a



# Aufgabe 3b

x = np.array([1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,2000,2010])
y = np.array([75.995, 91.972, 105.711, 123.203, 131.669, 150.697, 179.323, 203.212, 206.505, 249.633, 281.422, 308.745])
poly = CubicSpline(x, y)

x_int = np.arange(1900, 2020, 0.1)
y_int = poly(x_int)

plt.plot(x_int, y_int)
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
plt.xlabel("Jahr")
plt.ylabel("Bevölkerungszahl der USA [in Mio.]")
plt.title("Aufgabe 3c - Polynom 11. Grades")
plt.grid()
plt.show()