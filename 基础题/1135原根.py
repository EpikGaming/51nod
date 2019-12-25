def euler(P):
    ans = P
    for i in range(2,int(P ** 0.5 + 1)):
        if P % i == 0:
            ans -= ans / i
            while P % i == 0:
                P /= i
    if P > 1:
        ans -= ans / P
    return int(ans)

def FindPrimeFactor(P):
    x = P - 1
    i = 2
    listA = []
    while i * i < x:
        if x % i == 0:
            listA.append(i)
            while x % i == 0:
                x //= i
        i += 1
    return listA

def FindRoot(listA,P):
    i = 2
    while True:
        for j in listA:
            if pow(i,(P - 1) // j,P) == 1:
                break
        else:
            return i
            break
        i += 1
P = int(input())
listA = FindPrimeFactor(P)
print(FindRoot(listA,P))