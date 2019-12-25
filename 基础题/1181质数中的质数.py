N = int(input())
max = 1000010
listA = [True] * max
listA[0] = listA[1] = False
listB = []
for i in range(2,max):
    if listA[i] == True:
        listB.append(i)
        for j in range(2,max // i):
            listA[i * j] = False
for j in range(N,max):
    if listA[j] == True and listA[listB.index(j)] == True:
        print(j)
        break
print(listB)
print(listA[N])