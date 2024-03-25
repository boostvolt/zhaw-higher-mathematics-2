import numpy as np
import matplotlib.pyplot as plt

# Gegebene Daten
Ti = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) 
i = np.array([999.9, 999.7, 998.2, 995.7, 992.2, 988.1, 983.2, 977.8, 971.8, 965.3, 958.4])

# a) Ausgleichsfunktion f(T) = aT^2 + bT + c
A = np.array((Ti**2, Ti, np.ones_like(Ti))).T
y = i.T

ATA = A.T@A
AT = A.T

# Ohne QR-Zerlegung
lambda_no_qr = np.linalg.solve(ATA, AT @ y)
print(lambda_no_qr)

# Mit QR-Zerlegung
Q, R = np.linalg.qr(A)
lambda_qr = np.linalg.solve(R, Q.T@y)

# Datenpunkte und berechnete f(T)
T_values = np.linspace(0, 100, 10000)
f_values = np.array((T_values**2, T_values, np.ones_like(T_values))).T@ lambda_no_qr
f_values_qr = np.array((T_values**2, T_values, np.ones_like(T_values))).T @ lambda_qr

# Plot
plt.figure()
plt.plot(Ti, i, 'o', label='Datenpunkte')
plt.plot(T_values, f_values, '-', label='Ohne QR-Zerlegung')
plt.plot(T_values, f_values_qr, '--', label='Mit QR-Zerlegung')
plt.xlabel('Temperatur (°C)')
plt.ylabel('Dichte (g/l)')
plt.legend()
plt.title('Ausgleichsfunktion f(T) = aT^2 + bT + c')
plt.show()

# b) Konditionszahl der Matrizen A^T*A und R
cond_ATA = np.linalg.cond(A.T@ A, np.inf)
cond_R = np.linalg.cond(R, np.inf) 
print('Konditionszahl von A^T*A:', cond_ATA)
print('Konditionszahl von R:', cond_R)

# Die Konditionszahl von R ist besser, da sie um ein Faktor 10'000 kleiner ist als die Konditionszahl von A^T*A. 
# Der Fehler ist also geringer wenn wir die QR-Zerlegung benutzen.

# c) Verwendung von numpy.polyfit()
coefficients_polyfit = np.polyfit(Ti, i, 2)
f_values_polyfit = np.polyval(coefficients_polyfit, T_values) # Werte der Ausgleichsfunktion mit polyval

# Plot
plt.figure()
plt.plot(Ti, i, 'o', label='Datenpunkte')
plt.plot(T_values, f_values, '-', label='Ohne QR-Zerlegung')
plt.plot(T_values, f_values_qr, '--', label='Mit QR-Zerlegung')
plt.plot(T_values, f_values_polyfit, '-.', label='Mit numpy.polyfit()')
plt.xlabel('Temperatur (°C)')
plt.ylabel('Dichte (g/l)')
plt.legend()
plt.title('Ausgleichsfunktion f(T) = aT^2 + bT + c')
plt.show()


# d) Fehlerfunktionale berechnen
f_error = np.linalg.norm(y - (A @ lambda_no_qr), 2)**2 # Fehlerfunktional ohne QR-Zerlegung
f_error_qr = np.linalg.norm(y - (A @ lambda_qr), 2)**2 # Fehlerfunktional mit QR-Zerlegung
print('Fehlerfunktional ohne QR-Zerlegung:', f_error)
print('Fehlerfunktional mit QR-Zerlegung:', f_error_qr)

# Das Fehlerfunktional mit QR-Zerlegung ist minim kleiner. Bis zu einer Genauigkeit von 
# 10**(-12) sind sie identisch.