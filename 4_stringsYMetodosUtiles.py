# Ejercicio 4a
# Dada la cadena: "  fisica y matematica  "
# Aplica los métodos para:
#   1. Quitar espacios extremos
#   2. Convertir a mayúsculas
#   3. Reemplazar "Y" por "&"
# Imprime el resultado de cada paso.

cadena = "  fisica y matematica  "

# TU CÓDIGO AQUÍ
print (f"Original    : '{cadena}'")
print (f"strip()     : '{cadena.strip()}'")
print (f"upper()     : '{cadena.upper()}'")
cambiar = cadena.replace("y","&")
print (f"replace()   :", cambiar)

# Ejercicio 4b
# Dada la cadena: "rojo-verde-azul-amarillo"
# 1. Sepárala en una lista de colores usando split()
# 2. Une la lista con " | " usando join()
# 3. Verifica con 'in' si "verde" está en la lista (imprime True/False)

colores_str = "rojo-verde-azul-amarillo"

# TU CÓDIGO AQUÍ
colores = colores_str.split("-")
print (type(colores))
print (f"split(,)    :", colores)
unir = " | ".join(colores)
print ("join(' ')   :", unir)
print (f"\a'verde' in colores: {'verde' in colores}")