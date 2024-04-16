# -*- coding: utf-8 -*-
senha = 2002
acesso = False
while acesso == False:
    n = int(input())
    if n != senha:
        print('Senha Invalida')
    else:
        print('Acesso Permitido')
        acesso = True
