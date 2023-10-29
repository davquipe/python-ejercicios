def es_bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

def años_bisiestos_en_rango(año_inicio, año_fin):
    años_bisiestos = []
    dias_totales = 0
    
    for año in range(año_inicio, año_fin + 1):
        dias_año_actual = 366 if es_bisiesto(año) else 365
        dias_totales += dias_año_actual
        
        if es_bisiesto(año):
            años_bisiestos.append((año, dias_totales))
            
    return años_bisiestos

año_inicio = int(input("Introduce el año de inicio: "))
año_fin = int(input("Introduce el año final: "))

resultados = años_bisiestos_en_rango(año_inicio, año_fin)

print(f"Años bisiestos entre {año_inicio} y {año_fin}:")
for año, dias in resultados:
    print(f"Año {año}: Han pasado {dias} días desde el año {año_inicio}")
