import sympy as sp

# Definiere das Symbol
x = sp.symbols("x")

# Berechne die Ableitung
f_prime = (2000 * 100**2) / (10000 - 100 * x) ** 2

value = 0
f_prime_value = f_prime.subs(x, value)

print(f"Der Wert der Ableitung bei x = {value} ist {f_prime_value}")
