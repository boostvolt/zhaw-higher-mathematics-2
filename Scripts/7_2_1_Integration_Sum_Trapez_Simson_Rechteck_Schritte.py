import numpy as np
import scipy as sc
import sympy as sy

'''INPUT'''
x = sy.symbols('x')

f = 2000 * sy.log(10_000 / (10_000 - 100 * x)) - 9.8 * x  # funktion

a, b = 0.0, 30
err = 0.1
'''INPUT'''

erste_ableitung = f.diff(x)
zweite_ableitung = erste_ableitung.diff()
dfl = sy.lambdify(x, zweite_ableitung)
print('f\'(x): ', str(erste_ableitung), '     f\'\'(x): ', str(zweite_ableitung))

x_range = np.linspace(a, b, 100)
max_y = np.amax(abs(dfl(x_range)))
print('max wert:', max_y)

h_rf = np.sqrt(err * 24 / ((b - a) * max_y))
h_tf = np.sqrt(err * 12 / ((b - a) * max_y))
h_sf = np.sqrt(np.sqrt(err * 2880 / ((b - a) * max_y)))

print('max Schrittweite Rechteck: ', h_rf, 'max Schritte n=',np.ceil((b-a)/h_rf))
print('max Schrittweite Trapez: ', h_tf, 'max Schritte n=',np.ceil((b-a)/h_tf))
print('max Schrittweite Simpson: ', h_sf, 'max Schritte n=',np.ceil((b-a)/h_sf))

