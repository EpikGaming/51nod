def package(N,W,cost,value):
    f = [0] * (W + 1)
    for i in range(N):
        for j in range(W,cost[i] - 1,-1):
            f[j] = max(f[j],f[j - cost[i]] + value[i])
    return f

N,W = map(int,input().split(" "))
listB = []
listC = []
for i in range(N):
    listA = input().split()
    listB.append(int(listA[0]))
    listC.append(int(listA[1]))
listD = package(N,W,listB,listC)
print(listD[-1])