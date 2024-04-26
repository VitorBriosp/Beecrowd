# -*- coding: utf-8 -*-
x = int(input())
a = 0
s = 0
while True:
    try:
        z = int(input())
        if z <= x:
            pass
        else:
            for i in range(x, z + 1):
                a+=i
                s+=1
                if a >= z:
                    break
            print(s)
            break
    except ValueError:
        break
