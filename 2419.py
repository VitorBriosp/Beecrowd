# -*- coding: utf-8 -*-
def separador(z):
    mat = [0] * len(z)
    for i in range(len(z)):
        mat[i] = z[i]
    return mat

'''
ESSA FUNÇÃO
'''
def dentro_dos_limites(i, j, x, y):
    return 0 <= i < x and 0 <= j < y

a, b = input().split()
x, y = int(a), int(b)
matriz = []
costa = 0

for pos in range(x):
    s = input()
    sep = separador(s)
    matriz.append(sep)

for i in range(x):
    for w in range(y):
        if matriz[i][w] == '#':
            if (dentro_dos_limites(i-1, w, x, y) and matriz[i-1][w] == '.') or \
               (dentro_dos_limites(i+1, w, x, y) and matriz[i+1][w] == '.') or \
               (dentro_dos_limites(i, w-1, x, y) and matriz[i][w-1] == '.') or \
               (dentro_dos_limites(i, w+1, x, y) and matriz[i][w+1] == '.') or \
               (i == 0) or (i == x-1) or (w == 0) or (w == y-1):
                costa += 1
print(costa)
