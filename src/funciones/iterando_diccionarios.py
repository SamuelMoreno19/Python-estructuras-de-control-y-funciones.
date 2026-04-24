#Al iterar sobre un diccionario, 
# por defecto se recorren sus claves:

usuario = {"nombre": "Laura", "edad": 28, "ciudad": "Madrid"}

# Iterando sobre claves
for clave in usuario:
    print(f"Clave: {clave}, Valor: {usuario[clave]}")

#También podemos 
#usar los métodos items(), keys() y values():

# Iterando sobre pares clave-valor
for clave, valor in usuario.items():
    print(f"{clave}: {valor}")

# Iterando solo sobre valores
for valor in usuario.values():
    print(valor)