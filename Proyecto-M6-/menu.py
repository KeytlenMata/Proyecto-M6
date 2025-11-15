import juego

def mostrar_titulo():
    print("=" * 60)
    ancho = 60
    titulo = "🔥  A D I V I N A   E L   N Ú M E R O   S E C R E T O  🔥"
    print(titulo.center(ancho))

def mostrar_menu():
    ancho = 60
    print("=" * ancho)
    print("\n" + "MENU PRINCIPAL".center(ancho) + "\n")
    print("1. Jugar")
    print("2. Instrucciones")
    print("3. Salir")
    print("=" * ancho)

def main_menu():
    mostrar_titulo()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ").strip()

        if opcion == "1":
            print("\nIniciando el juego...")
            n_min, n_max = juego.seleccionar_dificultad()
            juego.juego_numero_secreto(n_min, n_max)
            input("Presiona Enter para continuar...")


        elif opcion == "2":
            juego.mostrar_instrucciones()
            input("Presiona Enter para continuar...")

        elif opcion == "3":
            print("\nSaliendo del programa. Hasta luego.\n")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


main_menu()
