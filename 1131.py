gr = 0
vi = 0
vg = 0
e = 0
while True:
    try:
        a, b = input().split()
        x = int(a)
        y = int(b)
        if x > y:
            vi+=1
            gr+=1
        elif y > x:
            vg+=1
            gr+=1
        else:
            e+=1
            gr+=1
        c = int(input('Novo grenal (1-sim 2-nao)\n'))
        if c == 2:
            break
    except ValueError:
        break
ven = 'nenhum'
if vi > vg:
    ven = 'Inter venceu mais'
elif vg > vi:
    ven = 'Gremio venceu mais'
else:
    ven = 'Nao houve vencedor'
print('{} grenais'.format(gr))
print('Inter:{}'.format(vi))
print('Gremio:{}'.format(vg))
print('Empates:{}'.format(e))
print('{}'.format(ven))
