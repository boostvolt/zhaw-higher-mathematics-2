import sympy as sp

x1, x2, x3 = sp.symbols("x1 x2 x3")
f1 = x1 + x2**2 - x3**2 -13
f2 = sp.log(x2/4) + sp.exp(0.5*x3-1) - 1
f3 = (x2 -3)**2 - x3**3 + 7

f = sp.Matrix([f1, f2, f3])
Df = f.jacobian([x1, x2, x3])

x_0 = sp.Matrix([1.5,3,2.5])
print(f)
print(Df)

k = 0

# Nach 3 Durchläufen irgend in einem endlos State
while((f.subs([(x1, x_0[0]), (x2, x_0[1]), (x3, x_0[2])])).norm(2) > 10**(-5)):
    delta = Df.inv().subs([(x1, x_0[0]), (x2, x_0[1]), (x3, x_0[2])]) @ -(f.subs([(x1, x_0[0]), (x2, x_0[1]), (x3, x_0[2])]))
    x_0 = x_0 + (delta / 2**k)
    k += 1 # keine Ahnung, was die korrekte Definition von k ist
    print(k)
    print(x_0.evalf())

# Wird nicht erreicht
print("done")
print(x_0)