# -*- coding: utf-8 -*-
n = input()
total = []
soma = 0
coluna = 11
for i in range(12):
    lista = []
    for j in range(12):
        a = float(input())
        lista.append(a)
        if j < coluna:
            soma+=lista[j]
    total.append(lista[i])
    coluna-=1
if n == 'S':
    print('{:.1f}'.format(soma))
elif n == 'M':
    print('{:.1f}'.format(soma / 66))
