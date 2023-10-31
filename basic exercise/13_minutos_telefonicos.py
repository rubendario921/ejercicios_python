# Escribir un programa que permita determinar la cantidad total a pagar por una llamada telefónica de N minutos (introducido por el usuario), teniendo en cuenta lo siguiente: 
# • Las llamadas de 5 minutos o menos tienen un coste de 10 USD.
# • Cada minuto adicional a partir de los 5 primeros cuesta 2 USD.

minutos = int(input("Ingrese los minutos conversados: "))

if minutos>5:
    adicional = minutos - 5
    valor_a_pagar= ((5*10)+(adicional*2))
else:
    valor_a_pagar= (minutos*10)

print(f"El valor a cancelar es: ${valor_a_pagar}")