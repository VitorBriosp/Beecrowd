# -*- coding: utf-8 -*-
n = int(input())
for cupid in range(n):
    s = int(input())
    if s == 0:
        print('NULL')
    elif s % 2 == 0:
        print('EVEN', end=' ')
        if s > 0:
            print('POSITIVE')
        else: 
            print('NEGATIVE')
    else:
        print('ODD', end=' ')
        if s > 0:
            print('POSITIVE')
        else:
            print('NEGATIVE')
