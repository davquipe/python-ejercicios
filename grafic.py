def dibujar_grafico_barras(valores):
    # Determinar la altura máxima de las barras
    max_val = max(valores)
    
    # Invertir el orden para dibujar de arriba a abajo
    for nivel in range(max_val, 0, -1):
        for valor in valores:
            # Si el valor es igual o mayor al nivel actual, dibujar una barra
            if valor >= nivel:
                print("█", end="  ")
            else:
                print(" ", end="  ")
        print()  # Salto de línea al final de cada fila

# Lista de valores para el gráfico
datos = [3, 7, 2, 5, 8]

# Llamada a la función
dibujar_grafico_barras(datos)
