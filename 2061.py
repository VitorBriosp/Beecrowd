# -*- coding: utf-8 -*-
a, b = input().split()
x = int(a)
y = int(b)
abas = x
for i in range(y):
    d = input()
    if d == 'fechou':
        abas+=1
    elif d == 'clicou':
        abas-=1
print(abas)
