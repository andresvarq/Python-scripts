# Ejercicio 1
def convertir_i_f (numero:int):
    return float(numero)
print(convertir_i_f(25))
print(convertir_i_f(33))


# Ejercicio 2
def convertir_f_i (numero:float):
    return int(numero)
print(convertir_f_i(56.3))
print(convertir_f_i(48.65))


# Ejercicio 3
def suma_min_max(*numero:float):
    return f'{min(numero) + max(numero)}'
print(suma_min_max(4, 56, 68.3, 7))
print(suma_min_max(58.75, 88, 1, 99, 34, 102.8, 0.2))


# Ejercicio 4
def hola_mundo (var1:str = 'Hola', var2:str = 'mundo'):
    return f'{var1} {var2}'


# Ejercicio 5
def suma_dc (numero:float, numero2:float):
    inte = int(numero)
    dec = numero - inte
    inte2 = int(numero2)
    dec2 = numero2 - inte2
    return dec + dec2


# Ejercicio 6
r = float(input('Cual es el radio de la circunferencia? '))

def perimetro_c (r:float):
    return 2*3.1416*r

def area_c (r:float):
    return 3.1416*(r**2)

p = perimetro_c(r)
a = area_c(r)
print(f'Para una circunferencia con radio {r}, el perimetro es {p} y el área es {a}')


# Ejercicio 7
num1 = float(input('Primer número '))
num2 = float(input('Segundo número '))

def suma (num1, num2):
    return num1 + num2
suma = suma(num1, num2)

def resta (num1, num2):
    return num1 - num2
resta = resta(num1, num2)

def multip (num1, num2):
    return num1 * num2
multip = multip(num1, num2)

def divis(num1, num2):
    return num1 / num2
divis = divis(num1, num2)

print(f'La suma es {suma}, la resta es {resta}, la multiplicación {multip} y la division {divis}')


# Ejercicio 8
a = float(input('Primer lado '))
b = float(input('Segundo lado '))
c = float(input('Tercer lado '))

def area_t (a, b, c):
    s = (a + b + c) / 2
    return (s*(s-a)*(s-b)*(s-c))**(1/2)
areat = area_t(a, b, c)

print(f'El area del triangulo es {areat}')
