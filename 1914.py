# -*- coding: utf-8 -*-
n = int(input())
f = 0
for i in range(n):
    a, b, c, d = input().split()
    xx, yy = input().split()
    x = int(xx)
    y = int(yy)
    if (x + y) % 2 == 0:
        f = 'PAR'
    else:
        f = 'IMPAR'
    if f == b:
        print(a)
    else:
        print(c)
