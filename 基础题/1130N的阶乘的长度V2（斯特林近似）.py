import math
def Stirling(listA):
    listB = []
    for n in listA:
        x = n * math.log10(n / math.e) + 0.5 * math.log10(2 * math.pi * n)
        listB.append(int(x + 1))
    return listB

N = int(input())
listA = []
for i in range(N):
    listA.append(int(input()))
listB = Stirling(listA)
for i in listB:
    print(i)