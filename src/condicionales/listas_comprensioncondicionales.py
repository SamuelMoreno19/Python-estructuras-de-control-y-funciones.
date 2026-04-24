# Aquí, se crea una lista paridad que contiene "par" o "impar" según la condición aplicada a cada elemento de numeros.

numeros = [1, 2, 3, 4, 5]
paridad = ["par" if n % 2 == 0 else "impar" for n in numeros]
print(paridad)  # Salida: ['impar', 'par', 'impar', 'par', 'impar']