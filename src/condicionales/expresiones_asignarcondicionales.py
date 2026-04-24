# En este caso, si edad es menor que 18, categoria es "Menor"; 
# si no, se evalúa la siguiente expresión condicional para determinar si es "Joven Adulto" o "Adulto".

edad = 20
categoria = "Menor" if edad < 18 else ("Joven Adulto" if edad < 30 else "Adulto")
print(categoria)