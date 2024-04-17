# -*- coding: utf-8 -*-
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
s = 0
p = 0
if a > 0:
    s+=a
    p+=1
if b > 0:
    s+=b
    p+=1
if c > 0:
    s+=c
    p+=1
if d > 0:
    s+=d
    p+=1
if e > 0:
    s+=e
    p+=1
if f > 0:
    s+=f
    p+=1
cal = s / p
print(p, 'valores positivos')
print('{:.1f}'.format(cal))
