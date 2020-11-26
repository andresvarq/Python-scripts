# Ejercicio 1
def TerminaEnCuatro (numero: int):
    numero2 = numero - 4
    if (numero2 == 0) or ((numero2 / 10) == int(numero2 / 10)):
        resultado = f'{numero} termina en 4'
    else:
        resultado = f'{numero} no termina en 4'
    return resultado



#ejercicio 2
def TieneTres (numero: int):
    if (numero > 99) and (numero < 1000):
        resultado = True
    else:
        resultado = False
    return resultado



# Ejercicio 3
def AmbosSonPar (numero: int):
    decena = int(numero / 10)
    if (numero / 2) == int(numero / 2):
        if (decena / int(decena / 2)) == 2:
            resultado = True
        else:
            resultado = False
    else:
        resultado = False
    return resultado



#Ejercicio 4
def EsPrimo (numero:int):
    if (numero < 20) and (numero > 9):
        if (numero / 2) == int(numero / 2):
            if numero == 2:
                resultado = True
            else:
                resultado = False
        else:
            if (numero / 3) == int(numero / 3):
                if numero == 3:
                    resultado = True
                else:
                    resultado = False
            else:
                if (numero / 5) == int(numero / 5):
                    #code
                    if numero == 5:
                        resultado = True
                    else:
                        resultado = False
                else:
                    if (numero / 7) == int(numero / 7):
                        if numero == 7:
                            resultado = True
                        else:
                            resultado = False
                    else:
                        resultado = True
    else:
        resultado = 'El número no cumple con las condiciones'
    return resultado



#Ejercicio 5
def TambienEsPrimo (numero: int):
    if numero > 0: #positivos
        if (numero < 100) and (numero > 9):
            if (numero / 2) == int(numero / 2):
                if numero == 2:
                    resultado = 'Número es positivo y primo'
                else:
                    resultado = 'Número es positivo'
            else:
                if (numero / 3) == int(numero / 3):
                    if numero == 3:
                        resultado = 'Número es positivo y primo'
                    else:
                        resultado = 'Número es positivo'
                else:
                    if (numero / 5) == int(numero / 5):
                        if numero == 5:
                            resultado = 'Número es positivo y primo'
                        else:
                            resultado = 'Número es positivo'
                    else:
                        if (numero / 7) == int(numero / 7):
                            if numero == 7:
                                resultado = 'Número es positivo y primo'
                            else:
                                    resultado = 'Número es positivo'
                        else:
                            resultado = 'Número es positivo y primo'
        else:
            resultado = 'El número no cumple con las condiciones'
    else: #negativos
        if (numero > -100) and (numero < -9):
            if (numero / 2) == int(numero / 2):
                if numero == 2:
                    resultado = 'Número es negativo y primo'
                else:
                    resultado = 'Número es negativo'
            else:
                if (numero / 3) == int(numero / 3):
                    if numero == 3:
                        resultado = 'Número es negativo y primo'
                    else:
                        resultado = 'Número es negativo'
                else:
                    if (numero / 5) == int(numero / 5):
                        if numero == 5:
                            resultado = 'Número es negativo y primo'
                        else:
                            resultado = 'Número es negativo'
                    else:
                        if (numero / 7) == int(numero / 7):
                            if numero == 7:
                                resultado = 'Número es negativo y primo'
                            else:
                                    resultado = 'Número es negativo'
                        else:
                            resultado = 'Número es negativo y primo'
        else:
            resultado = 'El número no cumple con las condiciones'
    return resultado



#Ejercico 6
def SonIguales (numero:int):
    if (numero < 100) and (numero > 9):
        decena = int(numero / 10)
        unidad = numero - (decena * 10)
        if unidad == decena:
            resultado = True
        else:
            resultado = False
    else:
        resultado = 'Número no cumple con las condiciones'
    return resultado



#Ejercicio 7
def EsMayor (numero1: int, numero2: int):
    if numero1 < numero2:
        resultado = f'{numero2} es mayor que {numero1}'
    else:
        resultado = f'{numero1} es mayor que {numero2}'
    return resultado



#Ejercicio 8
def sumados (num1: int, num2: int):
    if (num1 < 100) and (num1 > 9):
        dec1 = int(num1 / 10)
        uni1 = num1 - (dec1 * 10)
        if (num2 < 100) and (num2 > 9):
            dec2 = int(num2 / 10)
            uni2 = num2 - (dec2 * 10)
            resultado = dec1 + dec2 + uni1 + uni2
        else:
            resultado = 'Números no cumplen con las condiciones'
    else:
        resultado = 'Números no cumplen con las condiciones'
    return resultado



#Ejercicio 9
def MayorDig (num: int):
    if (num < 1000) and (num > 99):
        cent = int(num / 100)
        dec = int((num - (cent * 100)) / 10)
        uni = num - (cent * 100) - (dec * 10)
        if (uni > dec) and (uni > cent):
            resultado = 'Mayor número está en las unidades'
        else:
            if (dec > uni) and (dec > cent):
                resultado = 'Mayor número está en las decenas'
            else:
                resultado = 'Mayor número está en las centenas'
    else:
        resultado = 'Número no cumple con las condiciones'
    return resultado



#Ejercicio 10
def EsMulti (num: int):
    cent = int(num / 100)
    dec = int((num - (cent * 100)) / 10)
    uni = num - (cent * 100) - (dec * 10)
    if (num < 1000) and (num > 99):
        if (cent / dec) == int(cent / dec):
            resultado = f'{cent} es multiplo de {dec}'
        else:
            if (dec / cent) == int(dec / cent):
                resultado = f'{dec} es multiplo de {cent}'
            else:
                if (cent / uni) == int(cent / uni):
                    resultado = f'{cent} es multiplo de {uni}'
                else:
                    if (uni / cent) == int(uni / cent):
                        resultado = f'{uni} es multiplo de {cent}'
                    else:
                        if (dec / uni) == int(dec / uni):
                            resultado = f'{dec} es multiplo de {uni}'
                        else:
                            if (uni / dec) == int(uni / dec):
                                resultado = f'{uni} es multiplo de {dec}'
                            else:
                                resultado = 'Ningún dígito es múltiplo del otro'
    else:
        resultado = 'Número no válido'
    return resultado



#Ejercicio 11
def sumados2 (num1: int, num2: int, num3: int):
    dec1 = int(num1 / 10)
    uni1 = num1 - (dec1 * 10)
    dec2 = int(num2 / 10)
    uni2 = num2 - (dec2 * 10)
    dec3 = int(num3 / 10)
    uni3 = num3 - (dec3 * 10)
    if ((num1 < 100) and (num1 > 9)) and ((num2 < 100) and (num2 > 9)) and ((num3 < 100) and (num3 > 9)):
        if dec1 < uni1:
            maj1 = uni1
        elif dec1 == uni1:
            maj1 = uni1
        else:
            maj1 = dec1
        if dec2 < uni2:
            maj2 = uni2
        elif dec2 == uni2:
            maj2 = uni2
        else:
            maj2 = dec2
        if dec3 < uni3:
            maj3 = uni3
        elif dec3 == uni3:
            maj3 = uni3
        else:
            maj3 = dec3

        if maj1 > maj2:
            if maj1 > maj3:
                resultado = f'El mayor dígito es {maj1}, está en {num1}'
            elif maj1 == maj3:
                resultado = f'El mayor dígito es {maj1}, está en {num1} y {num3}'
            else:
                resultado = f'El mayor dígito {maj3}, está en {num3}'
        elif maj1 == maj2:
            if maj1 > maj3:
                resultado = f'El mayor dígito es {maj1}, está en {num1} y {num2}'
            elif maj1 == maj3:
                resultado = f'El mayor dígito es {maj1}, está en {num1}, {num2} y {num3}'
            else:
                resultado = f'El mayor dígito es {maj3}, está en {num3}'
        else:
            if maj2 > maj3:
                resultado = f'El mayor dígito es {maj2}, está en {num2}'
            elif maj2 == maj3:
                resultado = f'El mayor dígito es {maj2}, está en {num2} y {num3}'
            else:
                resultado = f'El mayor es {maj3}, dígito está en {num3}'
    else:
        resultado = 'Números no cumplen la condición'
    return resultado



#Ejercicio 12
def suma (num1: int, num2: int, num3: int):
    if (num1 + num2) == num3:
        resultado = f'{num1} + {num2} es igual a {num3}'
    else:
        if (num2 + num3) == num1:
            resultado = f'{num2} + {num3} es igual a {num1}'
        else:
            if (num1 + num3) == num2:
                resultado = f'{num1} + {num3} es igual a {num2}'
            else:
                resultado = 'Ninguno de los números es la suma de los otros 2'
    return resultado



#Ejercicio 13
def OtraVezPrimos (numero: int):
    if (numero < 50) and (numero > 0):
        if (numero / 2) == int(numero / 2):
            if numero == 2:
                resultado = 'Número es positivo y primo'
            else:
                resultado = 'Número es positivo'
        else:
            if (numero / 3) == int(numero / 3):
                if numero == 3:
                    resultado = 'Número es positivo y primo'
                else:
                    resultado = 'Número es positivo'
            else:
                if (numero / 5) == int(numero / 5):
                    if numero == 5:
                        resultado = 'Número es positivo y primo'
                    else:
                        resultado = 'Número es positivo'
                else:
                    if (numero / 7) == int(numero / 7):
                        if numero == 7:
                            resultado = 'Número es positivo y primo'
                        else:
                                resultado = 'Número es positivo'
                    else:
                        resultado = 'Número es positivo y primo'
    else:
        resultado = f'{numero} no cumple con las condiciones'
    return resultado



#Ejercicio 14
def OtraVezIguales (num: int):
    if ((num < 10000) and (num > 999)) or ((num > -10000) and (num < -999)):
        mil = int(num / 1000)
        cent = int((num - (mil * 1000)) / 100)
        dec = int((num - (cent * 100) - (mil * 1000)) / 10)
        if cent == dec:
            resultado = True
        else:
            resultado = False
    else:
        resultado = f'{num} no cumple con las condiciones'
    return resultado



#Ejercicio 15
def PorSiete (num: int):
    if (num / 7) == int(num / 7):
        resultado = True
    else:
        resultado = False
    return resultado



#Ejercicio 16
def CuantosDigitos (num: int):
    if (num < 1000) and (num > -1000):
        if (num < -99) or (num > 99):
            resultado = f'{num} tiene tres dígitos'
        else:
            if (num <-9) or (num > 9):
                resultado = f'{num} tiene dos dígitos'
            else:
                resultado = f'{num} tiene un dígito'
    else:
        resultado = f'{num} no cumple con las condiciones'
    return resultado



#Ejercicio 17
def espar (num: int):
    if (num < 10000) and (num > 999):
        mil = int(num / 1000)
        cent = int((num - (mil * 1000)) / 100)
        dec = int((num - (cent * 100) - (mil * 1000)) / 10)
        uni = num - (mil * 1000) - (cent * 100) - (dec * 10)
        if mil % 2 == 0: #mil es par
            if cent % 2 == 0: #cent es par
                if dec % 2 == 0: #dec es par
                    if uni % 2 == 0: #uni es par
                        resultado = 'Todos los digitos son pares'
                    else: #uni es inpar
                        resultado = 'Hay tres dígitos pares y un inpar'
                else:#dec es inpar
                    if uni % 2 == 0: #uni es par
                        resultado = 'Hay tres dígitos pares y un inpar'
                    else: #uni es inpar
                        resultado = 'Hay dos dígitos pares y dos inpares'
            else: #cent es inpar
                if dec % 2 == 0: #dec es par
                    if uni % 2 == 0: #uni es par
                        resultado = 'Hay tres dígitos pares y un inpar'
                    else: #uni es inpar
                        resultado = 'Hay dos dígitos pares y dos inpares'
                else:#dec es inpar
                    if uni % 2 == 0: #uni es par
                        resultado = 'Hay dos dígitos pares y dos inpares'
                    else: #uni es inpar
                        resultado = 'Hay tres dígitos inpares y un par'
        else: #mil es inpar
            if cent % 2 == 0: #cent es par
                if dec % 2 == 0: #dec es par
                    if uni % 2 == 0: #uni es par
                        resultado = 'Hay tres dígitos pares y un inpar'
                    else: #uni es inpar
                        resultado = 'Hay dos dígitos pares y dos inpares'
                else:#dec es inpar
                    if uni % 2 == 0: #uni es par
                        resultado = 'Hay dos dígitos pares y dos inpares'
                    else: #uni es inpar
                        resultado = 'Hay tres dígitos inpares y un par'
            else: #cent es inpar
                if dec % 2 == 0: #dec es par
                    if uni % 2 == 0: #uni es par
                        resultado = 'Hay dos dígitos pares y dos inpares'
                    else: #uni es inpar
                        resultado = 'Hay tres dígitos inpares y un par'
                else:#dec es inpar
                    if uni % 2 == 0: #uni es par
                        resultado = 'Hay tres dígitos inpares y un par'
                    else: #uni es inpar
                        resultado = 'Todos los digitos son inpares'
    else:
        resultado = f'{num} no cumple con las condiciones'
    return resultado



#Ejercicio 18
#Incompleto
def mismofin(num1: int, num2: int, num3: int):
    pass

#Ejercicio 19
def salario (hora_trabajada: int, tarifa: float):
    resultado = hora_trabajada * tarifa
    if (hora_trabajada < 0) or (tarifa < 0):
        resultado = 'Algo no está bien'
    else:
        if hora_trabajada > 40:
            tarifa = (tarifa * 1.5) * (hora_trabajada - 40)
    return tarifa

print(salario(16, 2000))
print(salario(50, 20))