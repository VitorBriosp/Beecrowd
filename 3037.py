# -*- coding: utf-8 -*-
jogo = int(input())
j = 0
m = 0
partida = 0
for i in range(jogo):
    for h in range(1, 6 + 1):
        a, b = input().split()
        x = int(a)
        d = int(b)
        pon = x * d
        if h <= 3:
            j+=pon
        if h > 3:
            m+=pon
    if j > m: 
        print('JOAO')
        j-=j
        m-=m
    else:
        print('MARIA')
        j-=j
        m-=m
