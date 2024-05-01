# -*- coding: utf-8 -*-
while True:
    try:
        n = input()
        if len(n) >= 10:
            print('palavrao')
        else:
            print('palavrinha')
    except EOFError:
        break
