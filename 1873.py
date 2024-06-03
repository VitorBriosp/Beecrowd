# -*- coding: utf-8 -*-
def venc(x, y):
    c = 0
    d = 0
    a = ['pedra', 'papel', 'tesoura', 'lagarto', 'spock']
    matriz = [
        ["empate", "sheldon", "rajesh", "rajesh", "sheldon"],
        ["rajesh", "empate", "sheldon", "sheldon", "rajesh"],
        ["sheldon", "rajesh", "empate", "rajesh", "sheldon"],
        ["sheldon", "rajesh", "sheldon", "empate", "rajesh"],
        ["rajesh", "sheldon", "rajesh", "sheldon", "empate"]
    ]
    for i in range(len(a)):
        if x == a[i]:
            c = i
            break
    for i in range(len(a)):
        if y == a[i]:
            d = i
            break
    print(matriz[c][d])
n = int(input())
for i in range(n):
    r, s = input().split()
    venc(r, s)
