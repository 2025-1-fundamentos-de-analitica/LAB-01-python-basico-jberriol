"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


import csv


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    diccionario = {}

    with open("files/input/data.csv", mode="r", encoding="utf-8") as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter="\t")
        for fila in lector_csv:
            listaValores = fila[4].split(",")
            for valor in listaValores:
                claveValor = valor.split(":")
                if diccionario.get(fila[0]) == None:
                    diccionario[fila[0]] = int(claveValor[1])
                else:
                    diccionario[fila[0]] += int(claveValor[1])

    return dict(sorted(diccionario.items()))