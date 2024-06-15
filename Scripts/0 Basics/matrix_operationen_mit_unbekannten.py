from sympy import Matrix, symbols

# Definieren Sie unbekannte Variablen
a, b = symbols("a b")

# Erstellen Sie Matrizen mit unbekannten Variablen
A = Matrix([[-4, 2], [0, (-4 / b)]])

# Ein Vektor wird auch mit Matrix() erstellt!
B = Matrix([[-4], [-1 + (4 / b)]])

C = Matrix([[2], [-1]])

# Lösen Sie das Gleichungssystems A * X = B
X = A.solve((-1) * B)

F = C + X

# Zeigen Sie das Ergebnis an
print("Lösung des Gleichungssystems:")
print(X)
print(F)
