''''#o(n^2)DP算法
N = int(input())
listA = []
for i in range(N):
    listA.append(int(input()))
Lis = [1] * N
for i in range(N):
    for j in range(i):
        if listA[i] > listA[j] and Lis[i] < Lis[j] + 1:
            Lis[i] = Lis[j] + 1
Lis.sort()
print(Lis[-1])
'''

#o(nlgn)算法
N = int(input())
listA = []
for i in range(N):
    listA.append(int(input()))
listB = []
listB.append(int(listA[0]))
print(listA)
print(listB)
for i in range(1,N):
    if listA[i] > listB[-1]:
        listB.append(listA[i])
    else:
        low = 1
        high = len(listB)
        while low <= high:
            mid = (low + high) // 2
            if listA[i] > listB[mid - 1]:
                low = mid + 1
            else:
                high = mid -1
        listB[low - 1] = listA[i]
    print(listB)
print(listB)
print(len(listB))