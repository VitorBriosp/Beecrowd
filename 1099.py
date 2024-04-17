# -*- coding: utf-8 -*-
n = int(input())
soma = 0
for a in range(n):
    s, p = input().split()
    x = int(s)
    y = int(p)
    if x > y:
        x, y = y, x
    for nums in range(x + 1, y):
        if nums % 2 != 0:
            soma+=nums
    print(soma)
    soma-=soma
