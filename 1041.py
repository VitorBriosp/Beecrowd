'''
Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano.
A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).
'''

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
