# -*- coding: utf-8 -*-
on = True
pa = 0
sss = 0
while on == True:
    try:
        if pa > 0:
            break
        n = float(input())
        if n < 0 or n > 10:
            print('nota invalida')
        while n >= 0 and n <= 10:
            try:
                if sss > 0:
                        break
                s = float(input())
                if s > 10 or s < 0:
                    print('nota invalida')
                else:
                    som = (n + s) /2
                    somf = '{:.2f}'.format(som)
                    print('media =',somf)
                    while s >= 0 and s <= 10:
                        print('novo calculo (1-sim 2-nao)')
                        t = int(input())
                        if t == 1:
                            n-=n + 1
                            s-=s + 1
                        elif t == 2:
                            pa+=t
                            sss+=t
                            break
                        else:
                            continue
            except ValueError:
                break
    except EOFError:
        break
