'''
Leia 2 valores inteiros (A e B). Após, o 
programa deve mostrar uma mensagem 
"Sao Multiplos" ou "Nao sao Multiplos",
indicando se os valores lidos são múltiplos entre si.
'''
# -*- coding: utf-8 -*-
a, b = input().split()
x = float(a)
y = float(b)
if x > y:
    x, y = y, x
if y % x == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
