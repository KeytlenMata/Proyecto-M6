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

    