# -*- coding: utf-8 -*-
n = int(input())
def func(nome, notas):
    nota = []
    if len(notas) == 1:
        notas+='0'
        n1 = float(notas[0])
        n2 = float(notas[1])
        nota+=[n1, n2]
        total = (nota[0] + nota[1]) / 2
    elif len(notas) >= 2:
        for g in range(len(notas)):
            nz = float(notas[g])
            nota+=[nz]
        if len(nota) == 2:
            total = (nota[0] + nota[1]) / 2
        else:
            if len(notas) == 4:
                n1, n2, n3, n4 = nota[0], nota[1], nota[2], nota[3]
                if n4 < n3 and n4 < n2 and n4 < n1:
                    pass
                else:
                    if n1 < n2 and n1 < n3:
                        nota[0] = n4
                    elif n2 < n1 and n2 < n3:
                        nota[1] = n4
                    else:
                        nota[2] = n4
            total = (nota[0] + nota[1] + nota[2]) / 3
    print('{}:'.format(nome), '{:.1f}'.format(total))
for i in range(n):
    s = input()
    a = input().split()
    func(s, a)
