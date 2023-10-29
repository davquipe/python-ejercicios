def imprimir_gato():
    # Definimos las dimensiones
    ancho = 80
    alto = 30
    
    # Puntos centrales de los ojos, nariz y boca
    centro_ojo_izquierdo = (ancho * 1/3, alto / 3)
    centro_ojo_derecho = (ancho * 2/3, alto / 3)
    centro_nariz = (ancho / 2, alto / 2)
    
    for y in range(alto):
        for x in range(ancho):
            # Ecuación de círculo para los ojos
            condicion_ojo_izquierdo = ((x - centro_ojo_izquierdo[0])**2 + 
                                       (y - centro_ojo_izquierdo[1])**2 <= (ancho / 15)**2)
            
            condicion_ojo_derecho = ((x - centro_ojo_derecho[0])**2 +
                                     (y - centro_ojo_derecho[1])**2 <= (ancho / 15)**2)
            
            # Ecuación de círculo pequeño para las pupilas
            condicion_pupila_izquierda = ((x - centro_ojo_izquierdo[0])**2 + 
                                          (y - centro_ojo_izquierdo[1])**2 <= (ancho / 50)**2)
            
            condicion_pupila_derecha = ((x - centro_ojo_derecho[0])**2 + 
                                        (y - centro_ojo_derecho[1])**2 <= (ancho / 50)**2)
            
            # Ecuación de elipse para la nariz
            condicion_nariz = ((x - centro_nariz[0])**2 / (ancho / 30)**2 +
                               (y - centro_nariz[1])**2 / (alto / 20)**2 <= 1)

            # Condiciones para las orejas
            condicion_oreja_izquierda = y == (-2 * (x - ancho / 4)) and y < alto / 4
            condicion_oreja_derecha = y == (2 * (x - 3 * ancho / 4)) and y < alto / 4
            
            # Condiciones para el bigote
            condicion_bigote_izquierdo = (y - centro_ojo_izquierdo[1] == (x - centro_ojo_izquierdo[0]) / 2 or 
                                          y - centro_ojo_izquierdo[1] == -(x - centro_ojo_izquierdo[0]) / 2) and x < centro_ojo_izquierdo[0]
            
            condicion_bigote_derecho = (y - centro_ojo_derecho[1] == (x - centro_ojo_derecho[0]) / 2 or 
                                        y - centro_ojo_derecho[1] == -(x - centro_ojo_derecho[0]) / 2) and x > centro_ojo_derecho[0]

            # Dibujar basado en las condiciones
            if condicion_ojo_izquierdo or condicion_ojo_derecho:
                print('O', end='')
            elif condicion_pupila_izquierda or condicion_pupila_derecha:
                print('.', end='')
            elif condicion_nariz:
                print('^', end='')
            elif condicion_oreja_izquierda or condicion_oreja_derecha:
                print('^', end='')
            elif condicion_bigote_izquierdo or condicion_bigote_derecho:
                print('-', end='')
            else:
                print(' ', end='')
        print()

imprimir_gato()
