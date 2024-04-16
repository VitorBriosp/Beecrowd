# -*- coding: utf-8 -*-
in_ = 0
out_ = 0
n = int(input())
for i in range(n):
    p = int(input())
    if p in range(10, 21):
        in_+=1
    else:
        out_+=1
print(in_, 'in')
print(out_, 'out')
        
