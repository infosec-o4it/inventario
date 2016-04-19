# -*- coding: utf-8 -*-


def percen(tupla):
    total = 0
    for diccionario in tupla:
        total += diccionario.total
    porcen = {}
    for diccionario in tupla:
        porcen[diccionario.grado.nombre] = 0
    for diccionario in tupla:
        porcen[diccionario.grado.nombre] += (diccionario.total * 100.0) / total
    return porcen
