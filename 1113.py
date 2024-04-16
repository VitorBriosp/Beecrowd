# -*- coding: utf-8 -*-
while True:
    try:
        a, b = input().split()
        x = int(a)
        y = int(b)
        if x > y:
            print('Decrescente')
        elif y > x:
            print('Crescente')
        else:
            break
    except EOFError:
        break
