"""En este ejemplo, el bloque else 
se ejecuta porque ningún número 
en la lista cumple la condición para ser primo,
 por lo que el bucle nunca ejecuta break."""

# Buscar un número primo en una lista
numeros = [4, 6, 8, 9, 10, 12]

for num in numeros:
    if num % 2 != 0 and num % 3 != 0:
        print(f"¡Encontrado un primo: {num}!")
        break
else:
    print("No se encontró ningún número primo en la lista")


# Comparemos con otro ejemplo donde sí se encuentra un primo:
# En este caso, el bloque else no se ejecuta 
# porque el bucle termina con break al encontrar el número 7.


numeros = [4, 6, 7, 8, 10]  # Ahora incluimos el 7

for num in numeros:
    if num % 2 != 0 and num % 3 != 0:
        print(f"¡Encontrado un primo: {num}!")
        break
else:
    print("No se encontró ningún número primo en la lista")