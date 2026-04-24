"""La sentencia `pass` es un operador que **no hace nada**. 
Funciona como un marcador de posición cuando necesitas 
sintácticamente una instrucción, 
pero no quieres ejecutar ningún código.
 Es especialmente útil en situaciones donde:

- Necesitas crear un bucle vacío
- Estás desarrollando código incrementalmente
- Quieres implementar un patrón de "no operación" explícito"""

# Bucle que no hace nada para los números pares
for numero in range(1, 10):
    if numero % 2 == 0:
        pass  # No hacemos nada con los números pares
    else:
        print(f"Procesando número impar: {numero}")



"""pass es una instrucción real que el intérprete de Python 
ejecuta (aunque no realiza ninguna operación). 
Esto lo hace útil como marcador de posición 
en código que estás desarrollando:"""

def procesar_datos():
    # Función aún no implementada
    pass

# El programa puede seguir ejecutándose sin errores
procesar_datos()

# En bucles, pass puede servir 
# para crear estructuras que se activarán condicionalmente:

modo_debug = False

for i in range(100):
    # En modo normal, no mostramos nada durante el procesamiento
    if not modo_debug:
        pass
    else:
        print(f"Procesando iteración {i}")

    # Código de procesamiento real aquí