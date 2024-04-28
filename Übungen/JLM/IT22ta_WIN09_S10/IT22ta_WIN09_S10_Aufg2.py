import numpy as np
import matplotlib.pyplot as plt

# Gegebene Konstanten
vrel = 2600  # relative Ausströmgeschwindigkeit des Treibstoffs in m/s
mA = 3000000  # Anfangsmasse der Rakete in kg
mE = 800000  # Masse der Rakete am Ende der Brennphase in kg
tE = 190  # Dauer der Brennphase in s
g = 9.81  # Fallbeschleunigung in m/s^2
n = 1000  # Anzahl der Schritte
mu = (mA-mE) / tE

# Funktion für die Beschleunigung der Rakete
def acceleration(t):
    return vrel * mu / (mA - mu * t) - g

# Trapezregel zur numerischen Integration
def trapezoidal_rule(func, a, b, n):
    h = (b - a) / n
    integral = 0.5 * (func(a) + func(b))
    for i in range(1, n):
        integral += func(a + i * h)
    integral *= h
    return integral

# Funktion zur Berechnung der Geschwindigkeit und Höhe
def calculate_velocity_and_height():
    # Zeitpunkte
    t_values = np.linspace(0, tE, n)

    # Beschleunigung und Geschwindigkeit berechnen
    acceleration_values = np.array([acceleration(t) for t in t_values])
    velocity_values = np.array([trapezoidal_rule(acceleration, 0, t, n) for t in t_values])

    # Geschwindigkeit in m/s und Höhe in m berechnen
    height_values = np.array([trapezoidal_rule(lambda t: velocity_values[i], 0, t, 1000) for i, t in enumerate(t_values)])

    return t_values, velocity_values, height_values

# Berechnung von t, v(t) und h(t)
t, v, h = calculate_velocity_and_height()
t_analytical = vrel * np.log(mA / (mA - mu * t)) - g * t
h_analytical = -(vrel * (mA - mu * t) / mu) * (np.log(mA / (mA - mu * t))) + vrel * t - 0.5 * g * t ** 2

# Plotten von v(t) und h(t)
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.plot(t, acceleration(t))
plt.title('Beschleunigung der Rakete')
plt.xlabel('Zeit (s)')
plt.ylabel('Beschleunigung (m/s^2)')

plt.subplot(1, 3, 2)
plt.plot(t, v)
plt.plot(t, t_analytical)
plt.title('Geschwindigkeit der Rakete')
plt.legend(['Numerisch', 'Analytisch'])
plt.xlabel('Zeit (s)')
plt.ylabel('Geschwindigkeit (m/s)')

plt.subplot(1, 3, 3)
plt.plot(t, h)
plt.plot(t, h_analytical)
plt.title('Höhe der Rakete')
plt.legend(['Numerisch', 'Analytisch'])
plt.xlabel('Zeit (s)')
plt.ylabel('Höhe (m)')

plt.tight_layout()
plt.show()

# Geschwindigkeit und Höhe am Ende der ersten Brennphase
v_end = v[-1]
h_end = h[-1]
a_end = acceleration(tE)

print("Geschwindigkeit am Ende der ersten Brennphase:", v_end, "m/s")
print("Höhe am Ende der ersten Brennphase:", h_end, "m")
print("Beschleunigung am Ende der ersten Brennphase:", a_end, "m/s^2")
print("Beschleunigung in g: ", a_end / g, "g")
