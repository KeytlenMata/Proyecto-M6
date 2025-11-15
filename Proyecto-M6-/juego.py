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

    import random

#juego principal
def juego_numero_secreto():
    numero_secreto = random.randint(1, 10)   
    intentos = 5

    for i in range(intentos):
        entrada = input("Ingresa un número entre 1 y 10: ")

        
        if not entrada.isdigit():
            print(" Debes ingresar solo números.")
            continue

        intento = int(entrada)

        
        if intento == numero_secreto:
            return True  
        else:
            print("Incorrecto")

    return False 
