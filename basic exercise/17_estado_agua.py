#Determinar en que estado está el agua en función de su temperatura. Si es negativa el estado será sólido, si es 
#menor que 100 será líquido y si es mayor que 100 será gas. Pedir al usuario el valor de la temperatura.

print("Ejercicio Calcular el estado del agua")

nombreUsuario = input("Ingrese su nombre: ")

while True:
    try:
        temperatura = int(input("Ingrese la temperatura del agua: "))
        if temperatura <0:
            print(f"{nombreUsuario} El agua está en estado Solido.")
        elif temperatura <100:
            print(f"{nombreUsuario} El agua está en estado Líquido.")
        else:
            print(f"{nombreUsuario} El agua está en estado gaseoso.")
    except ValueError:
        print(f"{nombreUsuario} Por favor, ingrese un valor numérico valido para la temperatura.")
        continue

    respuesta = input(f"{nombreUsuario} ¿Desea ingresar otro valor (s/n)?").lower()
    if respuesta != 's':
        print(f"{nombreUsuario} Gracias por visitarnos")
        break