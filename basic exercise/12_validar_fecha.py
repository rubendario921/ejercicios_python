# Solicitar al usuario una fecha (dd:mm:aaaa) y comprobar si es correcta. Para que una fecha sea correcta es necesario:
# • El año debe ser mayor que cero.
# • El mes debe estar entre 1 y 12.
# • Dependiendo del mes que sea, el día debe estar dentro de los límites válidos. Los meses que tienen 31 días
# son 1, 3, 5, 7, 8, 10 y 12. Los meses de 30 días son 4, 6, 9 y 11. El mes de 28 días es 2, excepto en un año
# bisiesto que es 29 días. */

def validar_fecha(dia, mes, anio):
    if anio <= 0:
        return False
    
    if mes < 1 or mes > 12:
        return False
    
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        if dia < 1 or dia > 31:
            return False
    elif mes in [4, 6, 9, 11]:
        if dia < 1 or dia > 30:
            return False
    elif mes == 2:
        if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
            if dia < 1 or dia > 29:
                return False
        else:
            if dia < 1 or dia > 28:
                return False
    
    return True

dia = int(input('Ingrese el día: '))
mes = int(input('Ingrese el mes: '))
anio = int(input('Ingrese el año: '))

if validar_fecha(dia, mes, anio):
    print('La fecha es correcta.')
else:
    print('La fecha es incorrecta.')
