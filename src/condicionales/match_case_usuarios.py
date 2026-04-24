""" La declaración match-case también admite patrones anidados y la desestructuración de datos. 
Por ejemplo, al manejar una lista de diccionarios:"""

usuarios = [
    {"nombre": "Ana", "rol": "admin"},
    {"nombre": "Luis", "rol": "usuario"},
    {"nombre": "Marta", "rol": "moderador"}
]

for usuario in usuarios:
    match usuario:
        case {"rol": "admin"}:
            print(f"{usuario['nombre']} tiene permisos de administrador.")
        case {"rol": "moderador"}:
            print(f"{usuario['nombre']} puede moderar contenidos.")
        case {"rol": "usuario"}:
            print(f"{usuario['nombre']} es un usuario regular.")
        case _:
            print(f"Rol de {usuario['nombre']} desconocido.")