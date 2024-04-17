# -*- coding: utf-8 -*-
a = 0
g = 0
d = 0
while True:
    try:
        t = int(input())
        if t == 1:
            a+=1
        elif t == 2:
            g+=1
        elif t == 3:
            d+=1
        elif t == 4:
            break
    except ValueError:
        break
print('MUITO OBRIGADO')
print('Alcool: {}'.format(a))
print('Gasolina: {}'.format(g))
print('Diesel: {}'.format(d))
