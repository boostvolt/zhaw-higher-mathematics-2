import numpy as np
import matplotlib.pyplot as plt
'''INPUT'''
x_in = np.array([0, 1, 2, 3, 4, 5], dtype=np.float64)
y_in = np.array([0.54, 0.44, 0.28, 0.18, 0.12, 0.08], dtype=np.float64)
x = np.arange(0, 5, 0.1)
grad = 4
'''INPUT'''


coeff = np.polyfit(x_in, y_in, grad) # polynom 4. Grades. da 6 Datenpunkte -2
print('x^1 bis x^n: ', coeff)

plt.figure(1)
plt.grid()
plt.plot(x, np.polyval(coeff, x), zorder=0, label='polyfit')
plt.scatter(x_in, y_in, marker='x', color='r', zorder=1, label='measured')
plt.legend()
plt.show()