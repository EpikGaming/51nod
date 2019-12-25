#朴素搜索(超时)
def search(listA,a,b):
    listB = [0]
    for i in range(a,b + 1):
        if listA[i] > listB[-1]:
            listB.append(listA[i])
    return listB[-1]

N = int(input())
listA = []
listB = []
for i in range(N):
    listA.append(int(input()))
Q = int(input())
for j in range(Q):
    a,b = map(int,input().split(" "))
    listB.append(search(listA,a,b))
for i in listB:
    print(i)


#ST表搜索(超时爆内存)
import math
def ST(listA,a,b):
    listB = [[0] * N for i in range(N)]
    for i in range(len(listA)):
        listB[i][0] = listA[i]
    for j in range(1,int(math.log2(len(listA)) + 1)):
        for i in range(N - (2 ** j) + 1):
            listB[i][j] = max(listB[i][j - 1],listB[i + (2 ** (j - 1))][j - 1])
    if b - a == 1:
        ans = max(listB[a][0], listB[b][0])
    else:
        pos = int(math.log2(b - a + 1))
        ans = max(listB[a][pos],listB[b - (2 ** pos) + 1][pos])
    return ans

N = int(input())
listA = [int(input()) for i in range(N)]
listC = []
Q = int(input())
for i in range(Q):
    a,b = map(int,input().split())
    listC.append(ST(listA,a,b))
for j in listC:
    print(j)

#ST表搜索优化
def init(arr):
    arr_len = len(arr)
    exp = int(math.log(arr_len, 2))
    DP = [[0 for col in range(exp + 1)] for row in range(arr_len + 1)]
    for index, item in enumerate(arr):
        DP[index + 1][0] = item
    for e in range(1, exp + 1):
        for start in range(1, arr_len + 1):
            if start + (1 << e) - 1 > arr_len:
                break
            DP[start][e] = max(DP[start][e - 1], DP[start + (1 << (e - 1))][e - 1])
    return DP


def ask(DP, left, right):
    cut = int(math.log(right - left + 1, 2))
    return max(DP[left][cut], DP[right + 1 - (1 << cut)][cut])


arr = []
n = int(input())
for i in range(n):
    arr.append(int(input()))
DP = init(arr)
m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    print(ask(DP, a + 1, b + 1))


#线段树搜索
from bisect import bisect_right

def I():
    return int(input())

def build(A):
    S = [A]
    P = [1]
    lastS = A
    lastp = 1
    p = 2
    while p <= N:
        t = []
        for i in range(len(lastS) - lastp):
            t.append(max(lastS[i], lastS[i + lastp]))
        S.append(t)
        P.append(p)
        lastS = t
        lastp = p
        p *= 2
    return S, P

def query(L, R):
    Len = R - L + 1
    idx = bisect_right(P, Len) - 1
    p = P[idx]
    return max(S[idx][L], S[idx][R - p + 1])
N = I()
A = []
for _ in range(N):
    A.append(I())
S, P = build(A)
Q = I()
for _ in range(Q):
    L, R = map(int, input().split())
    print(query(L, R))