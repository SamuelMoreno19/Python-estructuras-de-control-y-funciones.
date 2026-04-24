# Filtrado de datos: 
# Procesar solo los elementos que cumplen cierta condición.

temperaturas = [22, -5, 28, 31, -15, 19, 26, -8]

print("Temperaturas positivas:")
for temp in temperaturas:
    if temp <= 0:
        continue

    print(f"{temp}°C")