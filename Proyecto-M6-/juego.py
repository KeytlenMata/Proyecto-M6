import random

def mostrar_instrucciones():
    print("\n📜 INSTRUCCIONES")
    print("┈" * 60)
    print("""
- Elige un nivel de dificultad.
- Tendrás 5 intentos para adivinar el número secreto.
- Después de cada intento, sabrás si el número secreto es mayor o menor.
- ¡Gana si lo adivinas antes de quedarte sin intentos!

🌟 ¡Buena suerte y que comience el juego! 🌟
""")

def seleccionar_dificultad():
    """
    Permite al jugador elegir un nivel de dificultad para el juego.
    Devuelve una tupla con los valores (min, max) del rango de números.

    - Fácil:   1 a 10
    - Medio:   1 a 20
    - Difícil: 1 a 50
    """

    print("🎯 SELECCIONA UN NIVEL DE DIFICULTAD 🎯\n")
    print("1️⃣  Fácil   (1 - 10)")
    print("2️⃣  Medio   (1 - 20)")
    print("3️⃣  Difícil (1 - 50)")

    while True:
        opcion = input("\n👉 Ingresa tu elección (1-3): ").strip()

        if opcion == "1":
            print("\n✅ Has elegido el nivel FÁCIL.")
            return 1, 10
        elif opcion == "2":
            print("\n✅ Has elegido el nivel MEDIO.")
            return 1, 20
        elif opcion == "3":
            print("\n✅ Has elegido el nivel DIFÍCIL.")
            return 1, 50
        else:
            print("\n⚠️ Opción no válida. Intenta de nuevo (solo 1, 2 o 3).")

#juego principal
def juego_numero_secreto(n_min, n_max):
    numero_secreto = random.randint(n_min, n_max)   
    intentos = 5
    
    for i in range(intentos):
        entrada = input(f"\nIngresa un número entre {n_min} y {n_max}: ")

        if not entrada.isdigit():
            print("Debes ingresar solo números.")
            continue
        
        intento = int(entrada)

        if intento == numero_secreto:
            print("\n🎉 ¡GANASTE! 🎉\n")
            return
      
        if intento > numero_secreto:
            print("El número es menor.")
        else:
            print("El número es mayor.")
         
    print(f"\n¡PERDISTE!, El número secreto era {numero_secreto}\n")