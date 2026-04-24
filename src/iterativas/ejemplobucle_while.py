# Por ejemplo, para solicitar entrada 
# al usuario hasta que proporcione un valor válido:

entrada = ""
while not entrada.isdigit():
    entrada = input("Introduce un número: ")

print(f"Has introducido el número: {entrada}")

