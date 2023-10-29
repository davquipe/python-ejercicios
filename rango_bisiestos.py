# Un año bisiesto es aquel que es divisible entre 4

def es_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    return False

año = int(input("Introduce un año: "))
if es_bisiesto(año):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")
