# -*- coding: utf-8 -*-
n = int(input())
for i in range(n):
    a, b, c = input().split()
    x = float(a)
    y = float(b)
    z = float(c)
    p1 = x * 2
    p2 = y * 3
    p3 = z * 5
    med = (p1 + p2 + p3) / 10
    medf = '{:.1f}'.format(med)
    print(medf)
