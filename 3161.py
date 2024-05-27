# -*- coding: utf-8 -*-
def trocar(char):
    l = []
    for i in range(len(char)):
        if ord(char[i]) >= 65 and ord(char[i]) <= 90:
            c = ord(char[i]) + 32
            l+= chr(c)
        else:
            l+= char[i]
    charl = ''.join(l)
    return charl
def inversa(st):
    n = len(st)
    saida = ""
    for i in range(n-1, -1, -1):
        saida += st[i]
    return saida
def teste(palavra, frase, gos, det, inver):
    for i in range(len(palavra)):
        if palavra[i] in frase or inver[i] in frase:
            gos+= [palavra[i]]
        elif palavra[i] not in frase and inver[i] not in frase:
            det+= [palavra[i]]
    return gos, det
a,b = input().split()
x, y = int(a), int(b)
gosta = []
detesta = []
frutas = []
inverso = []
c = 0
d = 0
for w in range(x):
    s = input()
    ss = trocar(s)
    frutas+=[ss]
    invers = inversa(ss)
    inverso+=[invers]
f = []
for r in range(y):
    l = input()
    f+=l
po = ''.join(f)
tro = trocar(po)
tes = teste(frutas, tro, gosta, detesta, inverso)
for kkk in range(len(frutas)):
    if frutas[kkk] in gosta:
        print('Sheldon come a fruta {}'.format(frutas[kkk]))
    elif frutas[kkk] in detesta:
        print('Sheldon detesta a fruta {}'.format(frutas[kkk]))
