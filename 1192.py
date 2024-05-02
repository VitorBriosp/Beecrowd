# -*- coding: utf-8 -*-
n = int(input())
for i in range(n):
    a=input()
    x = int(a[0])
    y = a[1]
    z = int(a[2])
    if x == z:
        print(x*z)
    elif y.isupper():
        print(z - x)
    elif y.islower():
        print(z + x)
