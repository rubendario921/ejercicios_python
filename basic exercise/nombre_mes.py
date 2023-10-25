# Pedir un mes (número) y mostrar el nombre del mes. 
import calendar
print("Pedir un mes (número) y mostrar el nombre del mes.")
mes_numero = int(input("Ingresa cualquier nùmero del mes: "))
nombre_mes = calendar.month_name[mes_numero]

print(f"El nombre del mes es: {nombre_mes}")
