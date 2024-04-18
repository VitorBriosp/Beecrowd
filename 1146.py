# -*- coding: utf-8 -*-
while True:
    try:
        n = int(input())
        if n == 0:
            break
        else:
            for i in range(1, n + 1):
                if i < n:
                    print(i, end=' ')
                if i == n:
                    print(i)
                    break
    except ValueError:
        break
