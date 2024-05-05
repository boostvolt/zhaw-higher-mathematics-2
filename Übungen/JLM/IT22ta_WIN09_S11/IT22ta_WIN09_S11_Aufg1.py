import matplotlib.pyplot as plt
import numpy as np


def richtungsfeld(f, xmin, xmax, ymin, ymax, hx, hy):
    # Erzeuge das Punkteraster in der xy-Ebene
    x = np.arange(xmin, xmax, hx)
    y = np.arange(ymin, ymax, hy)
    X, Y = np.meshgrid(x, y)

    # Berechne die Steigung für jeden Punkt
    # Ydiff = f(X, Y)

    # Normalisiere die Längen der Pfeile
    # magnitude = np.sqrt(1 + Ydiff ** 2)
    U = np.ones((int((xmax - xmin) / hx), int((ymax - ymin) / hy)))
    # U = 1 / magnitude
    V = f(X, Y)

    # Plotte das Richtungsfeld
    plt.figure(figsize=(20, 12))
    plt.quiver(X, Y, U, V)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Richtungsfeld der Differentialgleichung")
    plt.grid(True)


if __name__ == "__main__":
    xmin = -2
    xmax = 2
    ymin = -3
    ymax = 3
    hx = 0.1
    hy = 0.1

    # Beispiel Funktion f(x, y) = x + y
    def f(x, y):
        return x**2 + 0.1 * y

    # Test der Funktion
    richtungsfeld(f, xmin, xmax, ymin, ymax, hx, hy)
    plt.show()
