# Ejercicio 6a
# Crea un diccionario que represente un curso con las claves:
#   "nombre", "codigo", "creditos", "activo"
# Luego:
#   1. Agrega la clave "estudiantes" con el valor 35
#   2. Imprime el valor de "creditos" usando .get()
#   3. Intenta obtener la clave "salon" con valor por defecto "Sin asignar"

# TU CÓDIGO AQUÍ
curso = {
    "nombre"   : "Programación 1",
    "codigo"   : "F12",
    "creditos" : 4,
    "activo"   : True
    }

# Modificar y agregar entradas
curso["estudiantes"] = 35

# Imprimir valores
print ("créditos:", curso.get("creditos"))

# Obtener clave "salon"
print ("Salón:", curso.get("salon","sin asignar"))



# Ejercicio 6b
# Itera sobre el diccionario del ejercicio anterior e imprime
# cada clave y su valor en el formato:  clave     : valor
# (usa f-string con alineación, ej: f"{clave:12} : {valor}")

# TU CÓDIGO AQUÍ
print ("Iteación del diccionario")
for clave, valor in curso.items():
    print (f"{clave:12} : {valor}")
