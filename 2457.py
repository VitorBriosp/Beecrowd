# -*- coding: utf-8 -*-
def func(x, y):
    c = 0
    total = 0
    for i in y:
        if x in i:
            c+=1
            total+=1
        else:
            total+=1
    cal = c * 100 / total
    print('{:.1f}'.format(cal))
n = input()
s = input().split()
func(n, s)
