for notas in range(0, 11):
    n = 0
    l = 0
    while True:
        a = float(input())
        if a < 0 or a > 10:
            print('nota invalida')
        else:
            n += a
            break
    while True:
        b = float(input())
        if b < 0 or b > 10:
            print('nota invalida')
        else:
            l += b
            break
    m = (n + l) / 2
    mf = '{:.2f}'.format(m)
    print('media =', mf)
    break
