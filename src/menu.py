from functions import mostrar_listado_completo
from search import busqueda_secuencial, busqueda_binaria
from sorting import burbuja, insercion, seleccion, quick_sort


def solicitar_opcion(mensaje, opciones_validas):
    while True:
        opcion = input(mensaje).strip()
        if opcion in opciones_validas:
            return opcion
        print(f"\n❌ Opción inválida.\nIntenta nuevamente por favor 🙏.")

        


def menu(peliculas, series, nombre):
    while True:
        print("\n📺 Elija el tipo de contenido:\n")
        print("1 - Películas")
        print("2 - Series")
        print("0 - Salir")
        tipo = solicitar_opcion("\nSeleccione una opción: ", ['0', '1', '2'])

        if tipo == '1':
            lista = peliculas
            tipo_str = "Películas"
        elif tipo == '2':
            lista = series
            tipo_str = "Series"
        elif tipo == '0':
            print(f"\nGracias por tu visita!🍿\nTe esperamos pronto {nombre}!! 👋")
            break

        while True:
            print(f"\n🛠 {nombre} ¿Qué desea hacer con las {tipo_str}?\n")
            print(f"1 - Ver Catálogo de {tipo_str}")
            print("2 - Buscar")
            print("3 - Ordenar")
            print("0 - Volver al menú principal")
            accion = solicitar_opcion("\nSeleccione una opción: ", ['0', '1', '2', '3'])

            if accion == '1':
                mostrar_listado_completo(lista, tipo_str, nombre)
            elif accion == '2':
                mostrar_metodos_busqueda(lista, tipo_str, nombre)
            elif accion == '3':
                mostrar_metodos_ordenamiento(lista, tipo_str, nombre)
            elif accion == '0':
                print(f"\n↩️   Volviendo al menú principal.")
                break


def mostrar_metodos_busqueda(lista, tipo_str, nombre):
    while True:
        print(f"\n🔍  Métodos de búsqueda disponibles para {tipo_str}\n")
        print("1 - Búsqueda Secuencial (Lineal)")
        print("2 - Búsqueda Binaria")
        print("0 - Volver al menú anterior")
        metodo = solicitar_opcion("\nSeleccione método de búsqueda: ", ['0', '1', '2'])

        if metodo == '0':
            print(f"\n↩️  Volviendo al menú anterior.")
            break

        # Para Buscar la Película o Serie (en Singular por eso usamos slice con el -1 para quitar el último caracter)
        objetivo = input(f"\n{nombre} ingresá el nombre de la {tipo_str[:-1]} que estás buscando: ")

        # pos es la posición donde se encontró el dato (-1 si no la encontró)
        # tiempo es cuánto tardó en encontrar el dato. Ambos valores retornar de la función
        if metodo == '1':
            pos, tiempo = busqueda_secuencial(lista, objetivo)
        elif metodo == '2':
            pos, tiempo = busqueda_binaria(lista, objetivo)

        print(f"\nResultado: {'✅ Encontrado' if pos != -1 else '❌ No encontrado'}")
        print(f"🥇 Posición: {pos+1}")
        print(f"⏱ Tiempo de ejecución: {tiempo:.6f} segundos\n")


def mostrar_metodos_ordenamiento(lista, tipo_str, nombre):
    while True:
        print(f"\n📚  Métodos de ordenamiento disponibles para {tipo_str}\n")
        print("1 - Ordenamiento por Burbuja")
        print("2 - Ordenamiento por Selección")
        print("3 - Ordenamiento por Inserción")
        print("4 - Ordenamiento por Quick Sort")
        print("0 - Volver al menú anterior")
        metodo = solicitar_opcion("\nSeleccione método de ordenamiento: ", ['0', '1', '2', '3', '4'])

        if metodo == '0':
            print(f"\n↩️  Volviendo al menú anterior.")
            break

        if metodo == '1':
            lista_ordenada, tiempo = burbuja(lista)
        elif metodo == '2':
            lista_ordenada, tiempo = seleccion(lista)
        elif metodo == '3':
            lista_ordenada, tiempo = insercion(lista)
        elif metodo == '4':
            lista_ordenada, tiempo = quick_sort(lista)

        # Aquí usamos enumerate para recorrer la lista ordenada y empezar desde 1 el conteo para mostrarla
        print(f"\n🗂 Catálogo Ordenado:")
        for i, valor in enumerate(lista_ordenada, 1):
            print(f"{i}. {valor}")

        print(f"\n⏱ Tiempo de ejecución: {tiempo:.6f} segundos\n")
