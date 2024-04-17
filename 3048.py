# -*- coding: utf-8 -*-
n = int(input())
c = 0
b = 0
for aa in range(n):
    a = int(input())
    if a != b:
        c+=1
    b = a
print(c)
