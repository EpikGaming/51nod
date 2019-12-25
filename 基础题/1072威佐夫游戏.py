
def Wythoff(a,b):
    if a > b:
        a,b = b,a
    s = abs(a - b)
    res = (s * (5 ** 0.5 + 1) / 2)
    if int(res) == a:
        result = "B"
    else:
        result = "A"
    return result


n = int(input())
listA = []
listB = []
for i in range(n):
    listA = [int(i) for i in input().split()]
    result = Wythoff(listA[0],listA[1])
    listB.append(result)
print(listB)
for j in listB:
    print(j)


'''
有2堆石子。A B两个人轮流拿，A先拿。每次可以从一堆中取任意个或从2堆中取相同数量的石子，但不可不取。
拿到最后1颗石子的人获胜。假设A B都非常聪明，拿石子的过程中不会出现失误。给出2堆石子的数量，问最后谁能赢得比赛。
例如：2堆石子分别为3颗和5颗。那么不论A怎样拿，B都有对应的方法拿到最后1颗。

数论类博弈论问题，对于奇异局势，先手必败，当且仅当：
两堆石子数量为(x,y)(其中x < y)
(y - x) * (5 ** 0.5 + 1) / 2 == x 时
Input：
3
3 5
3 4
1 9
Output：
B
A
A
'''