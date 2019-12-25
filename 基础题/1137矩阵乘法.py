
'''import re
import numpy as np
N = int(input())
listB = []
listD = []
for i in range(N):
    listA = input().split()
    listA = [int(x) for x in listA]
    listB.append(listA)
for j in range(N):
    listC = input().split()
    listC = [int(x) for x in listC]
    listD.append(listC)
ans = np.matmul(listB,listD)
for i in range(len(ans)):
    a = str(ans[i])
    a = re.sub("\[","",a)
    a = re.sub("\]","",a)
    print(a)
'''

N = int(input())
listB = []
listD = []
for i in range(N):
    listA = input().split()
    listA = [int(x) for x in listA]
    listB.append(listA)
for j in range(N):
    listC = input().split()
    listC = [int(x) for x in listC]
    listD.append(listC)
M = [[sum(a * b for a, b in zip(m1, m2)) for m2 in zip(*listD)] for m1 in listB]
for i in M:
    print(' '.join(map(str, i)))
