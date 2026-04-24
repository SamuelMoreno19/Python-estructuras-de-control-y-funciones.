# Aquí, si el saldo es suficiente para el retiro, 
# se actualiza el saldo y se informa al usuario.
#  Si no es suficiente, se notifica al usuario y se muestra el saldo actual.

saldo = 300
retiro = 500
if saldo >= retiro:
    saldo -= retiro
    print("Retiro exitoso.")
    print(f"Nuevo saldo: {saldo}")
else:
    print("Fondos insuficientes.")
    print(f"Saldo actual: {saldo}")