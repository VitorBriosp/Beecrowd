def doge(walter, spym):
    #spym[w] spym[w + 1]
    spym
    lar = 0
    for i in range(len(spym)):
        c = 0
        a = ''
        b = ''
        d = spym[i]
        for w in range(len(d)):
            if ord(d[w]) == 120:
                c+=1
            elif c ==  0:
                a+=d[w]
            elif c == 1:
                b+=d[w]
        a = int(a)
        b = int(b)
        lar+=1
        if lar == len(spym):
            if b - 1 == 1:
                print('{}x'.format(a * b))
            else:
                print('{}x{}'.format(a * b, b - 1))
            lar-=lar
        else:
            if b - 1 == 1:
                print('{}x'.format(a * b))
            else:
                print('{}x{}'.format(a * b, b - 1), end=' + ')
while True:
    try:
        n = int(input())
        s = input().split(' + ')
        doge(n, s)
    except EOFError:
        break
