""" En este caso, solo se verifica la **contraseña** si el **usuario** es `'admin'`. 
Esto refleja una **jerarquía** lógica donde cierta verificación depende de un requisito previo.
También es posible anidar más de dos niveles de condicionales, aunque esto puede afectar negativamente a la legibilidad:"""

a = 5
b = 10
c = 15

if a > b:
    if a > c:
        print('a es el mayor.')
    else:
        if c > b:
            print('c es el mayor.')
        else:
            print('b es el mayor.')
else:
    if b > c:
        print('b es el mayor.')
    else:
        print('c es el mayor.')


# Este código determina cuál de las tres variables es la mayor. 
# Sin embargo, su complejidad puede dificultar su comprensión. Una alternativa más clara es:

mayor = a

if b > mayor:
    mayor = b

if c > mayor:
    mayor = c

print(f'El número mayor es {mayor}.')

