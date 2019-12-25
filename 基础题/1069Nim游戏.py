'''def change(a):
    #转二进制
    b = bin(a)
    return int(b[2:])

n = int(input())
listA = []
listB = []
for i in range(n):
    listA.append(int(input()))
#print(listA)
for j in listA:
    binary = change(j)
    listB.append(binary)
#print(listB)
result = 0
for x in listB:
    result = result ^ x
#print(result)
if result == 0:
    print("B")
else:
    print("A")
'''


n = int(input())
result = 0
for i in range(n):
    result = result ^ int(input())
print(result)
if result == 0:
    print("B")
else:
    print("A")

'''
有N堆石子。A B两个人轮流拿，A先拿。每次只能从一堆中取若干个，可将一堆全取走，但不可不取，拿到最后1颗石子的人获胜。
假设A B都非常聪明，拿石子的过程中不会出现失误。给出N及每堆石子的数量，问最后谁能赢得比赛。
例如：3堆石子，每堆1颗。A拿1颗，B拿1颗，此时还剩1堆，所以A可以拿到最后1颗石子。

位运算博弈论问题，对于N个石堆的不同石子数Xi，当且仅当所有Xi的异或和为0时为必败态
对于满足必败态的三个情况：
1.全0时，局面必败，异或和为0
2.X1^X2^……Xn != 0，一定存在某个合法的移动Xi->Xi'，使得X1^X2^……Xn == 0
3.X1^X2^……Xn == 0，一定不存在某个合法的移动Xi->Xi'，使得X1^X2^……Xn != 0
因为消去后的结果为Xi == Xi'，并不是一个合法的移动
Input：
3
1
1
1
Output：
A
'''