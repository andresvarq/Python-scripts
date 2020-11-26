def ruteo(distancias: dict, ruta_inicial: list) -> dict:
    """ definir la mejor ruta """
    #distancia inicial
    distancia_inicial = 0
    i = 0
    for i in range((len(ruta_inicial) - 1)):
        j = i + 1
        distancia_inicial = distancia_inicial + distancias[ruta_inicial[i], ruta_inicial[j]]
        i = j

    #proceso
    distancia_comprobacion_1 = 1000000
    distancia_comprobacion_2 = 1000000
    distancia_final = distancia_comprobacion_2
    while not distancia_final > distancia_comprobacion_2:
        ruta =  '-'.join(ruta_inicial)
        i = 1
        a = 1
        x = 1
        k = 0
        l = 1
        for i in range(1, len(ruta_inicial) - 1):
            j = i + 1
            for j in range(2, len(ruta_inicial) - 1):
                #intercambio
                ruta_inicial.insert(i, ruta_inicial[j])
                ruta_inicial.insert((j + 1), ruta_inicial[i + 1])
                ruta_inicial.pop(i + 1)
                ruta_inicial.pop(j + 1)
                distancia_ciclo = distancias[ruta_inicial[0], ruta_inicial[1]] + distancias[ruta_inicial[-2], ruta_inicial[-1]]
                for a in range(1, (len(ruta_inicial) - 2)):
                    b = a + 1
                    distancia_ciclo = distancia_ciclo + distancias[ruta_inicial[a], ruta_inicial[b]]
                    a = b
                ruta_inicial.insert(i, ruta_inicial[j])
                ruta_inicial.insert((j + 1), ruta_inicial[i + 1])
                ruta_inicial.pop(i + 1)
                ruta_inicial.pop(j + 1)
                if distancia_comprobacion_1 > distancia_ciclo:
                    distancia_comprobacion_1 = distancia_ciclo
                    k = i
                    l = j
                j += 1
            if distancia_comprobacion_2 > distancia_comprobacion_1:
                distancia_comprobacion_2 = distancia_comprobacion_1
                k = i

        ruta_inicial.insert(k, ruta_inicial[l])
        ruta_inicial.insert((l + 1), ruta_inicial[k + 1])
        ruta_inicial.pop(k + 1)
        ruta_inicial.pop(l + 1)
        
        distancia_final = distancias[ruta_inicial[0], ruta_inicial[1]] + distancias[ruta_inicial[-2], ruta_inicial[-1]]
        for x in range(1, (len(ruta_inicial) - 2)):
            y = x + 1
            distancia_final = distancia_final + distancias[ruta_inicial[x], ruta_inicial[y]]
            x = y
    else:
        if distancia_final > distancia_comprobacion_2:
            distancia_final = distancia_comprobacion_2
    
    #validación
    for d in distancias.values():
        if d >= 0:
            resultado = {'ruta': ruta, 'distancia': distancia_final}
        else:
            resultado = 'Por favor revisar los datos de entrada.'
            break
    for i in range(len(ruta_inicial) - 1):
        if distancias[ruta_inicial[i], ruta_inicial[i]] != 0:
            resultado = 'Por favor revisar los datos de entrada.'
    return resultado

distancias1 = {('H', 'H'): 0, ('H', 'A'): 21, ('H', 'B'): 57, ('H', 'C'): 58, ('H', 'D'): 195, ('H', 'E'): 245,
             ('H', 'F'): 241, ('A', 'H'): 127, ('A', 'A'): 0, ('A', 'B'): 231, ('A', 'C'): 113, ('A', 'D'): 254,
             ('A', 'E'): 179, ('A', 'F'): 41,('B', 'H'): 153, ('B', 'A'): 252, ('B', 'B'): 0, ('B', 'C'): 56,
             ('B', 'D'): 126, ('B', 'E'): 160, ('B', 'F'): 269, ('C', 'H'): 196, ('C', 'A'): 128, ('C', 'B'): 80,
             ('C', 'C'): 0, ('C', 'D'): 136, ('C', 'E'): 37, ('C', 'F'): 180, ('D', 'H'): 30, ('D', 'A'): 40,
             ('D', 'B'): 256, ('D', 'C'): 121, ('D', 'D'): 0, ('D', 'E'): 194, ('D', 'F'): 109, ('E', 'H'): 33,
             ('E', 'A'): 144, ('E', 'B'): 179, ('E', 'C'): 114, ('E', 'D'): 237, ('E', 'E'): 0, ('E', 'F'): 119,
             ('F', 'H'): 267, ('F', 'A'): 61, ('F', 'B'): 79, ('F', 'C'): 39, ('F', 'D'): 135, ('F', 'E'): 55,
             ('F', 'F'): 0}
lista1 = ['H', 'A', 'B', 'C', 'D', 'E', 'F', 'H']
print(ruteo(distancias1, lista1))



distancias2 = {('H', 'H'): 0, ('H', 'A'): 60, ('H', 'B'): 202, ('H', 'C'): 206, ('H', 'D'): 40, ('H', 'E'): 27,
             ('A', 'H'): 72, ('A', 'A'): 0, ('A', 'B'): 135, ('A', 'C'): 150, ('A', 'D'): 240, ('A', 'E'): 117,
             ('B', 'H'): 188, ('B', 'A'): 166, ('B', 'B'): 0, ('B', 'C'): 149, ('B', 'D'): 126, ('B', 'E'): 199,
             ('C', 'H'): 39, ('C', 'A'): 19, ('C', 'B'): 123, ('C', 'C'): 0, ('C', 'D'): 206, ('C', 'E'): 19,
             ('D', 'H'): 45, ('D', 'A'): 14, ('D', 'B'): 110, ('D', 'C'): 95, ('D', 'D'): 0, ('D', 'E'): 31,
             ('E', 'H'): 36, ('E', 'A'): 179, ('E', 'B'): 235, ('E', 'C'): 106,('E', 'D'): 25, ('E', 'E'): 0}
lista2 = ['H', 'B', 'E', 'A', 'C', 'D', 'H']
print(ruteo(distancias2, lista2))