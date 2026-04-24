"""Al trabajar con bucles `while`, es importante asegurarse de que:

- La **condición de salida** sea alcanzable
- Las **variables de control** se actualicen correctamente
- No se produzcan **bucles infinitos** no deseados

Por ejemplo, este código contiene un error que causa un bucle infinito:"""

# ¡CUIDADO! Bucle infinito
contador = 1
while contador <= 5:
    print(contador)
    # Olvidamos incrementar contador

# La versión corregida sería:

contador = 1
while contador <= 5:
    print(contador)
    contador += 1  # Importante: actualizar la variable de control