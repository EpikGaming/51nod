K,N = map(int,input().split())
listA = []
listB = []
for i in range(N):
    listA.append(int(input()))
listA = sorted(listA)
i,j = 0,N - 1
while i != j and i < j:
    if listA[i] + listA[j] < K:
        i += 1
    elif listA[i] + listA[j] > K:
        j -= 1
    elif listA[i] + listA[j] == K:
        listB.append((listA[i],listA[j]))
        i += 1
        j -= 1
if len(listB) == 0:
    print("No Solution")
else:
    for a,b in listB:
        print(a,b)