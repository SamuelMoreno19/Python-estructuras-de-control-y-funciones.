# En este caso, si divisor es cero, 
# el mensaje "División por cero no permitida" se asigna a resultado, evitando así un error de división entre cero.

dividendo = 10
divisor = 0
resultado = dividendo / divisor if divisor != 0 else "División por cero no permitida"
print(resultado)