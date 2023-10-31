# Escribir un programa que solicite un valor entero al usuario y determine si es par o impar. 
num = int(input("Por favor, ingrese un número entero: "))

if num %2 ==0:
    print(f"El número {num} es par.")
else:
    print(f"El número {num} es impar.")