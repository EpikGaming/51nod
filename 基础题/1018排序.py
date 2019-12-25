a = int(input())
listA = []
for i in range(a):
    listA.append(int(input()))
listA.sort()
for i in listA:
    print(i)

'''
给出N个整数，对着N个整数进行排序。

基础题，构造列表，插入数值，再用sort()进行列表内排序
Input：
5
5
4
3
2
1
Output：
1
2
3
4
5
'''