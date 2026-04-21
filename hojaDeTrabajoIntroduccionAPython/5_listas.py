# Ejercicio 5a
# Crea una lista con las materias: "Cálculo", "Física", "Programación", "Álgebra"
# Luego:
#   1. Agrega "Estadística" al final
#   2. Inserta "Química" en la posición 2
#   3. Elimina "Álgebra" de la lista
#   4. Imprime la lista final y su longitud

# TU CÓDIGO AQUÍ
materia = ["Calculo","Física","Programación","Álgebra"]

materia.append("Estadística")
materia.insert(2,"Química")
materia.remove("Álgebra")
print("Lista      :", materia)
print(f"len()     : {len(materia)}")

# Ejercicio 5b
# Dada la lista de notas, imprime: mínimo, máximo, suma y promedio.
# El promedio debe mostrarse con 2 decimales usando f-string :.2f

notas = [78, 92, 65, 88, 74, 95, 61, 83]

# TU CÓDIGO AQUÍ
print (f"Mínimo : {min(notas)}")
print (f"Máximo : {max(notas)}")
print (f"Suma   : {sum(notas)}")
print (f"Promedio : {sum(notas)/len(notas):.2f}")