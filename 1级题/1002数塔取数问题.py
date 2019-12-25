N = int(input())
listA = []
listB = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    listA.append([int(j) for j in input().split()])
for i in range(N):
    listB[N - 1][i] = listA[N - 1][i]
for i in range(N - 2,-1,-1):
    for j in range(i + 1):
        listB[i][j] = max(listB[i + 1][j],listB[i + 1][j + 1]) + listA[i][j]
print(listB[0][0])