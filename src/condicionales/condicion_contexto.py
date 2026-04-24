#Sin embargo, en algunos casos, los condicionales anidados son necesarios, 
# especialmente cuando una condición solo debe evaluarse dentro del contexto de otra. Por ejemplo:

usuario = 'admin'
contrasena = '1234'

if usuario == 'admin':
    if contrasena == '1234':
        print('Acceso concedido.')
    else:
        print('Contraseña incorrecta.')
else:
    print('Usuario no reconocido.')