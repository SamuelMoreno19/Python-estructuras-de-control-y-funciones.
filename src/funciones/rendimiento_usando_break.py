# Rendimiento: Usar break puede mejorar significativamente 
# el rendimiento al evitar iteraciones innecesarias.

# Versión ineficiente
encontrado = False
for elemento in lista_grande:
    if elemento == objetivo:
        encontrado = True
# Seguimos recorriendo toda la lista aunque ya encontramos el objetivo

# Versión eficiente
encontrado = False
for elemento in lista_grande:
    if elemento == objetivo:
        encontrado = True
        break  # Terminamos inmediatamente
