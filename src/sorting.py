import time

def burbuja(lista):
    lista_auxiliar = lista.copy() # Copia la Lista Completa a una Lista Interna de la función - https://docs.python.org/3/library/stdtypes.html#list.copy
    inicio = time.time()
    n = len(lista_auxiliar)
    for i in range(n):
        for j in range(0, n - i - 1): # n - i - 1 porque i es cuantas pasadas hicimos y -1 comparamos con el siguiente j+1 entonces no llegamos al último índice
            if lista_auxiliar[j] > lista_auxiliar[j + 1]: # Si el elemento es Mayor al siguiente, Hay que cambiar de posición
                lista_auxiliar[j], lista_auxiliar[j + 1] = lista_auxiliar[j + 1], lista_auxiliar[j] # Aquí hacemos el intercambio de posición
    tiempo = time.time() - inicio
    return lista_auxiliar, tiempo


def seleccion(lista):
    lista = lista.copy()
    inicio = time.time()
    for i in range(len(lista)):
        min_idx = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    tiempo = time.time() - inicio
    return lista, tiempo


def insercion(lista):
    lista_auxiliar = lista.copy()  # Copia para no modificar la original
    inicio = time.time()

    for i in range(1, len(lista_auxiliar)):  # Empezamos desde 1 porque el índice 0 es con el que vamos a empezar comparando
        actual = lista_auxiliar[i]           # Elemento que queremos insertar -Lo Guardamos en "actual" para usarlo después
        indice_anterior = i - 1              # Índice del elemento anterior al actual

        # Mueve los elementos mayores una posición a la derecha
        # Mientras el índice anterior sea Mayor o igual a 0 y el elemento Actual sea menor al elemento Anterior
        while indice_anterior >= 0 and actual < lista_auxiliar[indice_anterior]:   
            lista_auxiliar[indice_anterior + 1] = lista_auxiliar[indice_anterior] # Al elemento Actual le ponemos el valor del Anterior
            indice_anterior -= 1 # Reducimos en 1 al índice

        # Inserta el elemento en la posición correcta
        lista_auxiliar[indice_anterior + 1] = actual # Insertamos "actual" en la posición que estamos intercambiando (Antes era el Actual)

    tiempo = time.time() - inicio
    return lista_auxiliar, tiempo


def quick_sort(lista):
    lista_auxiliar = lista.copy()
    inicio = time.time()

    def quicksort_recursivo(arr):
        if len(arr) <= 1:
            return arr
        else:
            pivote = arr[0]
            menores = [x for x in arr[1:] if x < pivote]
            mayores = [x for x in arr[1:] if x >= pivote]
            return quicksort_recursivo(menores) + [pivote] + quicksort_recursivo(mayores)

    lista_ordenada = quicksort_recursivo(lista_auxiliar)
    tiempo = time.time() - inicio
    return lista_ordenada, tiempo
