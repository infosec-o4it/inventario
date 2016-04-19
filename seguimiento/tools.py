# -*- coding: utf-8 -*-


def percen(tupla, seccion):
    porcen = {}
    for diccionario in tupla:
        identidad = diccionario[seccion]
        porcen[identidad] = ((100.0 / (diccionario["cantidad"] * 5))
                             * diccionario["total"])
    return porcen


def hexargb(colorstring):
    colorstring = colorstring.strip()
    if colorstring[0] == '#':
        colorstring = colorstring[1:]
    if len(colorstring) == 4:
        colorstring = "0"+colorstring
    if len(colorstring) == 5:
        colorstring = "0"+colorstring
    if len(colorstring) != 6:
        raise ValueError("el valor # no es del fotmato #RRGGBB ") % colorstring
    r, g, b = colorstring[:2], colorstring[2:4], colorstring[4:]
    r, g, b = [int(n, 16) for n in (r, g, b)]
    return (r, g, b)


def escala(x):
    y = 13369356 - (13317081 * x) / 100
    return hexargb(str(hex(int(y))[2:]))
