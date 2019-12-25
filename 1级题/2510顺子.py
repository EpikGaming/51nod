n = int(input())
listA = [int(i) for i in input().split()]
W = int(input())
if n % W != 0:
    print("false")
    exit(0)
listA.sort()
while len(listA) != 0:
    i = listA[0]
    listB = [int(j) for j in range(i,W + i)]
    for i in range(W):
        if listB[i] not in listA:
            print("false")
            exit(0)
        else:
            listA.remove(listB[i])
if listA == []:
    print("true")