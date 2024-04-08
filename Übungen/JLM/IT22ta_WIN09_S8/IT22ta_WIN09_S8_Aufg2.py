import scipy as sp
import numpy as np

exact_result = sp.integrate.quad(lambda v: 10 / (-v * (v ** 0.5)), 20, 5)
print(exact_result)

a = 20
b = 5
h = -3

# Aufgabe a)
def f(v):
    return -10 * (v ** (-3/2))

sum = 0

for i in range(0,5):
    sum += f(a + i*h + h/2)

Rf = h * sum
print(Rf)

abs_error = np.abs(Rf - exact_result[0])
print(abs_error)

# Aufgabe b)

sum = 0

for i in range(1,5):
    sum += f(a + i*h)

Tf = h * ((f(a)+f(b))/2 + sum)
print(Tf)
abs_error = np.abs(Tf - exact_result[0])
print(abs_error)

# Aufgabe c)

sum1 = 0
sum2 = 0

for i in range(1,5):
    sum1 += f(a + h*i)

for i in range(1,6):
    sum2 += f(((a + (i-1) * h) + (a + i * h))/2)

SF = h/3 * (1/2 * f(a) + sum1 + 2 * sum2 + 1/2 * f(b))
print(SF)
abs_error = np.abs(SF - exact_result[0])
print(abs_error)
