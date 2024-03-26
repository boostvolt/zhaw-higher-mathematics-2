from matplotlib import pyplot as plt
import sympy as sp
import numpy as np

x = np.array([0,10,20,30,40,50,60,70,80,90,100])
y = np.array([999.9, 999.7, 998.2, 995.7, 992.2, 988.1, 983.2, 977.8, 971.8, 965.3, 958.4 ])
t = sp.symbols("t")
f = np.array([t ** 2, t, 1])

A_test = np.array([])

A = np.zeros((11, 3))

for i in range(0, 11, 1):
    for j in range(0, 3, 1): 
        A[i][j] = sp.sympify(f[j]).subs(t, x[i])

# A
def a_solve(A, y):
    return np.linalg.solve(A.T @ A, A.T @ y)

def a_qr(A, y):
    Q, R = np.linalg.qr(A);
    return np.linalg.solve(R, Q.T @ y)

# B
print(np.linalg.cond((A.T@A), np.inf))
print(np.linalg.cond(np.linalg.qr(A)[1], np.inf))

# QR hat eine bessere Konditionszahl, auch wenn diese selber schon sehr gross ist.

# C
def c(x, y):
    return np.polyfit(x, y, 2)

print(c(x, y))

plt.scatter(x, y, label="a_solve")
plt.plot(x, np.polyval(a_solve(A, y), x))
plt.plot(x, np.polyval(a_qr(A, y), x))
plt.plot(x, np.polyval(c(x,y), x))
plt.show()

# D
print(np.sum((y - np.polyval(a_solve(A, y), x)) ** 2))
print(np.sum((y - np.polyval(a_qr(A, y), x)) ** 2))
print(np.sum((y - np.polyval(c(x,y), x)) ** 2))

# Es gibt sehr kleine Unterschiede, die aber nicht wirklich ins Gewicht fallen.