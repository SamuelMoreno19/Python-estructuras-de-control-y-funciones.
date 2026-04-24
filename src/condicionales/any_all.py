# En este caso, any() no evalúa todos los elementos una vez que encuentra 1.

numeros = [0, 0, 1, 0]

if any(numeros):
    print("Al menos un número es no cero.")

    # Con all(), la evaluación se detiene al encontrar un valor falso:

    condiciones = [True, True, False, True]

if all(condiciones):
    print("Todas las condiciones son verdaderas.")
else:
    print("Al menos una condición es falsa.")