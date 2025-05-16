"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


import csv


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    cadena = {}

    with open("files/input/data.csv", mode="r", encoding="utf-8") as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter="\t")

        for fila in lector_csv:
            listaValores = fila[4].split(",")
            for valor in listaValores:
                claveValor = valor.split(":")
                if cadena.get(claveValor[0]) == None:
                    cadena[claveValor[0]] = [int(claveValor[1]), int(claveValor[1])]
                else:
                    if int(claveValor[1]) > cadena.get(claveValor[0])[1]:
                        (cadena.get(claveValor[0])[1]) = int(claveValor[1])
                    if int(claveValor[1]) < cadena.get(claveValor[0])[0]:
                        (cadena.get(claveValor[0])[0]) = int(claveValor[1])

    return sorted([(clave, valor[0], valor[1]) for clave, valor in cadena.items()])


if "__main__" in __name__:
    print(pregunta_06())