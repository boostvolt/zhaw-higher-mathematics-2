import sympy as sp
import numpy as np

x0 = sp.Matrix([1.5,3,2.5])

x1, x2, x3 = sp.symbols('x1 x2 x3')
X = sp.Matrix([x1,x2,x3])

f1 = x1 + x2**2 - x3**2 -13
f2 = np.log(x2/4) + sp.exp(0.5*x3-1) - 1 # error
f3 = (x2 - 3)**2 - x3**3 + 7

f = sp.Matrix([f1,f2,f3])
Df = f.jacobian(X)

Df0 =  Df.subs([(x1,1.5), (x2,3), (x3,2.5)])
f0 = f.subs([(x1,1.5), (x2,3), (x3,2.5)])


print(f0)
print(Df0)

#g = f(x0) + Df(x0) * (x-x0)