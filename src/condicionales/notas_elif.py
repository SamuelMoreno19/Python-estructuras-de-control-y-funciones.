""" Aquí, el programa asigna una calificación en función del rango en el que se encuentre la nota. Si nota es 87, 
cumple la condición nota >= 80, 
por lo que imprime "Calificación: Notable" y no evalúa las siguientes condiciones."""

nota = 87

if nota >= 90:
    print("Calificación: Sobresaliente")
elif nota >= 80:
    print("Calificación: Notable")
elif nota >= 70:
    print("Calificación: Aprobado")
else:
    print("Calificación: Suspenso")
    