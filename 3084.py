# -*- coding: utf-8 -*-
while True:
    try:
        a, b = input().split()
        x = int(a)
        y = int(b)
        cal = x // 30
        cal2 = y // 6
        if cal < 10:
            cal = '0{}'.format(x // 30)
        if cal2 < 10:
            cal2 = '0{}'.format(y // 6)
        print('{}:{}'.format(cal, cal2))
    except EOFError:
        break
