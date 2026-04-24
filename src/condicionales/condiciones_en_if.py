""" ### **Uso de condiciones complejas en declaraciones `if`**

Los operadores lógicos permiten escribir condiciones más compactas y claras, evitando anidar múltiples declaraciones `if`. Esto mejora la **legibilidad** y facilita el mantenimiento del código.

Ejemplo sin operadores lógicos:"""

usuario = "admin"
contrasena = "1234"

if usuario == "admin":
    if contrasena == "1234":
        print("Acceso concedido.")

# Ejemplo utilizando and:

if usuario == "admin" and contrasena == "1234":
    print("Acceso concedido.")