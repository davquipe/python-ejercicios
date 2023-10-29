# Solicitar al usuario que introduzca los valores de x y y
x = float(input("Introduce el valor de x: "))
y = float(input("Introduce el valor de y: "))

# Realizar operaciones básicas con x y y
suma = x + y
resta = x - y
multiplicacion = x * y
division = x / y if y != 0 else "Indefinido"
modulo = x % y if y != 0 else "Indefinido"
exponente = x ** y

# Mostrar resultados
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
print(f"Módulo: {modulo}")
print(f"Exponente: {exponente}")
