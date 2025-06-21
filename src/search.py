import time

def busqueda_secuencial(lista, objetivo):
    inicio = time.time()
    for i, valor in enumerate(lista):
        if valor.lower() == objetivo.lower():
            tiempo = time.time() - inicio
            return i, tiempo
    tiempo = time.time() - inicio
    return -1, tiempo

# Ordenamos la Lista Primero por eso la posición puede variar respecto al método secuencial
def busqueda_binaria(lista, objetivo):
    inicio = time.time()
    lista_ordenada = sorted(lista) # Crea una Nueva Lista Ordenada usando un método de Python
    bajo = 0 # Rango de Búsqueda inferior
    alto = len(lista_ordenada) - 1 # Rango de Búsqueda superior
    while bajo <= alto:
        mitad = (bajo + alto) // 2
        if lista_ordenada[mitad].lower() == objetivo.lower():
            tiempo = time.time() - inicio
            return mitad, tiempo
        elif lista_ordenada[mitad].lower() < objetivo.lower(): # Busca en la mitad Derecha porque la mitad es Menor a lo que se busca.
            bajo = mitad + 1
        else:                                                  # Busca en la mitad Izquierda porque la mitad es Mayor a lo que se busca.
            alto = mitad - 1
    tiempo = time.time() - inicio
    return -1, tiempo
