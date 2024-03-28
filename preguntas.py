"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------
 
Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    import csv

    # Inicializa la suma
    suma = 0

    # Abre el archivo CSV en modo lectura
    with open('data.csv', newline='') as csvfile:
        # Crea un objeto lector de CSV con espacio como delimitador
        csv_reader = csv.reader(csvfile, delimiter='\t')
        
        # Itera sobre cada fila en el archivo CSV
        for row in csv_reader:
            # Suma el valor de la segunda columna a la suma acumulada
            suma += int(row[1])  # Suponiendo que la segunda columna está en el índice 1

    # Retorna el resultado
    return suma
  


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

import csv
from collections import defaultdict

def contar_letras(csv_file):
    # Crear un diccionario para almacenar la frecuencia de cada letra
    frecuencia_letras = defaultdict(int)

    # Abrir el archivo CSV y leerlo
    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        # Iterar sobre cada fila del archivo
        for row in csv_reader:
            # Obtener el primer elemento de cada fila (primera columna)
            letra = row[0]
            # Incrementar la frecuencia de la letra en el diccionario
            frecuencia_letras[letra] += 1

    # Convertir el diccionario en una lista de duplas (letra, frecuencia)
    lista_duplas = list(frecuencia_letras.items())
    # Ordenar la lista de duplas alfabéticamente por la letra
    lista_duplas.sort(key=lambda x: x[0])

    return lista_duplas

# if __name__ == "__main__":
#     archivo_csv = 'data.csv'
#     frecuencia_letras = contar_letras(archivo_csv)
#     for letra, frecuencia in frecuencia_letras:
#         print(f'("{letra}", {frecuencia})')



def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

import csv
from collections import defaultdict

def sumar_numeros_por_letra(csv_file):
    # Crear un diccionario para almacenar la suma de los números por letra
    suma_numeros_por_letra = defaultdict(int)

    # Abrir el archivo CSV y leerlo
    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        # Iterar sobre cada fila del archivo
        for row in csv_reader:
            # Obtener la letra de la primera columna y el número de la segunda columna
            letra = row[0]
            numero = int(row[1])
            # Sumar el número a la suma correspondiente a la letra en el diccionario
            suma_numeros_por_letra[letra] += numero

    # Convertir el diccionario en una lista de duplas (letra, suma de números)
    lista_duplas = list(suma_numeros_por_letra.items())
    # Ordenar la lista de duplas alfabéticamente por la letra
    lista_duplas.sort(key=lambda x: x[0])

    return lista_duplas

# if __name__ == "__main__":
#     archivo_csv = 'data.csv'
#     suma_numeros = sumar_numeros_por_letra(archivo_csv)
#     for letra, suma in suma_numeros:
#         print(f'("{letra}", {suma})')



def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """

import csv
from collections import defaultdict
from datetime import datetime

def contar_registros_por_mes(csv_file):
    # Crear un diccionario para almacenar la cantidad de registros por mes
    registros_por_mes = defaultdict(int)

    # Abrir el archivo CSV y leerlo
    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        # Iterar sobre cada fila del archivo
        for row in csv_reader:
            # Obtener la fecha de la tercera columna y extraer el mes
            fecha = row[2]
            mes = fecha.split('-')[1]  # Extraer el mes como una cadena
            # Incrementar la cantidad de registros para ese mes
            registros_por_mes[mes] += 1

    # Convertir el diccionario en una lista de duplas (mes, cantidad de registros)
    lista_duplas = list(registros_por_mes.items())
    # Ordenar la lista de duplas por el mes
    lista_duplas.sort(key=lambda x: x[0])

    return lista_duplas

# if __name__ == "__main__":
#     archivo_csv = 'data.csv'
#     cantidad_registros_por_mes = contar_registros_por_mes(archivo_csv)
#     for mes, cantidad in cantidad_registros_por_mes:
#         print(f'("{mes}", {cantidad})')



def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """

import csv
from collections import defaultdict

def obtener_maximo_minimo_ordenado_por_letra(csv_file):
    # Crear un diccionario para almacenar los números correspondientes a cada letra
    numeros_por_letra = defaultdict(list)

    # Abrir el archivo CSV y leerlo
    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        # Iterar sobre cada fila del archivo
        for row in csv_reader:
            # Obtener la letra de la primera columna y el número de la segunda columna
            letra = row[0]
            numero = int(row[1])
            # Agregar el número a la lista correspondiente a la letra en el diccionario
            numeros_por_letra[letra].append(numero)

    # Crear una lista de tuplas (letra, número máximo, número mínimo)
    resultado = []
    for letra in sorted(numeros_por_letra.keys()):
        numeros = numeros_por_letra[letra]
        maximo = max(numeros)
        minimo = min(numeros)
        resultado.append((letra, maximo, minimo))

    return resultado

# if __name__ == "__main__":
#     archivo_csv = 'data.csv'
#     max_min_ordenado = obtener_maximo_minimo_ordenado_por_letra(archivo_csv)
#     for letra, maximo, minimo in max_min_ordenado:
#         print(f'("{letra}", {maximo}, {minimo})')



def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """

import csv
from collections import defaultdict

def obtener_min_max_valores_por_clave(csv_file):
    # Crear un diccionario para almacenar los valores asociados a cada clave
    valores_por_clave = defaultdict(list)

    # Abrir el archivo CSV y leerlo
    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        # Iterar sobre cada fila del archivo
        for row in csv_reader:
            # Obtener el diccionario codificado de la quinta columna
            diccionario_codificado = row[4]
            # Decodificar el diccionario
            diccionario_decodificado = dict(item.split(':') for item in diccionario_codificado.split(','))
            # Agregar los valores a la lista correspondiente a cada clave en el diccionario
            for clave, valor in diccionario_decodificado.items():
                valores_por_clave[clave].append(int(valor))

    # Crear una lista de tuplas (clave, valor mínimo, valor máximo) ordenada alfabéticamente por clave
    resultado = []
    for clave in sorted(valores_por_clave.keys()):
        valores = valores_por_clave[clave]
        minimo = min(valores)
        maximo = max(valores)
        resultado.append((clave, minimo, maximo))

    return resultado

# if __name__ == "__main__":
#     archivo_csv = 'data.csv'
#     min_max_por_clave = obtener_min_max_valores_por_clave(archivo_csv)
#     for clave, minimo, maximo in min_max_por_clave:
#         print(f'("{clave}", {minimo}, {maximo})')



def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """

import csv
from collections import defaultdict

def agrupar_letras_por_valor_columna2(csv_file):
    # Crear un diccionario para almacenar las letras asociadas a cada valor de la columna 2
    letras_por_valor = defaultdict(list)

    # Abrir el archivo CSV y leerlo
    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        # Iterar sobre cada fila del archivo
        for row in csv_reader:
            # Obtener la letra de la primera columna y el valor de la segunda columna
            letra = row[0]
            valor = int(row[1])
            # Agregar la letra a la lista correspondiente al valor en el diccionario
            letras_por_valor[valor].append(letra)

    # Crear una lista de tuplas (valor, lista de letras asociadas) ordenada por valor
    resultado = [(valor, letras) for valor, letras in sorted(letras_por_valor.items())]

    return resultado

# if __name__ == "__main__":
#     archivo_csv = 'data.csv'
#     letras_por_valor = agrupar_letras_por_valor_columna2(archivo_csv)
#     for valor, letras in letras_por_valor:
#         print(f'({valor}, {letras})')



def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """

import csv
from collections import defaultdict

def generar_lista_tuplas(csv_file):
    # Crear un diccionario para almacenar las letras asociadas a cada valor de la columna 2
    letras_por_valor = defaultdict(list)

    # Abrir el archivo CSV y leerlo
    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        # Iterar sobre cada fila del archivo
        for row in csv_reader:
            # Obtener la letra de la primera columna y el valor de la segunda columna
            letra = row[0]
            valor = int(row[1])
            # Agregar la letra a la lista correspondiente al valor en el diccionario
            letras_por_valor[valor].append(letra)

    # Crear una lista de tuplas (valor, lista de letras asociadas) ordenada por valor
    lista_tuplas = [(valor, sorted(set(letras))) for valor, letras in sorted(letras_por_valor.items())]

    return lista_tuplas

# if __name__ == "__main__":
#     archivo_csv = 'data.csv'
#     lista_tuplas = generar_lista_tuplas(archivo_csv)
#     for valor, letras in lista_tuplas:
#         print(f'({valor}, {letras})')



def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """

import csv
from collections import defaultdict

def contar_registros_por_clave_ordenado(csv_file):
    # Crear un diccionario para almacenar la cantidad de registros por clave
    registros_por_clave = defaultdict(int)

    # Abrir el archivo CSV y leerlo
    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        # Iterar sobre cada fila del archivo
        for row in csv_reader:
            # Obtener el diccionario codificado de la quinta columna
            diccionario_codificado = row[4]
            # Decodificar el diccionario
            diccionario_decodificado = dict(item.split(':') for item in diccionario_codificado.split(','))
            # Contar la cantidad de registros para cada clave en el diccionario
            for clave in diccionario_decodificado.keys():
                registros_por_clave[clave] += 1

    # Ordenar el diccionario por las claves alfabéticamente
    registros_por_clave_ordenado = dict(sorted(registros_por_clave.items()))

    return registros_por_clave_ordenado

# if __name__ == "__main__":
#     archivo_csv = 'data.csv'
#     registros_por_clave_ordenado = contar_registros_por_clave_ordenado(archivo_csv)
#     for clave, cantidad in registros_por_clave_ordenado.items():
#         print(f'"{clave}": {cantidad}')



def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """

import csv

def contar_elementos_columnas(csv_file):
    # Crear una lista para almacenar las tuplas con la cantidad de elementos en las columnas 4 y 5
    lista_tuplas = []

    # Abrir el archivo CSV y leerlo
    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        # Iterar sobre cada fila del archivo
        for row in csv_reader:
            # Contar los elementos en las columnas 4 y 5 para la fila actual
            elementos_columna4 = len(row[3].split(','))
            elementos_columna5 = len(row[4].split(','))
            # Agregar la tupla a la lista
            lista_tuplas.append((row[0], elementos_columna4, elementos_columna5))

    return lista_tuplas

# if __name__ == "__main__":
#     archivo_csv = 'data.csv'
#     lista_tuplas = contar_elementos_columnas(archivo_csv)
#     for tupla in lista_tuplas:
#         print(tupla)



def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """

import csv
from collections import defaultdict

def sumar_columna2_por_letra_columna4(csv_file):
    # Crear un diccionario para almacenar la suma de la columna 2 para cada letra de la columna 4
    suma_por_letra = defaultdict(int)

    # Abrir el archivo CSV y leerlo
    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        # Iterar sobre cada fila del archivo
        for row in csv_reader:
            # Obtener los elementos de la columna 4 y el valor de la columna 2
            elementos_columna4 = row[3].split(',')
            valor = int(row[1])
            # Sumar el valor a cada letra correspondiente en el diccionario
            for elemento in elementos_columna4:
                for letra in elemento:
                    suma_por_letra[letra] += valor

    # Ordenar el diccionario alfabéticamente por las claves
    suma_por_letra_ordenado = dict(sorted(suma_por_letra.items()))

    return suma_por_letra_ordenado

# if __name__ == "__main__":
#     archivo_csv = 'data.csv'
#     suma_por_letra = sumar_columna2_por_letra_columna4(archivo_csv)
#     for letra, suma in suma_por_letra.items():
#         print(f'"{letra}": {suma}')



def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """

import csv
from collections import defaultdict

def sumar_valores_claves_por_letra_columna1(csv_file):
    # Crear un diccionario para almacenar la suma de los valores de las claves por cada letra de la columna 1
    suma_valores_por_letra = defaultdict(int)

    # Abrir el archivo CSV y leerlo
    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        # Iterar sobre cada fila del archivo
        for row in csv_reader:
            # Obtener la letra de la columna 1 y los elementos de la columna 5
            letra_columna1 = row[0]
            elementos_columna5 = row[4].split(',')
            # Iterar sobre cada elemento y sumar los valores para cada clave
            for elemento in elementos_columna5:
                clave, valor = elemento.split(':')
                suma_valores_por_letra[letra_columna1] += int(valor)

    # Ordenar el diccionario alfabéticamente por las claves
    suma_valores_por_letra_ordenado = dict(sorted(suma_valores_por_letra.items()))

    return suma_valores_por_letra_ordenado

# if __name__ == "__main__":
#     archivo_csv = 'data.csv'
#     suma_valores_por_letra = sumar_valores_claves_por_letra_columna1(archivo_csv)
#     for letra, suma in suma_valores_por_letra.items():
#         print(f"'{letra}': {suma}")


