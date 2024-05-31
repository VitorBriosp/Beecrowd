# -*- coding: utf-8 -*-
n = input()
soma = 0
coluna = 11
for i in range(12):
    l = []
    for j in range(12):
        s = float(input())
        l.append(s)
        if j > i and j < coluna:
            soma+=l[j]
    coluna-=1
if n == 'S':
    print('{:.1f}'.format(soma))
elif n == 'M':
    print('{:.1f}'.format(soma / 30))
