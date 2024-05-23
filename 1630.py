# -*- coding: utf-8 -*-
import math
def mdc(f, g):
    while g:
        f, g = g, f % g
    return f
def estacas(x, y):
    per = 2 * (x + y)
    madico = mdc(x, y)
    calculo_estacas = per // madico
    return calculo_estacas
while True:
    try:
        c, d = input().split()
        a = int(c)
        b = int(d)
        print(estacas(a, b))
    except EOFError:
        break
