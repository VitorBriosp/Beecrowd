# -*- coding: utf-8 -*-
jump = 0
while True:
    try:
        n = int(input())
        if jump:
            print('')
        jump = 1
        if n % 4 ==0 and n % 100 != 0:
            if n % 15 == 0:
                if n % 55 == 0:
                    print('This is leap year.')
                    print('This is huluculu festival year.')
                    print('This is bulukulu festival year.')
            if n % 15 != 0 and n % 55 == 0:
                print('This is leap year.')
                print('This is bulukulu festival year.')
            if n % 15 == 0 and n % 55 != 0:
                print('This is leap year.')
                print('This is huluculu festival year.')
            if n % 15 != 0 and n % 55 != 0:
                print('This is leap year.')
        elif n % 400 ==0:
            if n % 15 == 0:
                if n % 55 == 0:
                    print('This is leap year.')
                    print('This is huluculu festival year.')
                    print('This is bulukulu festival year.')
            if n % 15 != 0 and n % 55 == 0:
                print('This is leap year.')
                print('This is bulukulu festival year.')
            if n % 15 == 0 and n % 55 != 0:
                print('This is leap year.')
                print('This is huluculu festival year.')
            if n % 15 != 0 and n % 55 != 0:
                print('This is leap year.')
        elif n % 15 == 0 and n % 400 != 0 and n % 4 != 0 or n % 15 == 0 and n % 400 != 0 and n % 4 == 0 and n % 100 == 0:
            print('This is huluculu festival year.')
        elif n % 15 != 0 and n % 400 != 0 and n % 4 != 0 or n % 15 != 0 and n % 400 != 0 and n % 4 == 0 and n % 100 == 0:
            print('This is an ordinary year.')
    except EOFError:
        break
