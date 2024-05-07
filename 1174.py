# -*- coding: utf-8 -*-
i = 0
while True:
    try:
        n = float(input())
        if n <= 10:
            print('A[{}] = {}'.format(i,n))
        i+=1
    except EOFError:
        break
