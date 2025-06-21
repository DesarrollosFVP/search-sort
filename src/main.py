from data.movies import peliculas
from data.series import series
from menu import menu

if __name__ == "__main__":
    nombre = input("👤 Ingrese su nombre: ").strip().capitalize()
    print(f"\n👋 Hola {nombre}!\n")
    menu(peliculas, series, nombre)
