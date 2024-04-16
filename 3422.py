# -*- coding: utf-8 -*-
n = int(input())
for i in range(n):
    a, y = input().split()
    x = int(a)
    if y == '1T':
        if x <= 45:
            print(x)
        else:
            print(45,'+',x - 45, sep='')
    if y == '2T':
        if x <= 45:
            print(45 + x)
        else:
            print(90,'+',x - 45, sep='')
