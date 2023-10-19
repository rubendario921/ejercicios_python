#Calcular el mayor de tres números enteros introducidos por teclado.
print("Calcular el mayor de tres números enteros introducidos por teclado.")

num1 = int(input("Por favor ingrese el primer número: "))
num2 = int(input("Por favor ingrese el segundo número: "))
num3 = int(input("Por favor ingrese el tercer número: "))

if (num1 > num2) and (num1 > num3):
    print(f"El número mayor de los valores ingresados es: {num1}")
elif (num2 > num1) and (num2 > num3):
    print(f"El número mayor de los valores ingresados es: {num2}")
else:
    print(f"El número mayor de los valores ingresados es: {num3}")
