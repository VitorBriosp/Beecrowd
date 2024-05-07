# -*- coding: utf-8 -*-
n = int(input())
for i in range(n):
    s = input()
    c = 0
    nf = 0
    for w in range(len(s)):
        a = s.upper()
        if a[w] in 'AEIOU':
            c-=c
        else:
            c+=1
        if c >=3:
            nf+=1
    if nf >= 1:
        print('{} nao eh facil'.format(s))
    else:
        print('{} eh facil'.format(s))
