# -*- coding: utf-8 -*-
a, b = input().split()
x = float(a)
y = float(b)
if x > 0:
    if y > 0:
        quadrante = 'Q1'
    elif y < 0:
        quadrante = 'Q4'
    else:
        quadrante = 'Eixo X'
elif x < 0:
    if y > 0:
        quadrante = 'Q2'
    elif y < 0:
        quadrante = 'Q3'
    else:
        quadrante = 'Eixo X'
else:
    if y > 0 or y < 0:
        quadrante = 'Eixo Y'
    else: quadrante = 'Origem'
print(quadrante)
