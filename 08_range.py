def criba_eratostenes(n):
    # Inicializamos una lista con todos los números como True. Un valor en prime[i] será
    # False si i no es un número primo, de lo contrario True bool
    primos = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        
        # Si primos[p] no se cambió, entonces es un primo
        if (primos[p] == True):
            
            # Actualizar todos los múltiplos de p
            for i in range(p * p, n+1, p):
                primos[i] = False
        p += 1
    
    # Recolectar y retornar los números primos
    numeros_primos = []
    for p in range(2, n):
        if primos[p]:
            numeros_primos.append(p)
    
    return numeros_primos

# Prueba
limite = int(input("Introduce el límite superior para buscar números primos: "))
print(f"Números primos hasta {limite}: {criba_eratostenes(limite)}")
