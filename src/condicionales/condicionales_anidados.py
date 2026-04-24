""" En este ejemplo, el primer condicional verifica si la persona es mayor o igual a 18 años. Dentro de este bloque if, hay otro if que comprueba el estado civil. 
Dependiendo de ambas condiciones, 
el programa imprime un mensaje específico."""

edad = 30
estado_civil = 'soltero'

if edad >= 18:
    if estado_civil == 'casado':
        print('Eres un adulto casado.')
    else:
        print('Eres un adulto soltero.')
else:
    print('Eres menor de edad.')