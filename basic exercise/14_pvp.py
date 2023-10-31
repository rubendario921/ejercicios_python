# El dueño de una papelería desea un programa que le indique el precio de venta de un artículo dado. El precio se
# calcula de acuerdo con la siguiente fórmula: PVP = precio_coste + ganancia. Donde la ganancia será:
# • El 15% si el precio de coste es inferior USD. 3.
# • 50 céntimos si el precio de coste está entre USD: 3 y  6.
# • El 25% si el precio de coste supera los USD 6.

precio_neto = float(input("Ingrese el valor del precio neto: "))

if precio_neto < 3:
    ganancia = precio_neto * 0.15
elif precio_neto >= 3 and precio_neto <= 6:
    ganancia = 0.50
else:
    ganancia = precio_neto * 0.25

pvp = precio_neto + ganancia
print(f"El P.V.P es de: {pvp}")