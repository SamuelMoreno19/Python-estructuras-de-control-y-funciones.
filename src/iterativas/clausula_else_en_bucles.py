"""Una característica única de Python es la posibilidad de 
añadir una cláusula else a los bucles for y while. 
Esta cláusula se ejecuta una sola vez 
después de que el bucle haya terminado normalmente 
(es decir, sin que se haya ejecutado un break)."""

# Ejemplo de sintaxis válida con for-else
secuencia = [1, 2, 3]

for elemento in secuencia:
    # Cuerpo del bucle (necesita contenido)
    print(f"Procesando: {elemento}")
else:
    # Se ejecuta al terminar la secuencia completa
    print("El bucle terminó normalmente.")


# O en los bucles while:

condicion = False # Definimos la variable para que no de error

while condicion:
    pass  # Indica que el bloque existe, aunque esté vacío
else:
    pass  # Lo mismo aquí