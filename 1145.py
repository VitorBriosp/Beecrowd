# -*- coding: utf-8 -*-
a, b = input().split()
x = int(a)
y = int(b)
o = 1
for i in range(1, y + 1):
    if o < x:
        print(i, end=' ')
        o+=1
    else:
        print(i, end='\n')
        o-=o - 1
