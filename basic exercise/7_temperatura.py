# Determinar en que estado está el agua en función de su temperatura. Si es negativa el estado será sólido, si es  
# menor que 100 será líquido y si es mayor que 100 será gas. Pedir al usuario el valor de la temperatura. 

print("Determinar en que estado está el agua en función de su temperatura. Si es negativa el estado será sólido, si es menor que 100 será líquido y si es mayor que 100 será gas. Pedir al usuario el valor de la temperatura.")

valorTemp= int(input("Ingrese el valor de la temperatura: "))

if (valorTemp <0):
    print("El estado del agua es: SOLIDO")
elif(valorTemp <100):
    print("El estado del agua es: LIQUIDO")
elif(valorTemp>100):
    print("El estado del agua es: GAS")
