""" Esto significa que las expresiones con not se evalúan primero, luego and y finalmente or. 
Sin embargo, es una buena práctica usar paréntesis para hacer explícita la evaluación deseada y evitar confusiones."""

a = True
b = False
c = not b

resultado = a or b and c
print(resultado)  # Imprime True

# En este ejemplo, 
# la evaluación se realiza como a or (b and c). 
# Si se desea modificar el orden de evaluación, se deben utilizar paréntesis:

resultado = (a or b) and c
print(resultado)  # Imprime True