# -*- coding: utf-8 -*-
soma = 0
while True:
    try:
        a, b = input().split()
        x = int(a)
        y = int(b)
        if x > y:
            x, y = y, x
        if x <= 0 or y <= 0:
            break
        for n in range(x, y + 1):
            print(n, end=' ')
            soma+=n
        print('Sum={}'.format(soma))
        soma-=soma
    except ValueError:
        break
