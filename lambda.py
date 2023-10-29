def agrupar_por_longitud(palabras):
    longitudes_unicas = sorted(set(map(len, palabras)))
    return [[palabra for palabra in palabras if len(palabra) == longitud] for longitud in longitudes_unicas]

# Probar la función
lista_palabras = ["manzana", "kiwi", "banana", "uva", "fresa", "mango", "pera", "cereza"]
resultado = agrupar_por_longitud(lista_palabras)
print(resultado)
