import matplotlib.pyplot as plt
import numpy as np

# Daten (Jahr, Anzahl der Transistoren)
data = np.array(
    [
        [1971, 2250.0],
        [1972, 2500.0],
        [1974, 5000.0],
        [1978, 29000.0],
        [1982, 120000.0],
        [1985, 275000.0],
        [1989, 1180000.0],
        [1989, 1180000.0],
        [1993, 3100000.0],
        [1997, 7500000.0],
        [1999, 24000000.0],
        [2000, 42000000.0],
        [2002, 220000000.0],
        [2003, 410000000.0],
    ]
)

# # Extrahieren der Jahre und der Anzahl der Transistoren
years = data[:, 0]
transistors = data[:, 1]

# Fit
t = years - 1970
log_transistoren = np.log10(transistors)
fit = np.polyfit(t, log_transistoren, 1)

# Plot
plt.semilogy(years, transistors, "bo", label="Daten")
plt.semilogy(years, 10 ** (fit[0] * t + fit[1]), "r-", label="Fit")
plt.xlabel("Jahr")
plt.ylabel("Anzahl Transistoren")
plt.title("Entwicklung der Transistoranzahl in Prozessorchips")
plt.legend()
plt.grid(True)
plt.show()

# Ausgabe der Fit-Parameter
print("Fit-Parameter:")
print("Theta1:", fit[1])
print("Theta2:", fit[0])

# Extrapolation für 2015
t_2015 = 2015 - 1970
anzahl_transistoren_2015 = 10 ** (fit[0] * t_2015 + fit[1])
print("Geschätzte Anzahl Transistoren im Jahr 2015:", anzahl_transistoren_2015)

# θ_1 beschreibt den Startwert und θ_2 beschreibt die Steigung der Gerade oder den Faktor um welchen die Werte wachsen.
# Ein Wert ca. 0.5 würde bedeuten, dass sich die Transistoren alle 1.5 bis 2 Jahre verdoppeln.
