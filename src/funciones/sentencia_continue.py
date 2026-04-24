"""continue salta únicamente la iteración actual y pasa a la siguiente. Es como decir "ignora 
el resto de esta vuelta y continúa con la siguiente."""

for numero in range(1, 11):
    if numero % 2 == 0:  # Si el número es par
        continue  # Saltamos a la siguiente iteración

    print(f"Número impar: {numero}")