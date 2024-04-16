# -*- coding: utf-8 -*-
x = int(input())
y = int(input())
aux = x
soma = 0
if x > y:
    pass
else:
    x = y
    y = aux
for n in range(y + 1, x):
    if n % 2 != 0:
        soma+=n
print(soma)
