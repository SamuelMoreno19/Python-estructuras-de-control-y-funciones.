# Es posible agregar guardas a los patrones para refinar aún más las condiciones:
#Las guardas utilizan la palabra clave if para añadir condiciones adicionales al patrón, 
# proporcionando mayor control sobre la lógica de coincidencia.

edad = 20

match edad:
    case edad if edad < 18:
        print("Eres menor de edad.")
    case edad if edad >= 18 and edad < 65:
        print("Eres adulto.")
    case edad if edad >= 65:
        print("Eres adulto mayor.")
