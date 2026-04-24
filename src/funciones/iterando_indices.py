#A veces necesitamos acceder tanto a los elementos como a sus posiciones.
#  Para esto podemos combinar range() con la longitud de la secuencia:

nombres = ["Ana", "Carlos", "Elena"]
for i in range(len(nombres)):
    print(f"Posición {i}: {nombres[i]}")

    """Una alternativa más elegante es usar la función enumerate(), que devuelve pares de índice y valor:"""

    nombres = ["Ana", "Carlos", "Elena"]
for indice, nombre in enumerate(nombres):
    print(f"Posición {indice}: {nombre}")