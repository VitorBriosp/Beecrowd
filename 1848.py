s = 0
caw = 0
while caw < 3:
    try:
        a = input()
        if a == '---':
            s+=0
        elif a == '--*':
            s+=1
        elif a == '-*-':
            s+=2
        elif a == '-**':
            s+=3
        elif a == '*--':
            s+=4
        elif a == '*-*':
            s+=5
        elif a == '**-':
            s+=6
        elif a == '***':
            s+=7
        elif a == 'caw caw':
            print(s)
            s-=s
            caw+=1
    except ValueError:
        break
