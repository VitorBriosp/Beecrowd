# -*- coding: utf-8 -*-
n = int(input())
c_ = 0
r_ = 0
s_ = 0
total = 0
for i in range(n):
    aa, b = input().split()
    a = int(aa)
    if b == 'C':
        c_+=a
        total+=a
    if b == 'R':
        r_+=a
        total+=a
    if b == 'S':
        s_+=a
        total+=a
    ufptc = (c_ / total) * 100
    ufptr = (r_ / total) * 100
    ufpts = (s_ /total) * 100
    ptc = '{:.2f}'.format(ufptc)
    ptr = '{:.2f}'.format(ufptr)
    pts = '{:.2f}'.format(ufpts)

print('Total:', total, 'cobaias')
print('Total de coelhos:', c_)
print('Total de ratos:', r_)
print('Total de sapos:', s_)
print('Percentual de coelhos:', ptc, '%')
print('Percentual de ratos:', ptr, '%')
print('Percentual de sapos:', pts, '%')
