n = int(input())
t1 = 1
t2 = 2
t3 = 3
while n > 0:
        t1 = t2
        t2 = t3
        t3 = t1 + t2
        n -= (t3 - t2 - t1)
n += (t3 - t2 - t1)
print(t2 + n)
