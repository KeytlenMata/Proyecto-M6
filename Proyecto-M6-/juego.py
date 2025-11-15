import random

def mostrar_bienvenida():
    ancho = 50
    print("\n" + "┈" * ancho)
    titulo = "🔥  ADIVINA EL NÚMERO SECRETO  🔥"
    print(titulo.center(ancho))
    print("┈" * ancho)
    print("""
📜 Instrucciones:
- Elige un nivel de dificultad.
- Tendrás 5 intentos para adivinar el número secreto.
- Después de cada intento, te diré si el número es mayor o menor.
- ¡Gana si adivinas el número antes de quedarte sin intentos!

🌟 ¡Buena suerte y que comience el juego! 🌟
""")
    print("─" * ancho)

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

#juego principal
def juego_numero_secreto():
    numero_secreto = random.randint(1, 10)   
    intentos = 5
    
    for i in range(intentos):
        entrada = input("Ingresa un número entre 1 y 10: ")

        if not entrada.isdigit():
            print("Debes ingresar solo números.")
            continue
        
        intento = int(entrada)

        if intento == numero_secreto:
            print("¡Ganaste!")
            return
        
        if intento > numero_secreto:
            print("El número es menor.")
        else:
            print("El número es mayor.")
        
        print("Incorrecto.")

    print("¡Perdiste!")

seleccionar_dificultad()
juego_numero_secreto()
