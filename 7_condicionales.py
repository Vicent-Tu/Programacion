# Ejercicio 7a
# Escribe una función llamada clasificar_imc(imc) que reciba el
# Índice de Masa Corporal y retorne una cadena según esta escala:
#   < 18.5  → "Bajo peso"
#   18.5–24.9 → "Normal"
#   25–29.9 → "Sobrepeso"
#   >= 30   → "Obesidad"
#
# Pruébala con los valores: 16.0, 22.5, 27.3, 31.8

# TU CÓDIGO AQUÍ
#El programa dado como datos el indice corporal de una persona, determina uno de los cuatro estados posibles:
def clasificar_imc(imc):
	if imc < 18.5:
		return "Bajo Peso"
	elif imc  <= 24.9:
		return "Peso Normal"
	elif imc <= 29.9:
		return "Sobrepeso"
	else:
		return "Obesidad"

for imc in [16.0,22.5,27.3,31.8]:
	print (f"Imc {imc}: {clasificar_imc(imc)}")

# Ejercicio 7b
# Usa el operador ternario para determinar si un número es par o impar.
# Pruébalo con los números 4, 7 y 0.
# Salida esperada:  4 es par  /  7 es impar  /  0 es par

# TU CÓDIGO AQUÍ
x = 0
estado = "es par" if x % 2 == 0 else "es impar"
print (f"{x} {estado}")