# -*- coding: utf-8 -*-
while True:
    try:
        s = input()
        c = 0
        for i in range(len(s)):
            b = s[i]
            if s[i] != ' ':
                if c == 0:
                    b = s[i].upper()
                    c+=1
                    print(b, end='')
                elif c == 1:
                    b = s[i].lower()
                    c-=1
                    print(b, end='')
            else:
                print(b, end='')
            if i == len(s) - 1:
                print()
    except EOFError:
        break
