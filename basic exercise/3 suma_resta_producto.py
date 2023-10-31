# . Pedir al usuario un valor. Si el valor es positivo, pedir un segundo valor y calcular la suma, resta y producto de ambos. Mostrar los resultados por pantalla.
print("Calculadora Basica")
print(
    "Recomendaciones: El primer número debe ser positivo, caso contrario se finaliza el programa. "
)

num1 = int(input("Por favor, ingrese el primer número: "))

if num1 > 0:
    num2 = int(input("Ingrese el segundo número: "))

    suma = num1 + num2
    resta = num1 - num2
    producto = num1 * num2

    print(f"El valor de la suma es: {suma}")
    print(f"El valor de la resta es: {resta}")
    print(f"El valor de la producto es: {producto}")

else:
    print("El número ingresado es el incorrecto")