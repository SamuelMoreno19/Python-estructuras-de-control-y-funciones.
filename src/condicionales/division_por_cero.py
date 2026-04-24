# Aquí, si divisor es cero, 
# la primera condición divisor != 0 es falsa, y Python no evalúa dividendo / divisor > 1, evitando un ZeroDivisionError.

dividendo = 10
divisor = 0

if divisor != 0 and dividendo / divisor > 1:
    print("El resultado de la división es mayor que 1.")
else:
    print("No es posible dividir entre cero.")