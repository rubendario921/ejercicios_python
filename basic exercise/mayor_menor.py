#Calcular el mayor y menor de dos números enteros introducidos por teclado.
print("Calcular el mayor y el menor de dos números enteros introducidos por teclado.")

num1 = int(input("Por favor, ingrese el primer número: "))
num2 = int(input("Por favor, ingrese el segundo número: "))

if num1 > num2:
    print(f"El número {num1} es mayor")
    print(f"El número {num2} es menor")
else:
    print(f"El número {num2} es mayor")
    print(f"El número {num1} es menor")
