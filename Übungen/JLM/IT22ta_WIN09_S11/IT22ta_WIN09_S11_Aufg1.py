import numpy as np
import matplotlib.pyplot as plt



def richtungsfeld(f, xmin, xmax, ymin, ymax, hx, hy):
    # Erzeuge das Punkteraster in der xy-Ebene
    x = np.arange(xmin, xmax + hx, hx)
    y = np.arange(ymin, ymax + hy, hy)
    X, Y = np.meshgrid(x, y)

    # Berechne die Steigung für jeden Punkt
    Ydiff = f(X, Y)

    # Normalisiere die Längen der Pfeile
    magnitude = np.sqrt(1 + Ydiff ** 2)
    U = 1 / magnitude
    V = Ydiff / magnitude

    # Berechne die Farben basierend auf der Steigung
    color = np.arctan2(V, U)

    # Plotte das Richtungsfeld
    plt.figure(figsize=(20, 16))
    plt.quiver(X, Y, U, V, color, cmap='RdYlGn_r')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Richtungsfeld der Differentialgleichung')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    xmin = 0
    xmax = 5
    ymin = 0
    ymax = 3
    hx = 0.1
    hy = 0.1
    # Beispiel Funktion f(x, y) = x + y
    def f(x, y):
        return x**2 + 0.1*y


    # Test der Funktion
    richtungsfeld(f, xmin, xmax, ymin, ymax, hx, hy)