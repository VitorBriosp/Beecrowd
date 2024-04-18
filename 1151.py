# -*- coding: utf-8 -*-
n = int(input())
a = 0
b = 1
c = 1
for l in range(1, 3):
    if n == 1:
        print(a)
        break
    elif n == 2:
        print(a, b)
        break
for i in range(3, n + 1):
    if i == 3:
        if n == 3:
            print(a, b, c)
        else:
            print(a, b, c, end=' ')
    else:
        if i < n:
            print(c, end=' ')
        else:
            print(c)
    a = b
    b = c
    c = a + b
