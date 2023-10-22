# Calcular el mayor de cuatro números enteros introducidos por teclado

print("Calcular el mayor de cuatro números enteros introducidos por teclado")

num1 = int(input("Ingrese el primero número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercero número: "))
num4 = int(input("Ingrese el cuarto número: "))

if (num1 > num2) and(num1 > num3) and (num1>num4):
    print(f"El número mayor es: {num1}") 
elif(num2>num1) and (num2>num3) and (num2>num4):
    print(f"El número mayor es: {num2}")
elif(num3>num1) and(num3>num2)and(num3>num4):
    print(f"El número mayor es: {num3}")
else:
    print(f"El número mayor es: {num4}") 