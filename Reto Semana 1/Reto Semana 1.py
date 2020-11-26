
''' Nota quices
 :Parámetros:
 codigo (str): codigo único alfanumérico del estudiante
 nota1 (int): Nota del primer quiz reto semestre (0 - 100)
 nota2 (int): Nota del segundo quiz del semestre (0 - 100)
 nota3 (int): Nota del tercer quiz del semestre (0 - 100)
 nota4 (int): Nota del cuarto quiz del semestre (0 - 100)
 nota5 (int): Nota del quinto quiz del semestre (0 - 100)
 Retorno:
 String: de la forma "El promedio ajustado del estudiante {codigo} es: {promedio}" dónde, el promedio se
calcula eliminando la peor nota y se reporta con dos decimales utilizando la escala numérica de 0 a 5
 '''


def nota_quices(codigo: str, nota1: int, nota2: int, nota3: int, nota4: int, nota5: int):
    # Elimina la nota minima
    suma = (nota1 + nota2 + nota3 + nota4 + nota5)-(min(nota1, nota2, nota3, nota4, nota5))
    # Saca y redondea el promedio
    promedio = round(((suma/4)/20), 2)
    return f"El promedio ajustado del estudiante {codigo} es: {promedio}"


nota1 = nota_quices("AA0010276", 19, 90, 38, 55, 68)
print(nota1)

nota2 = nota_quices("IS00201620", 37,10,50,19,79)
print(nota2)

nota3 = nota_quices("BIO2201810", 45,46,33,74,22)
print(nota3)

nota4 = nota_quices("IQ102201810", 57,100,87,93,21)
print(nota4)

nota5 = nota_quices("MA00201520", 5,14,76,91,5)
print(nota5)


