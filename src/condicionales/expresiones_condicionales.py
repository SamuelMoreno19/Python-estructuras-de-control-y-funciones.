# Aquí, la variable mensaje recibe el valor "Eres mayor de edad." si edad es mayor o igual a 18. 
# Si no, toma el valor "Eres menor de edad.". 
# Esto evita el uso de una estructura if-else más extensa.

edad = 17
mensaje = "Eres mayor de edad." if edad >= 18 else "Eres menor de edad."
print(mensaje)