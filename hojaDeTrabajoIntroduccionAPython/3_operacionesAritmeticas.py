# Ejercicio 3a
# Dados a=23 y b=7, calcula e imprime:
#   - La división entera de a entre b
#   - El residuo (módulo) de a entre b
#   - a elevado a la potencia b (solo los primeros dígitos, usa f-string)

a, b = 23, 7

# TU CÓDIGO AQUÍ
print (f"{a} + {b}         = {a + b}")
print (f"{a} // {b}        = {a // b}")
print (f"{a} % {b}         = {a % b}")
print (f"{a} ** {b}        = {str(a ** b)[:5]}")
 
# Ejercicio 3b
# Usa el módulo math para calcular:
#   1. La raíz cuadrada de 144
#   2. El techo (ceil) de 7.3
#   3. El piso (floor) de 7.9
#   4. El valor de pi redondeado a 4 decimales (usa :.4f en el f-string)

import math

# TU CÓDIGO AQUÍ
print (f"sqrt(144)      = {math.sqrt(144)}")
print (f"math.ceil(7.3) = {math.ceil(7.3)}")
print (f"math.flor(7.9) = {math.floor(7.9)}")
print (f"math.pi        = {math.pi:.4f}")