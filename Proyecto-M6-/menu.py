import juego


def mostrar_menu():
    print("\n" + "=" * 40)
    print("              MENU PRINCIPAL")
    print("=" * 40)
    print("1. Jugar")
    print("2. Instrucciones")
    print("3. Salir")
    print("=" * 40)

def main_menu():
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
            print("\nSaliendo del programa. Hasta luego.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


main_menu()
