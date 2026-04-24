# En este caso, si acceso_permitido es verdadero, la variable acceso_registrado no se evaluará debido al cortocircuito del operador or. 
# Si es necesario que acceso_registrado se evalue siempre, debemos reorganizar el código:

acceso_registrado = True

acceso_permitido = False

if acceso_permitido or acceso_registrado:
    print("Acceso concedido.")

   
