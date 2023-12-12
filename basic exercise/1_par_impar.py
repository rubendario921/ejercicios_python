# Escribir un programa que solicite un valor entero al usuario y determine si es par o impar.
while True:
    try:
        num = int(input("Por favor, ingrese un número entero: "))
        if num % 2 == 0:
            print(f"El número {num} es par.")
        else:
            print(f"El número {num} es impar.")
    except ValueError:
        valor_incorrecto = input("Por favor ingrese un valor correcto.")
        print(f"El valor ingresado {valor_incorrecto} es incorrecto.")
        continue
    respuesta = input("¿Desea ingresar otro valor? (s/n): ").lower()
    if respuesta != "s":
        print("Muchas Gracias")
        break
