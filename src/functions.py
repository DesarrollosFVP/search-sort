def mostrar_listado_completo(lista, tipo_str, nombre):
    print(f"👉 La lista tiene {len(lista)} {tipo_str}.\n")
    print(f"\n📃 Listado completo de {tipo_str}:")
    print("------------------------------------\n")
    

    for i, valor in enumerate(lista, 1):
        print(f"{i}. {valor}")
