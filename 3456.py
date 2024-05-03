# -*- coding: utf-8 -*-
a = input()
while True:
    try:
        s = str(a)
        if int(a) >= 10:
            aa = s[len(s) - 1]
            aaa = s[:len(s) - 1]
            b = int(aa)
            c = int(aaa)
            a = b + c * 3
            print(s)
        else:
            print(s)
            break
    except EOFError:
        break
