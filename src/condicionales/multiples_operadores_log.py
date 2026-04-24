""" En este caso, se verifica si la persona es mayor de 18 años o si tiene al menos 16 años y cuenta con permiso parental. 
El uso de paréntesis ayuda a definir claramente las condiciones combinadas."""

edad = 17
permiso_parental = True

if (edad >= 18) or (edad >= 16 and permiso_parental):
    print("Puedes obtener la licencia de conducir.")
else:
    print("No cumples los requisitos para la licencia.")