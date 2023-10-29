def criba_eratostenes(n):
    # Crear una lista de booleanos y asumir que todos los números en el rango son primos
    primos = [True] * (n + 1)
    p = 2
    while p**2 <= n:
        # Si primos[p] no se ha cambiado, entonces es un primo
        if primos[p]:
            # Actualizar todos los múltiplos de p
            for i in range(p**2, n + 1, p):
                primos[i] = False
        p += 1
    
    # Recoger los números primos
    lista_primos = []
    for i in range(2, n + 1):
        if primos[i]:
            lista_primos.append(i)
    
    return lista_primos

# Probar la función
n = 50
print(f"Números primos hasta {n}: {criba_eratostenes(n)}")
