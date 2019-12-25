N = int(input())
listA = []
listB = []
a = 0
for i in range(N):
    a += int(input())
    listA.append(a)
print(listA)
Q = int(input())
for j in range(Q):
    listC = input().split()
    a = int(listC[0])
    b = int(listC[1])
    if a == 1:
        listB.append(listA[b-1])
    else:
        listB.append(listA[a + b - 2] - listA[a - 2])
#print(listB)
for x in listB:
    print(x)

'''
给出一个长度为N的数组，进行Q次查询，查询从第i个元素开始长度为l的子段所有元素之和。
例如，1 3 7 9 -1，查询第2个元素开始长度为3的子段和，1 {3 7 9} -1。3 + 7 + 9 = 19，输出19。

前缀和问题
'''