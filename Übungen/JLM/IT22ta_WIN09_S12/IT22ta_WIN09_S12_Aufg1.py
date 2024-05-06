def Name_S12_Aufg1(f, a, b, n, y0):
    h = (b - a) / n
    x = [a]
    y = [y0]

    for i in range(1, n + 1):
        xi = a + i * h
        k1 = f(x[i - 1], y[i - 1])
        k2 = f(x[i - 1] + 0.5 * h, y[i - 1] + 0.5 * h * k1)
        k3 = f(x[i - 1] + 0.5 * h, y[i - 1] + 0.5 * h * k2)
        k4 = f(x[i - 1] + h, y[i - 1] + h * k3)

        yi = y[i - 1] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

        x.append(xi)
        y.append(yi)

    return x, y
