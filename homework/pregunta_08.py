"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


import csv


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """

    diccionario = {}
    with open("files/input/data.csv", mode="r", encoding="utf-8") as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter="\t")
        for fila in lector_csv:
            if diccionario.get(int(fila[1])) == None:
                diccionario[int(fila[1])] = [fila[0]]
            else:
                if fila[0] in diccionario.get(int(fila[1])):
                    continue
                else:
                    diccionario.get(int(fila[1])).append(fila[0])

    return sorted([(clave, sorted(valor)) for clave, valor in diccionario.items()])