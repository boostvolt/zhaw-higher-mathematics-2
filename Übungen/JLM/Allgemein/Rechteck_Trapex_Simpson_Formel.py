import sympy as sp

# Definiere die Funktion
def f(x):
    return 10 / (-x * sp.sqrt(x))

# Rechteckregel
def rechteckregel(f, a, b, n):
    h = (b - a) / n  # Breite der Teilintervalle
    summe = 0
    for i in range(n):
        xi = a + i * h  # linke Grenze des i-ten Teilintervalls
        summe += f(xi)
    return summe * h

# Trapezregel
def trapezregel(f, a, b, n):
    h = (b - a) / n  # Breite der Teilintervalle
    summe = (f(a) + f(b)) / 2
    for i in range(1, n):
        xi = a + i * h  # linke Grenze des i-ten Teilintervalls
        summe += f(xi)
    return summe * h

def simpsonregel(f, a, b, n):
    h = (b - a) / n  # Breite der Teilintervalle
    summe = f(a) + f(b)
    for i in range(1, n):
        xi = a + i * h  # linke Grenze des i-ten Teilintervalls
        summe += 4 * f(xi - h / 2) + 2 * f(xi)
    return summe * h / 6

# Teste die Rechteckregel
a = 20
b = 5
n = 5

# Rechteckregel
res_rechteck = rechteckregel(f, a, b, n)
print("Rechteck:", res_rechteck)

# Trapezregel
res_trapez = trapezregel(f, a, b, n).evalf()
print("Trapez:", res_trapez)

# Simpsonregel (nur für gerade Anzahl an Teilintervallen)
res_simps = simpsonregel(f, a, b, n).evalf()
print("Simpson:", res_simps)
