# Ejercicio 9a
# Escribe una función convertir_temperatura(grados, escala="C") que convierta:
#   - Si escala="C"  → convierte Celsius a Fahrenheit: F = C * 9/5 + 32
#   - Si escala="F"  → convierte Fahrenheit a Celsius: C = (F - 32) * 5/9
#
# Pruébala con: 100°C, 0°C, 32°F y 212°F

# TU CÓDIGO AQUÍ
grados = float(input("Ingrese temperatura:"))
escala = input("¿Son graods Fahrenheit(F) o es Celsius(C)?:").lower()

def convertir_temperatura(grados,escala):
    """La función dada converte los grados en una escala Celsius a Fahrenheit"""

    """Args: 
            grados (float): los grados Celsius a converitr
            escala (str)  : especifica el nombre de la escala.

        Returns: Retorna los grados a escala Fahrenheit.
            """
    if escala == "f":
        return f"{(grados -32) * 5/9} Celsius"
    elif escala == "c":
        return  f"{grados * 1.8 +32} Fahrenheit"
    else:
        return "Escala incorrecta, intentelo de nuevo"

print (convertir_temperatura(grados,escala))



#===========================================================================================


# Ejercicio 9b
# Escribe una función resumen_lista(lista) que retorne
# tres valores: (minimo, maximo, promedio).
# Úsala con: [12, 45, 7, 89, 34, 56, 23]
# Imprime los tres resultados usando desempaquetado.

# TU CÓDIGO AQUÍ
def resumen_lista(lista): 
    """Calcula estadísticas básicas de una lista dada.
    
        Args:
            Lista (list): contiene el listado de los datos a evaluar
            
        Returns:
            tuple: (mínimo, máximo, promedio)
            """
    return min(lista), max(lista), sum(lista) / len(lista)

datos = [12,45,7,89,34,56,23]
minimo, maximo, promedio = resumen_lista(datos)

print(f"Datos    : {datos}")
print(f"Mínimo   : {minimo}")
print(f"Máximo   : {maximo}")
print(f"Promedio : {promedio:.2f}")



#================================================================================================



# Ejercicio 9c — Recursión
# Escribe una función recursiva fibonacci(n) que retorne
# el n-ésimo número de la sucesión de Fibonacci.
# Casos base: fibonacci(0)=0, fibonacci(1)=1
# Caso recursivo: fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
#
# Imprime los primeros 10 números: fibonacci(0) ... fibonacci(9)

# TU CÓDIGO AQUÍ
def fibonacci(n):
    """Cacula la sucesión del n-ésimo número de Fibonacci
    
        Args:
            n (int): es el n-ésimo número de la sucesión de Fibonacci

        
        Returns: la sucesión de fibonacci
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

for n in list(range(9)):
    print(fibonacci(n))