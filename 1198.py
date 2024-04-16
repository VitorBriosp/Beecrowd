# -*- coding: utf-8 -*-
while True:
    try:
        a, b = input().split()
        x = int(a)
        y = int(b)
        if x < y:
            print(y - x)
        else:
            print(x - y)
    except EOFError:
        break
