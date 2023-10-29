# ecuación lineal del tipo `ax + b = 0`
def resolver_ecuacion_lineal(a, b):
    if a == 0:
        return "No tiene solución" if b != 0 else "Infinitas soluciones"
    return -b/a

a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
print(f"Solución: x = {resolver_ecuacion_lineal(a, b)}")