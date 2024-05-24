# -*- coding: utf-8 -*-
def monke(doge, karen, murphy):
    som = 0
    lilbro = 0
    for w in range(doge):
        lilbro+=int(murphy[w])
        som+=lilbro*karen
    return som
while True:
    a = input().split()
    x = int(a[0])
    y = int(a[1])
    if x == -1 and y == -1:
        break
    bigbro = input().split()
    print(monke(x, y, bigbro))
