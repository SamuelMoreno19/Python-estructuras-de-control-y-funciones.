"""Las comprensiones de listas son una característica poderosa de Python que permite
 crear listas de forma concisa usando la sintaxis del bucle for: """

# Crear una lista con los cuadrados de los números del 1 al 5
cuadrados = [x**2 for x in range(1, 6)]
print(cuadrados)  # [1, 4, 9, 16, 25]

# Filtrar elementos usando una condición
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]