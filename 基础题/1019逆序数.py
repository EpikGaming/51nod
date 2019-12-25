'''a = int(input())
listA = []
x = 0
for i in range(a):
    listA.append(int(input()))
#print(listA)
for i in range(a):
    for j in range(i + 1,a):
        if listA[i] > listA[j]:
            #print(listA[i],listA[j])
            x += 1
print(x)
超时

'''
def merge_sort(list,x,y):
    res = 0
    m = (x + y) // 2
    if x < m:
        res += merge_sort(list,x,m)
    if m + 1 < y:
        res += merge_sort(list,m+1,y)
    #递归拆分列表
    leftlist = list[x:m+1]
    rightlist = list[m+1:y+1]
    leftlist.append(float('inf'))
    rightlist.append(float('inf'))
    a,b = 0,0
    for i in range(x,y+1):
        if leftlist[a] < rightlist[b]:
            list[i] = leftlist[a]
            a += 1
        else:
            list[i] = rightlist[b]
            b += 1
            res += m - x + 1 - a
    return res
a = int(input())
listA = []
for i in range(a):
    listA.append(int(input()))
print(merge_sort(listA,0,a-1))


'''
在一个排列中，如果一对数的前后位置与大小顺序相反，即前面的数大于后面的数，那么它们就称为一个逆序。
一个排列中逆序的总数就称为这个排列的逆序数。
如2 4 3 1中，2 1，4 3，4 1，3 1是逆序，逆序数是4。给出一个整数序列，求该序列的逆序数。

分治法归并排序题，需要用到递归以及列表的切片，用普通排序会超时
Input：
4
2
4
3
1
Output：
4
'''