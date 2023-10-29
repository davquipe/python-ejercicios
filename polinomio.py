# polinomio

def evaluar_polinomio(a, b, c, d, x):
    return a*x**3 + b*x**2 + c*x + d

a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))
d = float(input("Introduce el valor de d: "))
x = float(input("Introduce el valor de x: "))
print(f"Resultado: {evaluar_polinomio(a, b, c, d, x)}")
