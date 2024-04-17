# -*- coding: utf-8 -*-
a, b = input().split()
x = int(a)
y = int(b)
if x > y:
    y+=24
    res = y-x
    print('O JOGO DUROU {} HORA(S)'.format(res))
elif x < y:
    res = y - x
    print('O JOGO DUROU {} HORA(S)'.format(res))
else:
    print('O JOGO DUROU 24 HORA(S)')
