# -*- coding: utf-8 -*-
a = input().split()
t = len(a) - 1
x = int(a[0])
y = int(a[t])
s = 0
for i in range(y):
    s+=x + i
print(s)
