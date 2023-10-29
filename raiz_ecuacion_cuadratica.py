# ecuación cuadrática `ax^2 + bx + c = 0`:

def raices_cuadraticas(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return "No tiene soluciones reales"
    elif discriminante == 0:
        return -b / (2*a)
    else:
        x1 = (-b + discriminante**0.5) / (2*a)
        x2 = (-b - discriminante**0.5) / (2*a)
        return x1, x2

a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))
print(f"Raíces: {raices_cuadraticas(a, b, c)}")
