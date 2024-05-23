# -*- coding: utf-8 -*-
import math
n = int(input())
for i in range(n):
    c = 0
    lista=[]
    s = input()
    for w in range(len(s)):
        if ord(s[w]) == 33:
            c+=1
        else:
            lista+=s[w]
    b = int(''.join(lista))
    soma = 1
    for k in range(b, 0, -c):
        soma*=k
    print(soma)
