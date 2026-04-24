#La declaración else se ejecuta únicamente cuando la condición del if es falsa. 
# Esto asegura que siempre se ejecute uno de los dos bloques de código, 
# proporcionando un flujo de control claro y predecible.

contrasena = input("Introduce la contraseña: ")
if contrasena == "secreta123":
    print("Acceso concedido.")
else:
    print("Contraseña incorrecta. Acceso denegado.")