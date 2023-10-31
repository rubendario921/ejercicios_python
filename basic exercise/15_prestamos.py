#  Una empresa de préstamos decidió cambiar su esquema de cobros así:
# • Si el préstamo es de más de 5000 euros, cobra en tres cuotas
# • Si el préstamo es de menos de 1000 euros, cobra en una cuota
# • Si el préstamo es entre 2000 y 3000 euros cobra en dos cuotas
# • En los demás casos cobra en cinco cuotas
# Adicionalmente, si es de menos de 4000 euros cobra el 12% de interés, en caso contrario cobra el 10% de interés.
# El programa debe decir en cuántas cuotas debe pagar y de  cuánto es cada cuota. Para ello, se calcula el valor total de la deuda con interés y se divide en cuotas iguales.

prestamo = int(input("Ingrese la cantidad del prestamo a financiar: "))

if prestamo >= 4000:
    interes = prestamo * 0.1
    cuotas_minimas = 3

elif prestamo > 2000 and prestamo < 3000:
    interes = prestamo * 0.12
    cuotas_minimas = 2

elif prestamo <= 1000:
    interes = prestamo * 0.12
    cuotas_minimas = 1
else:
    print("El valor ingresado es el incorrecto.")

valor_final = prestamo + interes
cuotas = valor_final / cuotas_minimas

print(f"{cuotas_minimas} Cuotas de pago con el valor de: {cuotas}")
print(f"El valor del prestamo es: {prestamo}")
print(f"El valor del interes es: {interes}")
print(f"El valor total a cancelar es de: {valor_final}")