# Imagina break como un "botón de emergencia" que te permite 
# escapar de un bucle cuando se cumple cierta condición:

for numero in range(1, 11):
    if numero == 5:
        print("¡Encontrado el 5! Saliendo del bucle...")
        break
    print(f"Número actual: {numero}")

print("Bucle terminado")

