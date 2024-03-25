import numpy as np
import matplotlib.pyplot as plt

data=np.array([
    [1971, 2250.],
    [1972, 2500.],
    [1974, 5000.],
    [1978, 29000.],
    [1982, 120000.],
    [1985, 275000.],
    [1989, 1180000.],
    [1989, 1180000.],
    [1993, 3100000.],
    [1997, 7500000.],
    [1999, 24000000.],
    [2000, 42000000.],
    [2002, 220000000.],
    [2003, 410000000.],   
    ])

jahr = data[:,:1].flatten()
transistoren = data[:,1:].flatten()

A = np.column_stack((jahr, np.ones_like(jahr)))
y = transistoren.T

ATA = A.T@A
AT = A.T

# Ohne QR-Zerlegung
lambda_ = np.linalg.solve(ATA, AT @ y)
print(lambda_)

jahr_values = np.linspace(1970,2004, 100)
transistor_values = 10 **(lambda_[0] + (jahr_values -1970)*lambda_[1])


plt.figure()
plt.semilogy(jahr, transistoren, 'o', label='Datenpunkte')
plt.plot(jahr_values,transistor_values)
plt.xlabel('Jahr')
plt.ylabel('Anzahl Transistoren')
plt.legend()
plt.title('Anzahl Transitoren pro Jahr')
plt.show()