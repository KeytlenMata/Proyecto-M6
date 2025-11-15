def seleccionar_dificultad():
    """
    Permite al jugador elegir un nivel de dificultad para el juego.
    Devuelve una tupla con los valores (min, max) del rango de números.

    - Fácil:   1 a 10
    - Medio:   1 a 20
    - Difícil: 1 a 50
    """

    print("🎯 SELECCIONA UN NIVEL DE DIFICULTAD 🎯")
    print("1️⃣  Fácil (1 - 10)")
    print("2️⃣  Medio (1 - 20)")
    print("3️⃣  Difícil (1 - 50)")

    while True:
        opcion = input("👉 Ingresa tu elección (1-3): ").strip()

        if opcion == "1":
            print("✅ Has elegido el nivel FÁCIL.")
            return 1, 10
        elif opcion == "2":
            print("✅ Has elegido el nivel MEDIO.")
            return 1, 20
        elif opcion == "3":
            print("✅ Has elegido el nivel DIFÍCIL.")
            return 1, 50
        else:
            print("⚠️ Opción no válida. Intenta de nuevo (solo 1, 2 o 3).")
