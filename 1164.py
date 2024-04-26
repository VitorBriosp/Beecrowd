# -*- coding: utf-8 -*-
n = int(input())
divisores = 0
for i in range(1, n + 1):
    s = int(input())
    if s == 1:
        print(1,'nao eh perfeito')
    else:
        for a in range(1, s):
            if s == 1:
                print(1,'eh perfeito')
                break
            if s % a == 0:
                divisores+=a
            if divisores == s and a == s - 1:
                print('{} eh perfeito'.format(s))
                divisores-=divisores
            elif divisores != s and a == s - 1:
                print('{} nao eh perfeito'.format(s))
                divisores-=divisores
