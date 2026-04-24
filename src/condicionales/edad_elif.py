""" En este ejemplo, utilizamos comparaciones encadenadas para determinar el rango de la edad. 
Si la condición 18 <= edad < 65 es verdadera, 
se considera adulto y se imprime el mensaje correspondiente."""

edad = 45

if edad < 18:
    print("Eres menor de edad.")
elif 18 <= edad < 65:
    print("Eres adulto.")
else:
    print("Eres mayor de 65 años.")