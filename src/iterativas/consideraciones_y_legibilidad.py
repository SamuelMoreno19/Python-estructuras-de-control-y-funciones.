"""Aunque `pass` y `else` en bucles son características poderosas, es importante usarlas con moderación para mantener la legibilidad del código:

- Usa `pass` cuando quieras indicar explícitamente que "no hacer nada" es intencional
- La cláusula `else` en bucles puede ser confusa para programadores que vienen de otros lenguajes, así que considera añadir un comentario explicativo
- En equipos de desarrollo, asegúrate de que todos entiendan estas construcciones"""


# Versión más explícita con comentarios
for item in coleccion:
    if condicion(item):
        # Procesamiento normal
        procesar(item)
    else:
        pass  # Intencionalmente no hacemos nada con estos elementos
else:
    # Este bloque se ejecuta si el bucle termina normalmente (sin break)
    print("Procesamiento completado sin interrupciones")