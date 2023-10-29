def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Error: División por cero"
    return x / y

# Solicitar al usuario que introduzca dos números
try:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    # Mostrar opciones de operación
    print("\nSelecciona una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    # Solicitar al usuario que elija una operación
    seleccion = input("\nIntroduce el número de la operación deseada: ")

    if seleccion == '1':
        print(f"{num1} + {num2} = {sumar(num1, num2)}")
    elif seleccion == '2':
        print(f"{num1} - {num2} = {restar(num1, num2)}")
    elif seleccion == '3':
        print(f"{num1} x {num2} = {multiplicar(num1, num2)}")
    elif seleccion == '4':
        print(f"{num1} ÷ {num2} = {dividir(num1, num2)}")
    else:
        print("Selección no válida")

except ValueError:
    print("Por favor, introduce un número válido.")

