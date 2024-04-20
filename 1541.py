while True:
    try:
        x, y, z = input().split()
        a = int(x)
        b = int(y)
        c = int(z)
        at = (a * b) / (c / 100)
        lt = at ** 0.5
        print(int(lt))
    except ValueError:
        break
