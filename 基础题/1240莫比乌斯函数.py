def miu(N):
    if N == 1:
        return 1
    k = 0
    for i in range(2,int(N ** 0.5) + 1):
        if N % (i ** 2) == 0:
            return 0
    for i in range(2,int(N ** 0.5) + 1):
        if N % i == 0:
            k += 1
            N /= i
            continue
    if N > 1:
        k += 1
    return (-1) ** k


N = int(input())
print(miu(N))