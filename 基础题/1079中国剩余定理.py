def ex_gcd(a,b):
#用于求对应Mi模mi的数论倒数
    if b == 0:
        return 1,0
    x,y = ex_gcd(b,a % b)
    x,y = y,x - (a // b) * y
    return x,y
listA = []
listB = []
#listB存放质数
listC = []
#listC存放Kmod质数的结果
n = int(input())
M = 1
for i in range(n):
    listA = input().split()
    listB.append(int(listA[0]))
    listC.append(int(listA[1]))
for j in listB:
    M *= j
sum = 0
for i in range(n):
    #print(listB[i])
    m = M // listB[i]
    #print(m)
    x,y = ex_gcd(m,listB[i])
    z = x % listB[i]
    sum += listC[i] * z * m
print(sum % M)
'''
一个正整数K，给出K Mod 一些质数的结果，求符合条件的最小的K。
例如，K % 2 = 1, K % 3 = 2, K % 5 = 3。符合条件的最小的K = 23。

数论题，中国剩余定理（孙子定理）
M = a1 * a2 * a3 * …… * an
Mi = M / ai
扩展欧几里得算法求Mi模ai的数论倒数ti
答案解K = [(b1 * t1 * M1) + (b2 * t2 * M2) + …… +(bn * tn * Mn)] Mod M
Input:
3
2 1
3 2
5 3
Output:
23
'''