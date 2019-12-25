n = int(input())
strA = ""
for i in range(n):
    listA = [int(i) for i in (input().split())]
    if listA[0] % (listA[1] + 1) == 0:
        strA += "B" + "\n"
    else:
        strA += "A" + "\n"
strA = strA[:-1]
print(strA)

'''
有一堆石子共有N个。A B两个人轮流拿，A先拿。每次最少拿1颗，最多拿K颗，拿到最后1颗石子的人获胜。
假设A B都非常聪明，拿石子的过程中不会出现失误。给出N和K，问最后谁能赢得比赛。
例如N = 3，K = 2。无论A如何拿，B都可以拿到最后1颗石子。

简单博弈论问题，对于石子总数N，只要N能被K+1整除，则每次总是后手的人获胜，
因为每当先手的人拿i个石子，后手的人总是能拿K+1-i个石子以保证获胜
Input：
4
3 2
4 2
7 3
8 3
Output：
B
A
A
B
'''