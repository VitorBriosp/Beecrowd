# -*- coding: utf-8 -*-
soma = 0
a = 1
b = 1
while True:
    soma+=a/b
    a+=2
    b*=2
    if a > 39:
        break
print('{:.2f}'.format(soma))
