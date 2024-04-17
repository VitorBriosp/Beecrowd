# -*- coding: utf-8 -*-
contador = 0
a1 = int(input())
a2 = int(input())
a3 = int(input())
a4 = int(input())
a5 = int(input())
if a1 % 2 == 0:
    contador+=1
if a2 % 2 == 0:
    contador+=1
if a3 % 2 == 0:
    contador+=1
if a4 % 2 == 0:
    contador+=1
if a5 % 2 == 0:
    contador+=1
print('{} valores pares'.format(contador))
