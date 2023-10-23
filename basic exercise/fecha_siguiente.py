# Dada la fecha de hoy, calcular la fecha del día siguiente. Suponer que el año no es bisiesto. 
print("Dada la fecha de hoy, calcular la fecha del día siguiente. Suponer que el año no es bisiesto. ")

dia = int(input("Ingrese el dia actual: "))
mes = int(input("Ingrese el mes actual: "))
anio = int(input("Ingrese el anio actual: "))

dias_en_mes = 0

#Verificar el número de días en el mes actual

if (mes == 2):
    dias_en_mes = 28
elif mes in [4,6,9,11]:
    dias_en_mes =30
else:
    dias_en_mes=31

#Calcular la fecha del día
if dia<dias_en_mes:
    dia_siguiente = dia +1
    mes_siguiente = mes
else:
    dia_siguiente = 1
    if mes < 12:
        mes_siguiente = mes +1
    else:
        mes_siguiente= 1
        anio += 1
print(f"La fecha del día siguiente es: {dia_siguiente}/{mes_siguiente}/{anio}")