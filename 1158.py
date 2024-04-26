# -*- coding: utf-8 -*-
n = int(input())
soma = 0
for i in range(n):
    a, b = input().split()
    x = int(a)
    y = int(b)
    for ant in range(x, x + y * 2):
        if ant % 2 != 0:
            soma+=ant
    print(soma)
    soma-=soma
