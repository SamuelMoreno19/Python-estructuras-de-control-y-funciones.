# Las sentencias break y continue afectan 
# únicamente al bucle más interno que las contiene. 
# Para controlar bucles externos, 
# necesitarás técnicas adicionales:

for i in range(1, 4):
    print(f"Grupo {i}:")

    for j in range(1, 6):
        if j == 3:
            print("  Saltando el elemento 3")
            continue  # Solo afecta al bucle interno

        print(f"  Elemento {j}")

    print("Fin del grupo\n")

    """Si necesitas salir de múltiples bucles anidados, 
    puedes usar una bandera o variable de control:"""

    encontrado = False

for i in range(5):
    for j in range(5):
        if i * j > 10:
            print(f"Valor encontrado: {i} * {j} = {i*j}")
            encontrado = True
            break  # Sale del bucle interno

    if encontrado:
        break  # Sale del bucle externo