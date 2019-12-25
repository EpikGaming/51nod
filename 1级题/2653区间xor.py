def f(n):
    m = n % 4
    if m == 0:
        return n
    elif m == 1:
        return 1
    elif m == 2:
        return n + 1
    else:
        return 0
a,b = map(int,input().split())
print(f(b) ^ f(a - 1))