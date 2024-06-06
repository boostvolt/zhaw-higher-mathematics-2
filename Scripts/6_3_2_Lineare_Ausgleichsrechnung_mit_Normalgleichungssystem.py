import numpy as np
import matplotlib.pyplot as plt

'''INPUT '''
x = np.array([0, 1, 2, 3, 4, 5], dtype=np.float64)
y = np.array([0.54, 0.44, 0.28, 0.18, 0.12, 0.08], dtype=np.float64)

# Transformation für linearisierung der Ansatzfunktion
# 1 / (a+b*x^2) => Kehrwert. Dann muss auch y mit Kehrwert transformiert werden
y = 1/y
# ausgleichsfunktion = a => x, bx**2 => x**2
f1 = [1 for xi in x]
f2 = (x ** 2)
# f3 =
'''INPUT '''

print(
    '\nKonstruiere die Matrix A, so dass in Spalte 1 die Werte der Funktion f1(x) ausgewertet für alle xi stehen, usw. für die weiteren Spalten mit f2(x) und f3(x)')

A = np.array([f1, f2]).T
print('A = \n{}'.format(A))

print('\nFühre für A eine QR-Zerlegung durch, Q * R = A.')
Q, R = np.linalg.qr(A)
print('Q = \n{}\nR = {}'.format(Q, R))

print('\nLöse das LGS R * λ = QT * y')

coeff_direct = np.linalg.solve(A.T @ A, A.T @ y)
coeff_qr = np.linalg.solve(R, Q.T @ y)
coeff_polyfit = np.polyfit(x, y, A.shape[1] - 1)

error_direct = np.linalg.norm(y - A @ coeff_direct, 2) ** 2
error_qr = np.linalg.norm(y - A @ coeff_qr, 2) ** 2
error_polyfit = np.linalg.norm(y - A @ coeff_polyfit, 2) ** 2

print('\n\nMit direktem Lösen von AT * A * λ = AT * y: λ (a,b,..) (kleinste Q) = ' + str(coeff_direct))
print('Mit QR-Zerlegung: λ (a,b,..) = ' + str(coeff_qr))
print('Koeffizienten wenn mit numpy polyfit Grad 2 gelöst: λ = ' + str(coeff_polyfit))

print('\nKonditionszahl von AT * A = ' + str(np.linalg.cond(A.T @ A, np.inf)))
print('Konditionszahl von R = ' + str(np.linalg.cond(R, np.inf)))

print('\nFehler mit direktem Lösen = ' + str(error_direct))
print('Fehler mit QR = ' + str(error_qr))
print('Fehler mit numpy polyfit = ' + str(error_polyfit))

xx = np.arange(x[0], x[-1], (x[-1] - x[0]) / 1000)

plt.figure(1)
plt.grid()
plt.plot(xx, np.polyval(coeff_direct, xx), zorder=0, label='direct solve')
plt.plot(xx, np.polyval(coeff_qr, xx), label='qr + solve')
plt.plot(xx, np.polyval(coeff_polyfit, xx), label='np.polyfit')
plt.scatter(x, y, marker='x', color='r', zorder=1, label='measured')
plt.legend()
plt.show()

"""
b) Vergleichen Sie die Konditionszahl der auftretenden Matrizen ATA bzw. R. Was fällt Ihnen auf?

A: Beide Matrizen haben eine sehr schlechte Kondition; die Kondition von ATA ist aber noch einmal deutlich schlechter
   als die Kondition von R. Die resultierenden Koeffizienten unterscheiden sich mit den beiden Verfahren jedoch kaum
   und auch graphisch lassen sich kaum Diskrepanzen feststellen.


d) Berechnen Sie die Fehlerfunktionale für Ihre Lösungen aus a) und c). Gibt es Unterschiede?

A: Die Fehlerfunktionale sind bei allen Lösungsvarianten beinahe identisch. Die Lösungen unterscheiden sich graphisch
   fast gar nicht.
"""
