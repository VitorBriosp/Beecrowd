# -*- coding: utf-8 -*-
n = int(input())
dias = 0
for i in range(n):
    s = float(input())
    while True:
        try:
            s*=0.5
            if s > 1:
                dias+=1
            else:
                dias+=1
                print('{} dias'.format(dias))
                dias-=dias
                break
        except ValueError:
            break
