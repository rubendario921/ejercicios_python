#Un año es bisiesto si es divisible por 4 y no es por 100, o si es divisible por 400. Escribe un programa que lea un año y devuelva si es bisiesto o no. 

print("Un año es bisiesto si es divisible por 4 y no es por 100, o si es divisible por 400. Escribe un programa que lea un año y devuelva si es bisiesto o no. ")

anio = int(input("Ingrese el año a valorar: "))

if ((anio%4== 0 and anio %200 != 0)or (anio%400==0)):
    print ("El año ingresado es bisiesto")
else:
    print ("El año ingresado no es bisiesto")