# -*- coding: utf-8 -*-
x = int(input())
y = int(input())
soma = 0
if x > y:
    x, y = y, x
for a in range(x, y + 1):
    if a % 13 != 0:
        soma+=a
print(soma)
