# Fundamentos de Python - Control de Flujo y Funciones

Este repositorio contiene ejercicios prácticos sobre los conceptos fundamentales de Python, enfocados en **condicionales**, **funciones** e **iterativas** (bucles).

## Tabla de Contenidos

- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Cómo Ejecutar los Ejercicios](#cómo-ejecutar-los-ejercicios)
- [Ejercicios - Condicionales](#ejercicios---condicionales)
- [Ejercicios - Funciones](#ejercicios---funciones)
- [Ejercicios - Iterativas (Bucles)](#ejercicios---iterativas-bucles)

---

## Estructura del Proyecto

```
fundamentos_python_control_fun/
├── README.md
└── src/
    ├── condicionales/       # Ejercicios sobre if, elif, else y match-case
    ├── funciones/          # Ejercicios sobre funciones y parámetros
    └── iterativas/         # Ejercicios sobre bucles (for, while, etc.)
```

---

## Requisitos

- **Python 3.8+** (se recomienda 3.10+ para soporte completo de `match-case`)
- Cualquier editor de texto o IDE (VS Code, PyCharm, etc.)

### Verificar la instalación de Python:

```bash
python --version
# o
python3 --version
```

---

## Cómo Ejecutar los Ejercicios

### Opción 1: Ejecutar desde línea de comandos

```bash
# Navegar a la carpeta del proyecto
cd fundamentos_python_control_fun

# Ejecutar un archivo específico
python src/condicionales/if.py
python src/funciones/funcion_basica.py
python src/iterativas/bucles_for.py
```

### Opción 2: Ejecutar desde un IDE

1. Abre la carpeta del proyecto en tu IDE favorito
2. Navega al archivo que deseas ejecutar
3. Usa el botón "Run" o atajo de teclado (F5 en VS Code, Shift+F10 en PyCharm)

### Opción 3: Ejecución interactiva en Python

```bash
python
>>> exec(open('src/condicionales/if.py').read())
```

---

## Ejercicios - Condicionales

Los ejercicios de **condicionales** cubren sentencias `if`, `elif`, `else`, operadores lógicos y `match-case`.

### Ubicación: `src/condicionales/`

| Archivo | Descripción | Cómo ejecutar |
|---------|-------------|--------------|
| `if.py` | Estructura básica del condicional `if` | `python src/condicionales/if.py` |
| `if_else.py` | Uso de `if` y `else` | `python src/condicionales/if_else.py` |
| `elif.py` | Múltiples condiciones con `elif` | `python src/condicionales/elif.py` |
| `edad_elif.py` | Ejemplo práctico: validación de edad | `python src/condicionales/edad_elif.py` |
| `notas_elif.py` | Ejemplo práctico: calificación de notas | `python src/condicionales/notas_elif.py` |
| `numero.py` | Clasificación de números positivos/negativos/cero | `python src/condicionales/numero.py` |
| `hora.py` | Validación de horas | `python src/condicionales/hora.py` |
| `temperatura.py` | Ejemplo práctico: clasificación de temperatura | `python src/condicionales/temperatura.py` |
| `color_elif.py` | Ejemplo práctico: clasificación de colores | `python src/condicionales/color_elif.py` |
| `fondos.py` | Ejemplo práctico: cálculo de fondos | `python src/condicionales/fondos.py` |
| `operador_logico.py` | Operadores lógicos (`and`, `or`) | `python src/condicionales/operador_logico.py` |
| `operador_not.py` | Operador de negación `not` | `python src/condicionales/operador_not.py` |
| `operador_dia.py` | Operadores con días de la semana | `python src/condicionales/operador_dia.py` |
| `multiples_operadores_log.py` | Combinación de múltiples operadores lógicos | `python src/condicionales/multiples_operadores_log.py` |
| `precedencia_operadores.py` | Precedencia de operadores lógicos | `python src/condicionales/precedencia_operadores.py` |
| `cortocircuito_optimizacion.py` | Evaluación de cortocircuito (short-circuit) | `python src/condicionales/cortocircuito_optimizacion.py` |
| `any_all.py` | Funciones `any()` y `all()` para múltiples condiciones | `python src/condicionales/any_all.py` |
| `condicion_contexto.py` | Condiciones según contexto | `python src/condicionales/condicion_contexto.py` |
| `condiciones_en_if.py` | Diferentes tipos de condiciones en `if` | `python src/condicionales/condiciones_en_if.py` |
| `division_por_cero.py` | Prevención de error de división por cero | `python src/condicionales/division_por_cero.py` |
| `prevenir_errores.py` | Prevención de errores generales | `python src/condicionales/prevenir_errores.py` |
| `contraseña.py` | Validación de contraseña | `python src/condicionales/contraseña.py` |
| `condicionales_anidados.py` | Condicionales anidados básicos | `python src/condicionales/condicionales_anidados.py` |
| `anidar_condicionales.py` | Estructura y práctica de condicionales anidados | `python src/condicionales/anidar_condicionales.py` |
| `anidados_permiso_padres.py` | Ejemplo: sistema de permisos anidados | `python src/condicionales/anidados_permiso_padres.py` |
| `claridad_permiso_padres.py` | Mejora de claridad en lógica de permisos | `python src/condicionales/claridad_permiso_padres.py` |
| `expresion_condicional.py` | Expresiones condicionales (ternarias) | `python src/condicionales/expresion_condicional.py` |
| `expresiones_condicionales.py` | Múltiples usos de expresiones condicionales | `python src/condicionales/expresiones_condicionales.py` |
| `asignacion_expresionescondicional.py` | Asignación con expresiones condicionales | `python src/condicionales/asignacion_expresionescondicional.py` |
| `expresiones_asignarcondicionales.py` | Expresiones condicionales en asignaciones | `python src/condicionales/expresiones_asignarcondicionales.py` |
| `enfoque_de_expresioncondicional.py` | Enfoques diferentes para expresiones condicionales | `python src/condicionales/enfoque_de_expresioncondicional.py` |
| `listas_comprensioncondicionales.py` | Comprensiones de listas con condicionales | `python src/condicionales/listas_comprensioncondicionales.py` |
| `match_case.py` | Introducción a `match-case` (Switch case en Python 3.10+) | `python src/condicionales/match_case.py` |
| `match_numeros.py` | `match-case` con números | `python src/condicionales/match_case_numeros.py` |
| `match_usuarios.py` | `match-case` con tipos de usuarios | `python src/condicionales/match_case_usuarios.py` |
| `match_edad.py` | `match-case` para clasificar edades | `python src/condicionales/match_edad.py` |
| `match_punto.py` | `match-case` con patrones geométricos | `python src/condicionales/match_punto.py` |
| `evaluacionen_condicionales.py` | Evaluación de expresiones en condicionales | `python src/condicionales/evaluacionen_condicionales.py` |
| `efectos_secundarios.py` | Efectos secundarios en condicionales | `python src/condicionales/efectos_secundarios.py` |
| `separar_variable_secundarios.py` | Separación de variables para evitar efectos secundarios | `python src/condicionales/separar_variable_secundarios.py` |
| `optimizacion_rendimiento.py` | Optimización de rendimiento en condicionales | `python src/condicionales/optimizacion_rendimiento.py` |

---

## Ejercicios - Funciones

Los ejercicios de **funciones** cubren definición de funciones, parámetros, argumentos, retorno, docstrings y buenas prácticas.

### Ubicación: `src/funciones/`

| Archivo | Descripción | Cómo ejecutar |
|---------|-------------|--------------|
| `funcion_basica.py` | Definición básica de una función | `python src/funciones/funcion_basica.py` |
| `funciones.py` | Conceptos generales de funciones | `python src/funciones/funciones.py` |
| `funcion_booleana.py` | Funciones que retornan valores booleanos | `python src/funciones/funcion_booleana.py` |
| `parametros_argumentos.py` | Diferencia entre parámetros y argumentos | `python src/funciones/parametros_argumentos.py` |
| `parametros_posicionales.py` | Parámetros posicionales | `python src/funciones/parametros_posicionales.py` |
| `argumentos_posicionales_variables.py` | Argumentos posicionales con longitud variable | `python src/funciones/argumentos_posicionales_variables.py` |
| `parametros_por_nombre.py` | Parámetros pasados por nombre (keyword arguments) | `python src/funciones/parametros_por_nombre.py` |
| `argumento_nombre_variables.py` | Variables con nombre como argumentos | `python src/funciones/argumento_nombre_variables.py` |
| `parametros_valores_predeterminados.py` | Parámetros con valores predeterminados | `python src/funciones/parametros_valores_predeterminados.py` |
| `combinando_parametros.py` | Combinación de diferentes tipos de parámetros | `python src/funciones/combinando_parametros.py` |
| `return.py` | Uso básico de `return` | `python src/funciones/return.py` |
| `return_anticipado.py` | Retorno anticipado de funciones | `python src/funciones/return_anticipado.py` |
| `retorno_multiples_valores.py` | Retorno de múltiples valores | `python src/funciones/retorno_multiples_valores.py` |
| `funciones_sin_return.py` | Funciones sin instrucción `return` explícita | `python src/funciones/funciones_sin_return.py` |
| `buenas_practicas_return.py` | Buenas prácticas en uso de `return` | `python src/funciones/buenas_practicas_return.py` |
| `docstrings.py` | Introducción a docstrings | `python src/funciones/docstrings.py` |
| `estructura_docstring.py` | Estructura correcta de docstrings | `python src/funciones/estructura_docstring.py` |
| `docstring_funciones_simples.py` | Docstrings en funciones simples | `python src/funciones/docstring_funciones_simples.py` |
| `docstring_comportamiento_especial.py` | Docstrings para comportamientos especiales | `python src/funciones/docstring_comportamiento_especial.py` |
| `funcion_docstring_completa.py` | Función con docstring completo | `python src/funciones/funcion_docstring_completa.py` |
| `accediendo_docstring.py` | Acceso a docstrings via `__doc__` | `python src/funciones/accediendo_docstring.py` |
| `herramientas_docstring.py` | Herramientas para trabajar con docstrings (help, etc.) | `python src/funciones/herramientas_docstring.py` |
| `estilos_docstring.py` | Diferentes estilos de docstrings (Google, NumPy, etc.) | `python src/funciones/estilos_docstring.py` |
| `buenas_practicas_docstring.py` | Buenas prácticas en docstrings | `python src/funciones/buenas_practicas_docstring.py` |
| `calculos_procesamiento.py` | Funciones para cálculos y procesamiento | `python src/funciones/calculos_procesamiento.py` |
| `transformacion_de_datos.py` | Funciones de transformación de datos | `python src/funciones/transformacion_de_datos.py` |
| `estructuras_de_datos.py` | Funciones trabajando con estructuras de datos | `python src/funciones/estructuras_de_datos.py` |
| `conversion_temperatura.py` | Ejemplo: conversión de temperatura | `python src/funciones/conversion_temperatura.py` |
| `ejemplo_calcular_area_rectangulo.py` | Ejemplo: cálculo de área de rectángulo | `python src/funciones/ejemplo_calcular_area_rectangulo.py` |
| `practica_funcion_formatear_texto.py` | Práctica: función para formatear texto | `python src/funciones/practica_funcion_formatear_texto.py` |
| `validacion_argumentos.py` | Validación de argumentos en funciones | `python src/funciones/validacion_argumentos.py` |

---

## Ejercicios - Iterativas (Bucles)

Los ejercicios de **iterativas** cubren bucles `for`, `while`, `break`, `continue`, `else` y patrones avanzados.

### Ubicación: `src/iterativas/`

| Archivo | Descripción | Cómo ejecutar |
|---------|-------------|--------------|
| `bucles_for.py` | Introducción a bucles `for` | `python src/iterativas/bucles_for.py` |
| `bucle_for_anidado.py` | Bucles `for` anidados | `python src/iterativas/bucle_for_anidado.py` |
| `ejemplos_range.py` | Función `range()` y sus usos | `python src/iterativas/ejemplos_range.py` |
| `funcion_range.py` | Función `range()` en detalle | `python src/iterativas/funcion_range.py` |
| `iterando_indices.py` | Iteración con índices | `python src/iterativas/iterando_indices.py` |
| `iterando_cadenas.py` | Iteración sobre cadenas de caracteres | `python src/iterativas/iterando_cadenas.py` |
| `iterando_diccionarios.py` | Iteración sobre diccionarios | `python src/iterativas/iterando_diccionarios.py` |
| `bucles_anidados.py` | Bucles anidados avanzados | `python src/iterativas/bucles_anidados.py` |
| `bucle_while.py` | Introducción a bucles `while` | `python src/iterativas/bucle_while.py` |
| `ejemplobucle_while.py` | Ejemplos prácticos de `while` | `python src/iterativas/ejemplobucle_while.py` |
| `patrones_con_while.py` | Patrones comunes con `while` | `python src/iterativas/patrones_con_while.py` |
| `procesar_datoscon_while.py` | Procesamiento de datos con `while` | `python src/iterativas/procesar_datoscon_while.py` |
| `comparacion_con_bucles_for.py` | Comparación entre `for` y `while` | `python src/iterativas/comparacion_con_bucles_for.py` |
| `bucle_condicionsalida_variable.py` | Control de salida con variables en `while` | `python src/iterativas/bucle_condicionsalida_variable.py` |
| `validacion_con_while.py` | Validación de entrada con `while` | `python src/iterativas/validacion_con_while.py` |
| `validacion_con_else.py` | Validación usando `else` en bucles | `python src/iterativas/validacion_con_else.py` |
| `validacion_entraday_salida_break.py` | Validación con entrada/salida y `break` | `python src/iterativas/validacion_entraday_salida_break.py` |
| `validacion_de_datos_continue.py` | Validación de datos con `continue` | `python src/iterativas/validacion_de_datos_continue.py` |
| `sentencia_break.py` | Introducción a `break` | `python src/iterativas/sentencia_break.py` |
| `sentencia_continue.py` | Introducción a `continue` | `python src/iterativas/sentencia_continue.py` |
| `busqueda_eficiente_break.py` | Búsqueda eficiente usando `break` | `python src/iterativas/busqueda_eficiente_break.py` |
| `busqueda_con_else.py` | Búsqueda usando `else` en bucles | `python src/iterativas/busqueda_con_else.py` |
| `optimizar_algoritmos_break.py` | Optimización de algoritmos con `break` | `python src/iterativas/optimizar_algoritmos_break.py` |
| `rendimiento_usando_break.py` | Mejora de rendimiento con `break` | `python src/iterativas/rendimiento_usando_break.py` |
| `combinacion_break_y_continue.py` | Combinación de `break` y `continue` | `python src/iterativas/combinacion_break_y_continue.py` |
| `casos_practicos.py` | Casos prácticos de `break` y `continue` | `python src/iterativas/casos_practicos.py` |
| `casos_especiales_continue.py` | Casos especiales con `continue` | `python src/iterativas/casos_especiales_continue.py` |
| `filtrado_de_datos_continue.py` | Filtrado de datos con `continue` | `python src/iterativas/filtrado_de_datos_continue.py` |
| `clausula_else_en_bucles.py` | Cláusula `else` en bucles `for` y `while` | `python src/iterativas/clausula_else_en_bucles.py` |
| `ejecucion_del_else.py` | Cuándo se ejecuta `else` en bucles | `python src/iterativas/ejecucion_del_else.py` |
| `pass_y_else.py` | Sentencia `pass` y `else` en bucles | `python src/iterativas/pass_y_else.py` |
| `pass_y_else_en_bucles.py` | Uso combinado de `pass` y `else` | `python src/iterativas/pass_y_else_en_bucles.py` |
| `uso_en_bucles_while.py` | Uso de `else` en bucles `while` | `python src/iterativas/uso_en_bucles_while.py` |
| `bucles_infinitos_controlados.py` | Control de bucles infinitos | `python src/iterativas/bucles_infinitos_controlados.py` |
| `bucles_por_eventos.py` | Bucles controlados por eventos | `python src/iterativas/bucles_por_eventos.py` |
| `simulaciones_y_aproximaciones.py` | Simulaciones y aproximaciones con bucles | `python src/iterativas/simulaciones_y_aproximaciones.py` |
| `compresiones_con_for.py` | Comprensiones de listas con `for` | `python src/iterativas/compresiones_con_for.py` |
| `rendimiento_con_while.py` | Consideraciones de rendimiento con `while` | `python src/iterativas/rendimiento_con_while.py` |
| `rendimiento_y_legibilidad.py` | Balance entre rendimiento y legibilidad | `python src/iterativas/rendimiento_y_legibilidad.py` |
| `consideraciones_y_legibilidad.py` | Consideraciones generales de legibilidad | `python src/iterativas/consideraciones_y_legibilidad.py` |
| `ejemplos_practicos_avazandos.py` | Ejemplos prácticos avanzados | `python src/iterativas/ejemplos_practicos_avazandos.py` |
| `ejemplointegrador_sistema_validacion.py` | Ejemplo integrador: sistema de validación | `python src/iterativas/ejemplointegrador_sistema_validacion.py` |

---

## Guía Rápida de Ejecución

### Ejecutar un ejercicio específico:
```bash
python src/condicionales/if.py
```

### Ejecutar todos los ejercicios de una categoría:
```bash
# Todos los ejercicios de condicionales
for archivo in src/condicionales/*.py; do
    echo "Ejecutando $archivo..."
    python "$archivo"
done
```

### En PowerShell (Windows):
```powershell
# Ejecutar un archivo específico
python src/condicionales/if.py

# Ejecutar todos los ejercicios de una categoría
Get-ChildItem src/condicionales/*.py | ForEach-Object {
    Write-Host "Ejecutando $_..."
    python $_
}
```

### En Python interactivo:
```bash
python
>>> import sys
>>> sys.path.append('src')
>>> exec(open('src/condicionales/if.py').read())
```

---

## Notas Importantes

1. **Python 3.10+**: Los ejercicios con `match-case` requieren Python 3.10 o superior
2. **Entrada interactiva**: Algunos ejercicios pueden pedir entrada del usuario. Si necesitas automatizar, puedes usar redirección de entrada
3. **Errores esperados**: Algunos ejercicios pueden mostrar errores deliberadamente para ilustrar conceptos

---

## Consejos para el Aprendizaje

1. **Comenzar por orden**: Es recomendable empezar con condicionales, luego funciones, luego iterativas
2. **Experimentar**: Modifica los ejercicios y observa los resultados
3. **Combinación de conceptos**: Los ejercicios posteriores combinan conceptos de ejercicios anteriores
4. **Docstrings**: Lee los docstrings de las funciones para entender mejor el código

---

## Estructura Recomendada para Aprender

```
Día 1-2: Condicionales básicos
├── if.py → if_else.py → elif.py
├── operador_logico.py → operador_not.py
└── condicionales_anidados.py

Día 3-4: Funciones
├── funcion_basica.py → parametros_argumentos.py
├── return.py → retorno_multiples_valores.py
└── docstrings.py → buenas_practicas_docstring.py

Día 5-6: Bucles
├── bucles_for.py → bucle_while.py
├── sentencia_break.py → sentencia_continue.py
└── clausula_else_en_bucles.py → ejemplointegrador_sistema_validacion.py

Día 7: Integración
└── Ejercicios avanzados que combinan todos los conceptos
```

---

## Solución de Problemas

### Error: `ModuleNotFoundError: No module named 'src'`
```bash
# Asegúrate de ejecutar desde la carpeta raíz del proyecto
cd fundamentos_python_control_fun
python src/condicionales/if.py
```

### Error: `SyntaxError` en `match-case`
```bash
# Asegúrate de usar Python 3.10 o superior
python3.10 --version
# O instala la última versión de Python
```

### El script no produce salida
Algunos scripts pueden estar esperando entrada interactiva. Intenta:
```bash
echo "20" | python src/condicionales/edad_elif.py
```
