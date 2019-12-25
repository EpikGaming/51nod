def isPrime(num):
    if num == 1:
        return False
    for i in range(2,int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

N = int(input())
listA = []
for i in range(N):
    listA.append(int(input()))
for i in listA:
    if isPrime(i) == True:
        print("Yes")
    else:
        print("No")