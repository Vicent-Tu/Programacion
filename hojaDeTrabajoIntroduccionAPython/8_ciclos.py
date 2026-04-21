# Ejercicio 8a
# Usa un for con enumerate() para imprimir la siguiente lista de planetas
# numerados desde 1.
# Salida esperada:
#   [1] Mercurio
#   [2] Venus
#   ...

planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]

# TU CÓDIGO AQUÍ
for i, planeta in enumerate(planetas,start=1):
    print (f"{i} {planeta}")

# Ejercicio 8b
# Usa un ciclo while para imprimir la tabla de multiplicar del 7
# (del 7x1 hasta el 7x10).
# Formato:  7 x 1 = 7

# TU CÓDIGO AQUÍ
print("\n TABLA DEL 7")
i = 1
while i<11:
    print(f"7 x {i} = {7*i}")
    i += 1


# Ejercicio 8c — List comprehension
# En una sola línea, crea las siguientes listas y luego imprímelas:
#   1. Los cubos de los números del 1 al 8  (x³)
#   2. Los números del 1 al 30 que sean divisibles por 3 pero NO por 9

# TU CÓDIGO AQUÍ

print("\nCUBOS DE NUMEROS")
for i in range(1,9):
    print(f"{i}³ = {i**3}")

print ("\nDIVISBLES POR TRES")
a = 1
while a<=30:
    if a % 9 == 0:
        a += 1
        continue
    elif a % 3 == 0:
        print(f"{a}")
        a += 1
    else:
        a += 1
        continue




print([i for i in range(1, 31) if i % 9 != 0 and i % 3 == 0])
