# Ejercicio 10a
# Escribe una función convertir_entero(valor) que intente convertir
# el parámetro a entero usando int().
#   - Si tiene éxito, retorna el entero.
#   - Si ocurre un ValueError, imprime un mensaje de error y retorna None.
#   - El bloque finally debe imprimir "[intento con: ]" siempre.
#
# Pruébala con: "42", "3.14", "hola", 100

# TU CÓDIGO AQUÍ

def convertir_entero(valor):
    try:
        resultado = int(valor)
        return resultado
    except ValueError:
        print("Error: no se puede convertir a entero")
        return None
    finally:
        print(f"[intento con: {valor}]")

print(convertir_entero("42"))
print(convertir_entero("3.14"))
print(convertir_entero("hola"))
print(convertir_entero(100))

#==================================================================================================

# Ejercicio 10b
# Escribe una función validar_edad(edad) que:
#   - Lance un TypeError  si edad no es int
#   - Lance un ValueError si edad < 0 o edad > 150
#   - Retorne True si la edad es válida
#
# Pruébala dentro de un try/except con: 25, -5, 200, "veinte"

# TU CÓDIGO AQUÍ

def validar_edad(edad):
    if not isinstance(edad, int):
        raise TypeError("La edad ingresada no es un entero")
    
    if edad < 0 or edad > 150:
        raise ValueError("La edad debe estar entre 0 y 150")
    
    return True

# Prueebas

valores = [25, -5, 200, "veinte"]

for v in valores:
    try:
        resultado = validar_edad(v)
        print(f"{v}: Edad válida -> {resultado}")
    except TypeError as te:
        print(f"{v}: Error de tipo -> {te}")
    except ValueError as ve:
        print(f"{v}: Error de valor -> {ve}")