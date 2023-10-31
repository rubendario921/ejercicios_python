# Solicitar al usuario la inicial del día de la semana y mostrar el nombre del día completo. La letra inicial puede ser mayúscula o minúscula. Usar la x para el miércoles.
import calendar

print("Solicitar al usuario la inicial del día de la semana y mostrar el nombre del día completo. La letra inicial puede ser mayúscula o minúscula. Usar la x para el miércoles.")

inicial_dia = input("Ingrese la inicial del día de la semana: ").lower()

dias = {'l': 0, 'm': 1, 'x': 2, 'j': 3, 'v': 4, 's': 5, 'd': 6}
numero_dia = dias[inicial_dia]

nombre_dia = calendar.day_name[numero_dia]

print(f"El dia de la semana es: {nombre_dia}")
