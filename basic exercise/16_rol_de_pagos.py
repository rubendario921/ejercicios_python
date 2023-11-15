#  Calcular el salario neto de un trabajador de una empresa cuyo trabajo se paga por horas.
# Introducir por teclado el número de horas y el precio de la hora. El cálculo se realiza del siguiente modo:
# • Las primeras 35 horas de cada semana se pagan a la tarifa normal (suponer 4 semanas al mes).
# • Las horas extras se pagan un 50% más que las normales.
# • Los impuestos a deducir a los trabajadores varían en función de su sueldo mensual (considerando las horas
# extras trabajadas):
# o Si el sueldo es menor de € 600, libre de impuestos.
# o Si el sueldo está entre € 600 y € 1000, los impuestos son el 20%.
# o Si el sueldo es mayor de € 1000, el 30%.

hora_trabajadas = int(input("Ingrese las horas trabajadas: "))
valor_hora = int(input("Ingrese el valor de la hora de trabajo: "))

calculo_total = hora_trabajadas * valor_hora

if hora_trabajadas <= 35:
    valor_a_recibir = calculo_total
elif hora_trabajadas > 35:
    tarifa_suplementaria = (valor_hora * 50) / 100
    valor_a_recibir = calculo_total + tarifa_suplementaria

# Tarifas
if valor_a_recibir < 600:
    valor_total = valor_a_recibir
elif 600 <= valor_a_recibir < 1000:
    impuesto = (valor_a_recibir * 20) / 100
    valor_total = valor_a_recibir - impuesto
else:
    impuesto = (valor_a_recibir * 30) / 100
    valor_total = valor_a_recibir - impuesto

print(f"Valor Ingresos: {valor_a_recibir}")
print(f"Valor Impuestos: {impuesto}")
print(f"Valor Total: {valor_total}")
