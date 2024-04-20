# -*- coding: utf-8 -*-
while True:
    try:
        a, b = input().split()
        x = int(a)
        y = int(b)
        cal = x // 30
        cal2 = y // 6
        print('{:02}:{:02}'.format(cal, cal2))
    except EOFError:
        break
