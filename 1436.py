# -*- coding: utf-8 -*-
n = int(input())
for w in range(n):
    ncom = []
    s = input().split()
    for d in range(len(s)):
        z = int(s[d])
        if z >= 11 and z <= 20:
            ncom.append(z)
    nsor = sorted(ncom)
    ind = len(nsor) // 2
    print('Case {}: {}'.format(w + 1, ncom[ind]))
