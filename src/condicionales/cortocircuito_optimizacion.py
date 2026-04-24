""" Aquí, si condicion_a es falsa, Python no evalúa condicion_b, ya que el resultado del operador and será necesariamente falso. 
Esto puede ahorrar tiempo de ejecución, especialmente si condicion_b es una operación costosa o compleja."""

if condicion_a and condicion_b:
    """ Código a ejecutar si ambas condiciones son verdaderas """

    """ En este caso, si condicion_a es verdadera, Python no evalúa condicion_b, dado que el resultado de or ya es verdadero. 
    La evaluación de cortocircuito permite evitar evaluaciones innecesarias y potenciales errores en condicion_b."""

    if condicion_a or condicion_b:
     """Código a ejecutar si al menos una condición es verdadera"""