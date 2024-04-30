# -*- coding: utf-8 -*-
n = int(input())
men = 0
pos = 0
a = input().split()
for i in range(n):
    x = int(a[i])
    if i == 0:
        men = x
    if men > x:
        men = x
        pos = i
print('Menor valor: {}\nPosicao: {}'.format(men,pos))
