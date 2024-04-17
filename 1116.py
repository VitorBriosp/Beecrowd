# -*- coding: utf-8 -*-
n = int(input())
for i in range(n):
    a, b = input().split()
    x = int(a)
    y = int(b)
    if y == 0:
        print('divisao impossivel')
    else:
        cal = x /y
        print('{:.1f}'.format(cal))
