# -*- coding: utf-8 -*-
while True:
    try:
        s = input()
        a = []
        b1 = 0
        b2 = 0
        som1 = 0
        som2 = 0
        cal1 = 1
        cal2 = 9
        for i in range(len(s)):
            if s[i] == '.' or s[i] == '-':
                pass
            else:
                n = int(s[i])
                a.append(n)
        for w in range(len(a) - 2):
            bacon = a[w] * cal1
            torresmo = a[w] * cal2
            som1+=bacon
            som2+=torresmo
            cal1+=1
            cal2-=1
        final1 = som1 % 11
        final2 = som2 % 11
        if final1 == a[9] or final1 == 10 and a[9] == 0:
            b1 += 1
        if final2 == a[10] or final2 == 10 and a[10] == 0:
            b2 += 1
        if b1 == 1 and b2 == 1:
            print('CPF valido')
        else:
            print('CPF invalido')
    except EOFError:
        break
