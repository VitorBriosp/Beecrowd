# -*- coding: utf-8 -*-
soma = 0
a=1
b=1
while True:
    soma+=a/b
    b+=1
    if b > 100:
        break
print('{:.2f}'.format(soma))
