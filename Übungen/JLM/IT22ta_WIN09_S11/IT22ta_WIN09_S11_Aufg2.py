import numpy as np


# Exakte Lösung der Differentialgleichung
def exact_solution(x):
    return np.sqrt(2 * x ** 3 / 3 + 4)


# Euler-Verfahren
def euler_method(h):
    x_values = np.arange(0, 1.4 + h, h)
    y_values = [2]
    for i in range(1, len(x_values)):
        y = y_values[i - 1] + h * x_values[i - 1] ** 2 / y_values[i - 1]
        y_values.append(y)
    return x_values, y_values


# Mittelpunkt-Verfahren
def midpoint_method(h):
    x_values = np.arange(0, 1.4 + h, h)
    y_values = [2]
    for i in range(1, len(x_values)):
        x_mid = x_values[i - 1] + h / 2
        y_mid = y_values[i - 1] + (h / 2) * x_values[i - 1] ** 2 / y_values[i - 1]
        y = y_values[i - 1] + h * x_mid ** 2 / y_mid
        y_values.append(y)
    return x_values, y_values


# Modifiziertes Euler-Verfahren
def modified_euler_method(h):
    x_values = np.arange(0, 1.4 + h, h)
    y_values = [2]
    for i in range(1, len(x_values)):
        y_euler = y_values[i - 1] + h * x_values[i - 1] ** 2 / y_values[i - 1]
        k1 = x_values[i - 1] ** 2 / y_values[i - 1]
        k2 = x_values[i] ** 2 / y_euler
        y = y_values[i - 1] + h * (k1 + k2) / 2
        y_values.append(y)
    return x_values, y_values


# Hauptfunktion
def main():
    h = 0.7

    # Berechnung der Lösungen
    x_euler, y_euler = euler_method(h)
    x_midpoint, y_midpoint = midpoint_method(h)
    x_modified, y_modified = modified_euler_method(h)

    # Berechnung des absoluten Fehlers
    exact_values = exact_solution(x_euler)
    error_euler = np.abs(exact_values - y_euler)
    error_midpoint = np.abs(exact_values - y_midpoint)
    error_modified = np.abs(exact_values - y_modified)

    # Ausgabe der Fehler
    print("Euler-Verfahren Fehler:")
    for i in range(len(x_euler)):
        print(f"Absoluter Fehler bei x={x_euler[i]}: {error_euler[i]}")

    print("\nMittelpunkt-Verfahren Fehler:")
    for i in range(len(x_midpoint)):
        print(f"Absoluter Fehler bei x={x_midpoint[i]}: {error_midpoint[i]}")

    print("\nModifiziertes Euler-Verfahren Fehler:")
    for i in range(len(x_modified)):
        print(f"Absoluter Fehler bei x={x_modified[i]}: {error_modified[i]}")


# Ausführung der Hauptfunktion
if __name__ == "__main__":
    main()
