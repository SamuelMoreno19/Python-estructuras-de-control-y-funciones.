"""Un bucle infinito es aquel que, en principio, no tiene una condición de salida natural. Se implementa 
con while True: y generalmente incluye una condición de salida explícita 
usando break:"""

while True:
    respuesta = input("¿Quieres continuar? (s/n): ").lower()

    if respuesta == "n":
        print("Programa finalizado.")
        break

    if respuesta == "s":
        print("Continuando...")
    else:
        print("Respuesta no válida. Introduce 's' o 'n'.")