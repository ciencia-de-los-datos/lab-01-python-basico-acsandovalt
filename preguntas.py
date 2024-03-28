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

    suma = 0

    with open('data.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter='\t')
        
        for row in csv_reader:
            suma += int(row[1])

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

def pregunta_02():
    csv_file = 'data.csv'
    frecuencia_letras = defaultdict(int)

    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        for row in csv_reader:
            letra = row[0]
            frecuencia_letras[letra] += 1

    lista_duplas = list(frecuencia_letras.items())
    lista_duplas.sort(key=lambda x: x[0])

    return lista_duplas
    


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

def pregunta_03():
    csv_file = 'data.csv'
    suma_por_letra = defaultdict(int)
    
    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        for row in csv_reader:
            letra = row[0]
            numero = int(row[1])
            suma_por_letra[letra] += numero

    resultado = sorted(suma_por_letra.items())
    return resultado



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

def pregunta_04():
    csv_file = 'data.csv'
    registros_por_mes = defaultdict(int)

    
    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        for row in csv_reader:
            fecha = row[2]
            mes = fecha.split('-')[1]
            registros_por_mes[mes] += 1

    resultado = sorted(registros_por_mes.items())
    return resultado



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

def pregunta_05():
    csv_file = 'data.csv'
    max_min_por_letra = defaultdict(lambda: [float('-inf'), float('inf')])

    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        for row in csv_reader:
            letra = row[0]
            numero = int(row[1])
            max_min_por_letra[letra][0] = max(max_min_por_letra[letra][0], numero)  
            max_min_por_letra[letra][1] = min(max_min_por_letra[letra][1], numero)  
    
    resultado = [(letra, max_min[0], max_min[1]) for letra, max_min in sorted(max_min_por_letra.items())]
    return resultado



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

def pregunta_06():
    csv_file = 'data.csv'
    min_max_por_clave = defaultdict(lambda: [float('inf'), float('-inf')])

    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        for row in csv_reader:
            diccionario = row[4].split(',')  
            for elemento in diccionario:
                clave, valor = elemento.split(':')
                valor = int(valor)
                min_max_por_clave[clave][0] = min(min_max_por_clave[clave][0], valor)  
                min_max_por_clave[clave][1] = max(min_max_por_clave[clave][1], valor)  

    resultado = [(clave, min_max[0], min_max[1]) for clave, min_max in sorted(min_max_por_clave.items())]
    return resultado



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

def pregunta_07():
    csv_file = 'data.csv'
    asociaciones = defaultdict(list)

    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        for row in csv_reader:
            numero_columna_2 = int(row[1])
            letra_columna_1 = row[0]
            asociaciones[numero_columna_2].append(letra_columna_1)

    resultado = sorted(asociaciones.items())
    return resultado



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

def pregunta_08():
    csv_file = 'data.csv'
    asociaciones = defaultdict(list)

    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        for row in csv_reader:
            numero_columna_2 = int(row[1])
            letra_columna_1 = row[0]
            asociaciones[numero_columna_2].append(letra_columna_1)

    for numero, letras in asociaciones.items():
        asociaciones[numero] = sorted(set(letras))

    resultado = sorted(asociaciones.items())
    return resultado



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

def pregunta_09():
    csv_file = 'data.csv'
    clave_frecuencia = defaultdict(int)

    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        for row in csv_reader:
            valores_columna_5 = row[4].split(',')
            for valor in valores_columna_5:
                clave, _ = valor.split(':')
                clave_frecuencia[clave] += 1

    return clave_frecuencia



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

def pregunta_10():
    csv_file = 'data.csv'
    resultado = []

    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        for row in csv_reader:
            letra_columna_1 = row[0]
            elementos_columna_4 = len(row[3].split(','))
            elementos_columna_5 = sum(1 for clave_valor in row[4].split(',') if clave_valor.strip())
            resultado.append((letra_columna_1, elementos_columna_4, elementos_columna_5))

    return resultado



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

def pregunta_11():
    csv_file = 'data.csv'
    suma_por_letra = defaultdict(int)

    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        for row in csv_reader:
            letras_columna_4 = row[3].split(',')
            numero_columna_2 = int(row[1])
            for letra in letras_columna_4:
                suma_por_letra[letra] += numero_columna_2

    resultado = dict(sorted(suma_por_letra.items()))
    return resultado



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

def pregunta_12():
    csv_file = 'data.csv'
    suma_por_letra = defaultdict(int)

    with open(csv_file, 'r', newline='') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        for row in csv_reader:
            valores_columna_5 = row[4].split(',')
            for valor in valores_columna_5:
                clave, numero = valor.split(':')
                suma_por_letra[row[0]] += int(numero)

    return dict(suma_por_letra)

