# -*- coding: utf-8 -*-
i = 0
m = 0
while True:
    a = int(input())
    i+=a
    m+=1
    if a < 0:
        i-=a
        m-=1
        cal = i / m
        calf = '{:.2f}'.format(cal)
        print(calf)
        break
